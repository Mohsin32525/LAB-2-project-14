# 🧬 Practical Session I (Part B) — Reducing Data Redundancy and Preparing Datasets

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![MMSeqs2](https://img.shields.io/badge/MMSeqs2-%E2%9C%94-green)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Workflow](https://img.shields.io/badge/Data%20Processing-Bioinformatics-purple.svg)

> **Goal:** Prepare clean, non-redundant datasets for downstream machine learning by reducing redundancy, selecting representative sequences, and organizing the data into structured training, benchmarking, and cross-validation subsets.

---

##  Overview

| Step | Task | Tool/Script |
|------|------|-------------|
| 1️⃣ | Cluster positive & negative sequences | **MMSeqs2** |
| 2️⃣ | Select representative sequences | `filter_representatives.py` |
| 3️⃣ | Split data into training (80%) & test (20%) | `split_train_test.py` |
| 4️⃣ | Build 5-fold cross-validation subsets | `make_crossval_folds.py` |
| 5️⃣ | Verify dataset structure | Bash utilities |

---

<details>
<summary> <b>Step 1 — Clustering Sequences with MMSeqs2</b></summary>

Cluster positive and negative datasets independently to remove redundancy.

```bash
mmseqs easy-cluster input.fa cluster-results tmp --min-seq-id 0.3 -c 0.4 --cov-mode 0 --cluster-mode 1



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
