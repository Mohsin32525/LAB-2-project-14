Scripts Overview
1. filter_representatives.py

Filters the .tsv metadata file to keep only the representative sequences obtained after MMseqs2 clustering.

Inputs:

input.tsv → metadata file containing all sequences

rep.fasta → FASTA file with cluster representative sequences

output.tsv → filtered metadata file (representatives only)

```bash

python scripts/filter_representatives.py input.tsv rep_sequences.fasta representatives.tsv
```

2. make_folds.py

Generates stratified 5-fold cross-validation splits from the non-redundant dataset. Ensures that each fold preserves the class balance between positive and negative sequences.

Inputs:

positives.tsv → filtered positive dataset

negatives.tsv → filtered negative dataset

output.tsv → combined dataset with assigned fold numbers

```bash

python scripts/make_folds.py positives.tsv negatives.tsv dataset_with_folds.tsv

3. split_train_test.py
```

Splits the dataset into 80% training and 20% benchmarking (holdout) sets.
A fixed random seed (42) ensures reproducibility.

Inputs:

input.tsv → full dataset (representatives)

train.tsv → training set output file

test.tsv → benchmarking set output file

Usage:

python scripts/split_train_test.py dataset_with_folds.tsv train.tsv test.tsv

## Workflow

Run filter_representatives.py to keep only representative sequences after clustering.

Use split_train_test.py to divide the dataset into training (80%) and benchmarking (20%) sets.

Apply make_folds.py on the training data to generate stratified 5-fold cross-validation subsets.

📊 Output Files

representatives.tsv → metadata for non-redundant representatives.

train.tsv → training set (80%).

test.tsv → benchmarking set (20%).

dataset_with_folds.tsv → combined dataset with cross-validation fold assignments.
