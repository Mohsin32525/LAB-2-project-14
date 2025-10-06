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

Parameters

--min-seq-id 0.3 → Cluster at 30% sequence identity

-c 0.4 → Minimum coverage 40%

--cov-mode 0 → Full-length alignment mode

--cluster-mode 1 → Greedy set cover clustering

Run separately for:

positive.fasta

negative.fasta

Output Files

| File                              | Description                          |
| --------------------------------- | ------------------------------------ |
| `positive_cluster_rep_seq.fasta`  | Representative sequences (positives) |
| `positive_cluster_all_seqs.fasta` | All cluster members (positives)      |
| `positive_cluster_cluster.tsv`    | Cluster mapping (positives)          |
| `negative_cluster_rep_seq.fasta`  | Representative sequences (negatives) |
| `negative_cluster_all_seqs.fasta` | All cluster members (negatives)      |
| `negative_cluster_cluster.tsv`    | Cluster mapping (negatives)          |

<details> <summary>🎯 <b>Step 4 — Building 5-Fold Cross-Validation Subsets</b></summary>

Maintain balanced positive/negative ratios across folds.
```
python3 scripts/make_crossval_folds.py positive_train.tsv negative_train.tsv train_folds.tsv
```
### Output File

| File | Description |
|------|--------------|
| `train_folds.tsv` | Training sequences with assigned fold (1–5) |
Each sequence appears once in validation during cross-validation.

</details>
### 🧾 Verification Steps

| Check                        | Command                                                                           | Expected Result                         |
|------------------------------|-----------------------------------------------------------------------------------|------------------------------------------|
| **Filtering effectiveness**  | `wc -l positive.tsv positive_filtered.tsv negative.tsv negative_filtered.tsv`     | Confirms reduced redundancy              |
| **Train/test split (80/20)** | `wc -l positive_train.tsv positive_test.tsv negative_train.tsv negative_test.tsv` | Confirms 80/20 ratio                     |
| **5-fold balance**           | `cut -f7 train_folds.tsv \| sort \| uniq -c`                                     | Shows folds 1–5 with balanced sequence counts |


