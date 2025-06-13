# 📊 Outputs

## Report json file
A json file will be generated in the output folder. This json contain the following information. You can verify if all subjects were processed, and which one were excluded.

```json
{
    "halfpipe_unprocessed": {
        "total_subjects": 2,
        "processed_subjects": 2,
        "unprocessed_subjects": 0,
        "unprocessed_subject_list": []
    },
    "Total subjects before FD rejection": 2,
    "N Subjects with mean FD>0.5": 0,
    "Subjects with mean FD>0.5": [],
    "Selected sample based on group variable": "diagnosis",
    "cases 1": "n=1",
    "controls 0": "n=1",
    "original sample": "n=2",
    "new sample": "n=2",
    "data points available": "10",
    "standardized estimators are based on diagnosis": "0"
}
```

## TSV file
3 tsv files are generated
- beta maps
- qvalues maps 
- Summary of beta & qvalues