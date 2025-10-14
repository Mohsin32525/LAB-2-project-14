#!/usr/bin/env python3
import pandas as pd

# Input TSVs
pos_tsv = "positive_dataset.tsv"
neg_tsv = "negative_dataset.tsv"
pos_cluster_map = "pos_clusters_cluster.tsv"
neg_cluster_map = "neg_clusters_cluster.tsv"

# Output representative-only TSVs
filtered_pos_tsv = "pos_representatives.tsv"
filtered_neg_tsv = "neg_representatives.tsv"

# Load representative IDs
def load_representatives(cluster_file):
    df = pd.read_csv(cluster_file, sep="\t", header=None, names=["SequenceID", "Representative"])
    return set(df["Representative"].unique())

pos_reps = load_representatives(pos_cluster_map)
neg_reps = load_representatives(neg_cluster_map)

# Load original TSVs
pos_data = pd.read_csv(pos_tsv, sep="\t")
neg_data = pd.read_csv(neg_tsv, sep="\t")

# Filter only representative entries
filtered_pos = pos_data[pos_data["EntryID"].isin(pos_reps)]
filtered_neg = neg_data[neg_data["EntryID"].isin(neg_reps)]

# Save filtered TSVs
filtered_pos.to_csv(filtered_pos_tsv, sep="\t", index=False)
filtered_neg.to_csv(filtered_neg_tsv, sep="\t", index=False)
print(f"✅ Representative TSVs created:\n {filtered_pos_tsv}\n {filtered_neg_tsv}")
