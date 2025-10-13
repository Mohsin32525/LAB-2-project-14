# 🧬 Signal Peptide Prediction — Data Preparation

This project focuses on preparing **non-redundant, balanced datasets** for signal peptide prediction using machine learning.

---

## 1. Overview

Once preliminary sequence data are collected, the dataset is divided into two main subsets:

- **Training set**: Used to train models, optimize hyperparameters, and perform cross-validation experiments.  
- **Benchmarking set**: Also called the holdout dataset, reserved for testing model generalization on never-seen-before data.

---

## 2. Benchmarking Set: Motivation

Cross-validation alone is not sufficient for an unbiased estimate of model performance:

- Hyperparameter tuning via cross-validation may introduce overfitting.  
- The holdout benchmarking dataset provides a stronger guarantee of **never-seen-before** evaluation.  
- Models trained on subsets of the training data during cross-validation may bias results.  
- Only the model evaluated on the benchmarking set is considered ready for production use.

---

## 3. Redundancy Reduction

Before splitting, it is essential to create a **non-redundant dataset**:

- Control sequence identity and alignment coverage.  
- Reduce redundancy using **clustering tools** (MMseqs2).  
- Select **one representative sequence per cluster**.  

Once redundancy is addressed, the data can safely be split randomly.

---

## 4. MMseqs2 Clustering

For clustering, **MMseqs2 v14.7e284** was used on both positive and negative datasets.

**Input files:**

- `positive_dataset.fasta`  
- `negative_dataset.fasta`  

**Outputs for negative dataset:**

| File | Description |
|------|-------------|
| `neg_cluster.tsv` | Maps each sequence ID to its cluster representative |
| `neg_rep_seq.fasta` | FASTA of all cluster representatives |
| `neg_all_seq.fasta` | All input sequences used for clustering |

**Outputs for positive dataset:**

| File | Description |
|------|-------------|
| `positive_cluster.tsv` | Maps each sequence ID to its cluster representative |
| `positive_rep_seq.fasta` | FASTA of all positive cluster representatives |
| `positive_all_seq.fasta` | All positive sequences used for clustering |

---

## 5. Results After Redundancy Filtering

| Type | Count |
|------|-------|
| Non-redundant positives | 1093 |
| Non-redundant negatives | 8934 |
| Non-redundant negatives with helix transmembrane | 636 |

---

## 6. Data Splitting Strategy

To ensure proper training and unbiased evaluation:

### Training vs. Benchmarking

- **80%** of both positive and negative sequences → training set  
- **20%** of both positive and negative sequences → benchmarking set (holdout)

### Cross-Validation on Training Data

- Generate **5-fold cross-validation subsets** from the training set  
- Preserve the **overall positive/negative ratio** in each fold  
- Store the fold assignment in a `.tsv` file for reproducibility

---

## 7. Dataset Structure

The final `.tsv` dataset generated using `prepare_dataset.py` contains the following columns:

| Column | Description |
|--------|-------------|
| `EntryID` | Unique identifier for each protein |
| `OrganismName` | Name of the source organism |
| `Kingdom` | Taxonomic kingdom of the protein |
| `SequenceLength` | Length of the protein sequence |
| `HelixDomain` | True/False for negative entries; NaN for positives |
| `Class` | Negative / Positive |
| `SPstart` | Signal peptide start (for positives) |
| `SPend` | Signal peptide end (for positives) |
| `Set` | Fold number (1–5) for training entries; `Benchmark` for benchmarking entries |
| `Sequence` | Amino acid sequence |

---

## 8. Resulting Dataset Sizes

| Dataset | Negatives | Positives |
|---------|-----------|-----------|
| Training Set (total) | 7147 | 874 |
| Benchmark Set | 1787 | 219 |
| **Total** | 8934 | 1093 |

---

## 9. Summary

By following this pipeline, we:

- Reduced redundancy in both positive and negative datasets using **MMseqs2**  
- Selected **representative sequences**  
- Split data into **training and benchmarking sets** (80/20)  
- Built **5-fold cross-validation splits** for training  
- Ensured reproducibility and balanced datasets  

> The resulting dataset is **clean, balanced, and ready for machine learning–based signal peptide prediction**.
