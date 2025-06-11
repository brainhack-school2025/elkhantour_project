from cwas_rsfmri.run import run_pipeline
from importlib import resources
import pytest
import os
import json

def create_dummy_phenotype(bids_dir):
    # Create a dummy phenotype file
    phenotype_file = os.path.join(bids_dir, "phenotype.tsv")
    with open(phenotype_file, 'w') as f:
        f.write("participant_id\tdiagnosis\tsex\tage\tmedication\tsequence\tscan\n")
        f.write(f"sub-01\tNDD\tM\t28\tOlanzapine\tT3\tSiemens\n")
        f.write(f"sub-02\tHC\tF\t32\tBeta\tT1\tCimax\n")

def create_dummy_json(bids_dir, sub):
    confounds_json = os.path.join('{}_ses-{}_task-{}_run-{}_desc-{}_timeseries.json')

    json_file = os.path.join(bids_dir, sub, "ses-timepoint1", "func", 
                             confounds_json.format(sub, "timepoint1", 
                                                    "task01", "01", 
                                                    "denoiseSimple"))
    info = {
        "ConfoundRegressors" : [
            "cosine00",
            "cosine01",
            "cosine03",
            "rot_x",
            "rot_x_derivative1",
            "rot_y",
            "rot_y_derivative1",
            "rot_z",
            "rot_z_derivative1",
        ],
        "ICAAROMANoiseComponents" : [
            "aroma_motion_01",
            "aroma_motion_02",
            ],
        "NumberOfVolumesDiscardedByMotionScrubbing" : 0,
        "NumberOfVolumesDiscardedByNonsteadyStatesDetector" : 1,
        "MeanFramewiseDisplacement" : 0.07,
        "SamplingFrequency" : 0.5
    }


    with open(json_file, "w") as outfile:
        json.dump(info, outfile, indent=6)

def create_dummy_data(bids_dir):
    print("Creating dummy data for testing...")
    
    # Create a dummy BIDS directory structure with 2 subjects
    # A matrix of 4x4
    connectome_t = os.path.join('{}', 'ses-{}', 'func')

    for sub in ["sub-01", "sub-02"]:
        sub_dir = os.path.join(bids_dir, connectome_t.format(sub, "timepoint1"))
        os.makedirs(sub_dir, exist_ok=True)
        sub_connectome = "{}_ses-{}_task-{}_run-{}_seg-{}_meas-PearsonCorrelation_desc-{}_relmat.tsv".format(sub, 
                                                                                                            "timepoint1", 
                                                                                                            "task01", 
                                                                                                            "01", 
                                                                                                            "example_atlas", 
                                                                                                            "denoiseSimple")
        # Create a dummy atlas file
        atlas_file = os.path.join(bids_dir, "example_atlas.tsv")
        with open(atlas_file, 'w') as f:
            f.write("0\tRegion1\n1\tRegion2\n2\tRegion3\n3\tRegion4\n")

        # Create dummy connectome data
        # TODO : Write with numpy
        connectome_file = os.path.join(sub_dir, sub_connectome)
        with open(connectome_file, 'w') as f:
            f.write("0\t1\t2\t3\n0.1\t0.2\t0.3\t0.4\n0.2\t0.1\t0.4\t0.3\n0.3\t0.4\t0.1\t0.2\n0.4\t0.3\t0.2\t0.1\n")

        create_dummy_json(bids_dir, sub)

def test_smoke():
    bids_dir = resources.files("cwas_rsfmri") / "tests/data/bids"
    #non_bids_dir = tmp_path / "non_bids"
    atlas_file = os.path.join(bids_dir, "example_atlas.tsv")
    phenotype_file = os.path.join(bids_dir, "phenotype.tsv")
    output_dir = os.path.join(bids_dir, "output")

    create_dummy_data(bids_dir)
    create_dummy_phenotype(bids_dir)

    # Without scanner, sequence, medication
    run_pipeline(bids_dir=bids_dir, 
                output_dir=output_dir, 
                atlas_file=atlas_file,
                atlas="example_atlas", 
                pheno_p=phenotype_file,
                scanner=False, 
                sequence=False, 
                medication=False, 
                group="diagnosis",
                case_name="NDD", 
                control_name="HC",
                session="timepoint1",
                task="task01",
                run="01",
                feature="denoiseSimple")
    
    # Expect X participants with FD mean >0.5
    assert os.path.exists(output_dir), "Output directory was not created"
