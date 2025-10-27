# The Von Heijne Method for Signal Peptide Detection

This repository contains the implementation of the Von Heijne method for signal peptide (SP) cleavage site prediction. The method builds a Position-Specific Weight Matrix (PSWM) using experimentally validated protein sequences and compares them against background amino acid frequencies from SwissProt. A pseudocount of +1 was applied to avoid zero probabilities.

# Parameters considered for this method:

Amino acid window: [-13, +2] relative to the cleavage site

Background distribution: SwissProt amino acid frequencies

PSWM: built from positive examples (proteins with confirmed signal peptides)

Goal: identify likely cleavage sites by comparing observed amino acid frequencies with the background model

# PSWM Implementation

The notebook create_pswm.ipynb is used to build a Position-Specific Weight Matrix (PSWM) from a training dataset containing sequences and their annotated SPEnd index.

Input: DataFrame with protein sequences and SPEnd positions

Output: PSWM matrix representing log-odds scores for each amino acid at positions –13 to +2 around the cleavage site

A heatmap visualization of the PSWM can be generated to inspect the position-specific amino acid preferences.

# Evaluation of the Von Heijne Method

The script validation_and_testing_vonheijne.ipynb evaluates the performance of the algorithm in three steps:

# 1. Scoring with the PSWM

Each protein sequence is scanned using a sliding window of 14–15 amino acids.

For each window, a score is computed by summing log-odds values from the PSWM.

The highest-scoring window is retained as the predicted cleavage site.

# 2. Threshold Optimization (Validation Set)

Precision–Recall curves are computed on the validation set.

The best threshold for classifying sequences is chosen by maximizing the F1-score.

# 3. Testing and Metrics

Predictions on the test set are evaluated using the following metrics:

Matthews Correlation Coefficient (MCC)

Accuracy (ACC)

Precision (PPV)

Recall / Sensitivity (SEN)

# 5-Fold Cross-Validation

A more robust evaluation is performed using 5-fold cross-validation:

Splitting: In each fold, one set is used for testing, one set for validation, and the remaining three sets for training.

PSWM computation: The matrix is built for each fold using the selected training sets.

Metrics: MCC, PPV, ACC, and SEN are computed for each test set.

Visualization: Precision–Recall curves are plotted for each fold, highlighting the best threshold from the validation set.

# Results

After 5-fold cross-validation, the mean and standard deviation of each metric were calculated as follows:

## Results

After performing 5-fold cross-validation, the average performance metrics of the Von Heijne method are as follows:

| Metric        | Mean ± Std      |
|---------------|----------------|
| **MCC**       | 0.666 ± 0.011  |
| **Precision** | 0.670 ± 0.056  |
| **Accuracy**  | 0.931 ± 0.007  |
| **Sensitivity** | 0.745 ± 0.052 |

**Average Confusion Matrix:**

[[1704 82]

[ 55 162]]
