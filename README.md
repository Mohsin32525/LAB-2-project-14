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
# 🧬 Reducing Data Redundancy and Preparing Datasets

Prepare clean datasets for machine learning by removing redundancy and selecting representative sequences.

## Steps

1. **Cluster sequences** using MMSeqs2 to remove similar sequences.  
2. **Select representatives** with `filter_representatives.py`.  
3. **Split data** into 80% training and 20% testing (`split_train_test.py`).  
4. **Create 5-fold cross-validation** sets (`make_crossval_folds.py`).  
5. **Verify** results using `wc -l` and `uniq -c`.

## Output

- Non-redundant FASTA and filtered metadata files.  
- Training/test splits and fold assignments.

 Result: Clean, balanced, reproducible datasets for ML.



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
