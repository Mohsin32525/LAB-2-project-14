# Protein Sequence Length and Signal Peptide Analysis

This repository includes the notebook **`plots.ipynb`**, designed to explore and visualize key characteristics of protein sequences in both **training** and **benchmarking** datasets.  
The analyses cover aspects such as **protein length**, **signal peptide (SP) features**, **amino acid composition**, **taxonomic origin**, and **SP cleavage site motifs**.

---

## 🔍 Objectives of the Analysis

This analysis aims to:

- Identify potential **dataset biases** (e.g., in length, amino acid composition, or taxonomy).  
- Evaluate whether sequence-derived features are **informative for classification tasks**.  
- Gain **biological insights** into signal peptide properties.  
- Compare and **highlight differences** between training and benchmarking datasets.

---

## ⚙️ Requirements

To run the notebook, install the following Python libraries:

```bash
pip install pandas numpy matplotlib seaborn logomaker
```
## Required libraries:
```
pandas

numpy

matplotlib

seaborn

logomaker (for generating sequence logos)
```
## Analyses Performed
## 1. Protein Length Distribution

Purpose:
Compares the overall lengths of protein sequences between positive and negative classes in both datasets.
This helps detect potential differences in sequence length distributions that may influence model performance.

## 2. Signal Peptide (SP) Length Distribution

Purpose:
Examines the lengths of signal peptides to determine whether their sizes vary between classes or across datasets.
This provides insights into possible biological or dataset-specific variations.

## 3. Amino Acid Composition Analysis

Purpose:
Analyzes the amino acid (AA) composition of signal peptides and compares it with the SwissProt background distribution.
This helps reveal amino acid usage biases typical of signal peptides compared to general proteins.

## 4. Taxonomic Classification

Purpose:
Investigates the taxonomic origins of proteins at both kingdom and species levels.
This step identifies taxonomic imbalances that could introduce bias into classification or training results.

## 5. Sequence Logos of SP Cleavage Sites

Purpose:
Generates sequence logos around signal peptide cleavage sites to visualize conserved sequence motifs and positional patterns.
These motifs help understand common biological signatures of signal peptide cleavage regions.

## Summary

By combining these analyses, this notebook helps uncover:

Structural and compositional biases in datasets

Taxonomic and biological differences between data subsets

Potentially informative sequence features for protein classification tasks


