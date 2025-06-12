from cwas_rsfmri.run import run_pipeline
import numpy as np
import pandas as pd
import os
import json


def create_dummy_phenotype(bids_dir):
    # Create a dummy phenotype file
    phenotype_file = os.path.join(bids_dir, "phenotype.tsv")
    with open(phenotype_file, 'w') as f:
        f.write("participant_id\tdiagnosis\tsex\tage\tmedication\tsequence\tscan\n")
        f.write(f"sub-01\tNDD\tM\t28\tOlanzapine\tT3\tSiemens\n")
        f.write(f"sub-02\tHC\tF\t32\tBeta\tT1\tCimax\n")

def create_bids_dir_structure(bids_dir):
    # Create dataset_description.json
    dataset_description = {
        "Name": "Dummy BIDS Dataset",
        "BIDSVersion": "1.0.0",
        "License": "CC0",
        "Authors": ["Dummy Author"],
        "Acknowledgements": "This is a dummy dataset for testing purposes.",
        "HowToAcknowledge": "Please cite the original dataset.",
        "Funding": [],
        "ReferencesAndLinks": [],
        "DatasetDOI": ""
    }
    
    with open(os.path.join(bids_dir, 'dataset_description.json'), 'w') as f:
        json.dump(dataset_description, f, indent=4)
    
    # Create meas-PearsonCorrelation_relmat.json
    meas_json = {
        "Name": "Pearson Correlation Connectivity Matrix",
        "Description": "Connectivity matrix computed using Pearson correlation.",
        "BIDSVersion": "1.0.0"
    }
    
    with open(os.path.join(bids_dir, 'meas-PearsonCorrelation_relmat.json'), 'w') as f:
        json.dump(meas_json, f, indent=4)

def create_dummy_json(bids_dir, sub):
    confounds_json = os.path.join('{}_ses-{}_task-{}_run-{}_desc-{}_timeseries.json')

    json_file = os.path.join(bids_dir, sub, "ses-timepoint1", "func", 
                             confounds_json.format(sub, "timepoint1", 
                                                    "task01", "01", 
                                                    "denoiseSimple"))
    info = {
        "ConfoundRegressors" : [
            "cosine00",
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
        "MeanFramewiseDisplacement" : np.random.uniform(0.1, 0.8),  # Random value for testing
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
        connectome_file = os.path.join(sub_dir, sub_connectome)
        connectome = np.random.uniform(-10, 10, size=(4, 4))
        connectome = (connectome + connectome.T) / 2
        np.fill_diagonal(connectome, 1)
        
        labels = [0, 1, 2, 3]
        df = pd.DataFrame(connectome, columns=labels)
        df.to_csv(connectome_file, sep="\t", float_format="%.4f", index=False)
        
        create_dummy_json(bids_dir, sub)

def test_smoke(tmpdir):
    bids_dir = tmpdir.mkdir("data").mkdir("bids")
    #non_bids_dir = tmp_path / "non_bids"
    atlas_file = os.path.join(bids_dir, "example_atlas.tsv")
    phenotype_file = os.path.join(bids_dir, "phenotype.tsv")
    output_dir = os.path.join(bids_dir, "output")

    create_bids_dir_structure(bids_dir)
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