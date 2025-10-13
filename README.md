# LAB-2-project-14
Laboratory of Bioinformatics 2 – Project Files

This repository includes all the scripts and data used for the Laboratory of Bioinformatics 2 course project.

## Table of Contents

- [Data Collection](#data-collection)
- [Data Preparation](#data-preparation)
- [Analysis](#analysis)
- [Feature Extraction](#feature-extraction)
- [Implement ML Algorithms](#implement-ml-algorithms)
- [Model Evaluation](#model-evaluation)
- [Discussion](#discussion)

## Data Collection


 It focuses on preparing and analyzing protein datasets retrieved from UniProt.

Positive Protein Set


Number of proteins: 2,949

Selection criteria: Proteins were retrieved from UniProt using the following filters:
```bash
existence level = 1, length ≥ 40 amino acids, reviewed entries, taxonomy ID = 2759, non-fragmented, and containing annotated signal peptides.(existence:1) AND (length:[40 TO ]) AND (reviewed:true) AND (taxonomy_id:2759) AND (fragment:false) AND (ft_signal_exp:)
```

API Endpoint:
https://rest.uniprot.org/uniprotkb/search?format=json&query=%28%28existence%3A1%29+AND+%28taxonomy_id%3A2759%29+AND+%28ft_signal_exp%3A*%29+AND+%28length%3A%5B40+TO+*%5D%29+AND+%28reviewed%3Atrue%29+AND+%28fragment%3Afalse%29%29&size=500

Negative Protein Set

Number of proteins: 20,615

Selection criteria: Proteins without annotated signal peptides but meeting other quality criteria:
```bash
existence = 1, length ≥ 40, reviewed, taxonomy ID = 2759, and non-fragmented.(existence:1) AND (length:[40 TO ]) AND (reviewed:true) AND (taxonomy_id:2759) AND (fragment:false) NOT (ft_signal:) AND ((cc_scl_term_exp:SL-0091) OR (cc_scl_term_exp:SL-0191) OR (cc_scl_term_exp:SL-0173) OR (cc_scl_term_exp:SL-0209) OR (cc_scl_term_exp:SL-0204) OR (cc_scl_term_exp:SL-0039))

```

API Endpoint:
https://rest.uniprot.org/uniprotkb/search?format=json&query=%28%28fragment%3Afalse%29+AND+%28reviewed%3Atrue%29+AND+%28existence%3A1%29+AND+%28taxonomy_id%3A2759%29+AND+%28length%3A%5B40+TO+*%5D%29+AND+NOT+%28ft_signal%3A*%29+AND+%28cc_scl_term_exp%3ASL-0091+OR+cc_scl_term_exp%3ASL-0191+OR+cc_scl_term_exp%3ASL-0173+OR+cc_scl_term_exp%3ASL-0209+OR+cc_scl_term_exp%3ASL-0204+OR+cc_scl_term_exp%3ASL-0039%29%29&size=500

Notes: This endpoint also returns results in chunks of 500 and requires pagination.


## 2. API-Based Data Retrieval

Two scripts were developed to automate dataset construction via the UniProt API:

- [get_dataset_pos.ipynb](get_dataset_pos.ipynb) → retrieves the **positive set**  
- [get_dataset_neg.ipynb](get_dataset_neg.ipynb) → retrieves the **negative set**  

Each script performs the API queries, outputs results in both **.tsv** and **.fasta** formats, and applies filtering rules:

- **Positive set**: sequences are retained only if they contain a signal peptide of at least 14 amino acids and a defined cleavage site.  
- **Negative set**: sequences are kept only if they contain a transmembrane helix within the first 90 residues.  


3. Data Collection Output

The retrieved datasets were stored in two complementary formats:

.tsv files → contain protein metadata.

Positive set: UniProt accession, organism name, kingdom, sequence length, signal peptide cleavage site position.

Negative set: UniProt accession, organism name, kingdom, sequence length, and presence/absence of a transmembrane helix in the first 90 residues.

.fasta files → contain the corresponding protein sequences.

### Summary of Retrieved Proteins

| Dataset              | Count  |
|----------------------|--------|
| Positive Set         | 2,932  |
| Negative Set         | 20,615 |
| Negatives with Helix | 1,384  |

## Data Preparation
# Reducing Data Redundancy and Preparing Datasets

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

## Step 1 — Clustering Sequences with MMSeqs2

Cluster positive and negative datasets independently to remove redundancy.


Commond
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
```
positive.fasta

negative.fasta
```

Output Files

| File                              | Description                          |
| --------------------------------- | ------------------------------------ |
| `positive_cluster_rep_seq.fasta`  | Representative sequences (positives) |
| `positive_cluster_all_seqs.fasta` | All cluster members (positives)      |
| `positive_cluster_cluster.tsv`    | Cluster mapping (positives)          |
| `negative_cluster_rep_seq.fasta`  | Representative sequences (negatives) |
| `negative_cluster_all_seqs.fasta` | All cluster members (negatives)      |
| `negative_cluster_cluster.tsv`    | Cluster mapping (negatives)          |

## Step 2 — Selecting Representative Sequences

Filters the .tsv metadata file to keep only representative sequences obtained after MMSeqs2 clustering.

Command
```
python scripts/filter_representatives.py input.tsv rep_sequences.fasta representatives.tsv


Inputs

input.tsv → Metadata file containing all sequences

rep.fasta → FASTA file with cluster representative sequences

output.tsv → Filtered metadata file (representatives only 
```
Example Usage
```
python3 scripts/filter_representatives.py positive.tsv positive_cluster_rep_seq.fasta positive_filtered.tsv
python3 scripts/filter_representatives.py negative.tsv negative_cluster_rep_seq.fasta negative_filtered.tsv
```
Output Files
📁 File	🧾 Description
positive_filtered.tsv	Filtered metadata for representative positive sequences (~2933 → ~1094)
negative_filtered.tsv	Filtered metadata for representative negative sequences (~20616 → ~8935)
| 📁 File                     | 🧾 Description                                                                 |
|-----------------------------|-------------------------------------------------------------------------------|
| `positive_filtered.tsv`      | Filtered metadata for representative positive sequences (~2933 → ~1094)       |
| `negative_filtered.tsv`      | Filtered metadata for representative negative sequences (~20616 → ~8935)     |
``
Ensures one representative per cluster, reducing redundancy.

## Step 3 — Splitting Training and Benchmarking Data

Command
```
python3 scripts/split_train_test.py positive_filtered.tsv positive_train.tsv positive_test.tsv
python3 scripts/split_train_test.py negative_filtered.tsv negative_train.tsv negative_test.tsv
```
| 📁 File               | 🧾 Description                                                |
|----------------------|---------------------------------------------------------------|
| `positive_train.tsv`  | 80% of positive representative sequences (training)          |
| `positive_test.tsv`   | 20% of positive representative sequences (testing)           |
| `negative_train.tsv`  | 80% of negative representative sequences (training)          |
| `negative_test.tsv`   | 20% of negative representative sequences (testing)           |

Split the non-redundant datasets into 80% training and 20% benchmarking/testing sets.

### Step 4 — Building 5-Fold Cross-Validation Subsets

Maintain balanced positive/negative ratios across 5 folds.

 Command
 ```
python3 scripts/make_crossval_folds.py positive_train.tsv negative_train.tsv train_folds.tsv
```
Outputfile

| 📁 **File**       | 🧾 **Description**                          |
| ----------------- | ------------------------------------------- |
| `train_folds.tsv` | Training sequences with assigned fold (1–5) |

Each sequence appears once in validation during cross-validation.

### Step 5 — Verification Steps

| 🧠 **Check**                 | 💻 **Command**                                                                    | 📊 **Expected Result**                        |
| ---------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------- |
| **Filtering effectiveness**  | `wc -l positive.tsv positive_filtered.tsv negative.tsv negative_filtered.tsv`     | Confirms reduced redundancy                   |
| **Train/test split (80/20)** | `wc -l positive_train.tsv positive_test.tsv negative_train.tsv negative_test.tsv` | Confirms 80/20 ratio                          |
| **5-fold balance**           | `cut -f7 train_folds.tsv \| sort \| uniq -c`                                      | Shows folds 1–5 with balanced sequence counts |

### Summary
By completing Practical Session I (Part B), we have:

🧹 Reduced redundancy in both positive & negative datasets (MMSeqs2)

🧬 Selected representative sequences

📑 Filtered metadata to keep only representatives

🔀 Split datasets into 80/20 training and benchmarking sets

🎯 Built 5-fold cross-validation subsets with balanced class ratios


 Result: Clean, balanced, reproducible datasets for ML.


## Analysis


Project Overview

The repository provides a foundation for protein sequence analysis, useful for tasks such as signal peptide prediction, dataset preparation, or other bioinformatics workflows. All codes are implemented in Python.

Contributors
four
MOHSIN

RAJAB

HASSAN

NADIR

Languages

Python – 100%
