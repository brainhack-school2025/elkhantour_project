import os
import numpy as np
import pandas as pd
from pathlib import Path

def create_output_directory(out_p):
    """
    Create output directory if it doesn't exist.
    
    Args:
        out_p (str): Path to the output directory.
    """
    out_p = Path(out_p)
    out_p.mkdir(parents=True, exist_ok=True)
    print(f"Output directory created at: {out_p}")
    return out_p

def find_halfpipe_output(working_directory):
    reports_dir = os.path.join(working_directory, "reports") # Path to report folder
    connectome_t = os.path.join('{}', 'ses-{}', 'func', "{}_ses-{}_task-{}_run-{}_seg-{}_meas-PearsonCorrelation_desc-{}_relmat.tsv")
    confounds_json = os.path.join('{}_ses-{}_task-{}_run-{}_desc-{}_timeseries.json')

    dict_halfpipe = {
        "reports_dir": reports_dir,
        "connectome_t": connectome_t,
        "confounds_json": confounds_json}
    
    return dict_halfpipe
    
def verify_atlas_files(atlas_file) :

    # 1. Verify atlas path
    print("Verifying altas location ...")
    print("path to access atlas:", atlas_file)
    
    if not os.path.exists(atlas_file):
        raise FileNotFoundError(f"Missing required file: {atlas_file}")
    
    labels = pd.read_csv(atlas_file, sep='\t', header=None)

    conn_mask = np.tril(np.ones((len(labels),len(labels)))).astype(bool)
    roi_labels = labels[1].to_list()

    return conn_mask, roi_labels
    

def verify_working_directory(working_directory) :
    print("\nVerifying working directory location ...")
    print("Path to access working directory:", working_directory)
    
    if not os.path.exists(working_directory):
        raise FileNotFoundError(f"Missing exclude.json in reports directory: {working_directory}")
    

def verify_exclude_json(json_exclude_qc_path, reports_dir) :
    print("\nVerifying exlude.json file location ...")
    print("Path to access reports folder:", reports_dir)

    if not os.path.exists(reports_dir):
        raise FileNotFoundError(f"Missing reports directory: {reports_dir}")
    
    exclude_file = json_exclude_qc_path
    print("Path to access exclude.json file:", exclude_file)
    
    if not os.path.exists(exclude_file):
        raise FileNotFoundError(f"Missing exclude.json in reports directory: {exclude_file}")
    
    print("\nAll required files and folder verified successfully")

    return True

def verify_files_and_directories(working_directory, json_exclude_qc_path, reports_dir, out_p):
    """
    Verify all required files and directories exist.
    
    Args:
        atlas_file (str): Path to the atlas file.
        working_directory (str): Path to the working directory.
        json_exclude_qc_path (str): Path to the exclude.json file.
    
    Returns:
        bool: True if all verifications pass, raises an error otherwise.
    """
    verify_working_directory(working_directory)
    verify_exclude_json(json_exclude_qc_path, reports_dir)
    create_output_directory(out_p)