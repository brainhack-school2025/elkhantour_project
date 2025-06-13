# ⚙️ How to use cwas-rsfmri?

## BIDS-App principle
This pipeline follows the BIDS-App workflow. This means, it takes connectome files in BIDS-fortmat (BEP-017) as an input. 

In one simple command line, the wokflow will be launched.

### Example usage
```bash
cwas-rsfmri --bids_dir=bids_directory --output_dir=results --atlas_file=atlas.txt --atlas=example_atlas --phenotype_file=participants.tsv --group=diagnosis --case_id=NDD --control_id=HC --session=timepoint1 --task=task01 --run=01 --feature=denoiseSimple
```

## Options
### Paths
`--bids_dir` : BIDS directory where all the connectomes are located

`--output_dir` : Directory to save results. This folder will be automatically created

`--atlas_file`: Path to atlas description file (.txt or .tsv accepted)

`--phenotype_file`: Indicate the location of your phenotype file. 
Accepted extension file: .tsv .csv or .xlsx

### File selection
CWAS-rsfmri expect BIDS-formatted connectomes (following BEP-017). For more information, please see the [BEP-017 proposal](https://bids.neuroimaging.io/extensions/beps/bep_017.html).

To select specific task, run and atlas, please refer to your filename: `sub-{}_ses-{}_task-{}_run-{}_seg-{atlas}_desc-{feature}_relmat_.tsv`

`--atlas`: The name of your atlas as indicated in your filename.

`--feature`: Decription of the feature used for the denoising pipeline.

`--session`: Session to process.

`--task`: Task to process.

`--run`: Run to process.


### Phenotype precision
Required format and columns are indicated in bold, optional in italic.
|   participants_id  |    age     |     sex    |  diagnosis | *medication* | *sequence* |   *scan*   |
|--------------------|------------|------------|------------|--------------|------------|------------|
| sub-01             |   24       |      F     |     HC     |      NA      |     3T     |   Siemens  |
| sub-02             |   32       |      F     |    SCHZ    |     SSRI     |     1.5T   |   CimaX    |

From your phenotype file you can indicate the following flags:

`--group`: Indicate the column name. Group comparison to perform (e.g. diagnosis).

`--case_id`: Indicate the variable name of your case groupe (e.g. SCHZ).

`--control_id`: Indicate the variable name of your control groupe (e.g. HC).

*Optional*

`--scanner`: Indicate `True` if you have different scanner settings. Default to `False`.

`--sequence`: Indicate `True` if you have different sequence settings. Default to `False`.

`--medication`: Indicate `True` if you have medication indications. Default to `False`.