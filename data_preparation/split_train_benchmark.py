#!/usr/bin/env python3
import pandas as pd
from sklearn.model_selection import train_test_split

# Load representative TSVs
pos = pd.read_csv("pos_representatives.tsv", sep="\t")
neg = pd.read_csv("neg_representatives.tsv", sep="\t")

# 80/20 train/benchmark split
train_pos, bench_pos = train_test_split(pos, test_size=0.2, random_state=42)
train_neg, bench_neg = train_test_split(neg, test_size=0.2, random_state=42)

# Add Class labels
for df in [train_pos, bench_pos]:
    df["Class"] = "Positive"
for df in [train_neg, bench_neg]:
    df["Class"] = "Negative"

# Merge positive + negative
train = pd.concat([train_pos, train_neg])
bench = pd.concat([bench_pos, bench_neg])

# Save outputs
train.to_csv("training_set.tsv", sep="\t", index=False)
bench.to_csv("benchmark_set.tsv", sep="\t", index=False)
print("✅ Data split complete:")
print(f"Training set: {train.shape[0]} entries")
print(f"Benchmark set: {bench.shape[0]} entries")
