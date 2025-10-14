#!/usr/bin/env python3
import pandas as pd
from Bio import SeqIO

# -------------------------------
# Step 1: Define input files
# -------------------------------
# Filtered representative TSVs
pos_reps_tsv = "pos_representatives.tsv"
neg_reps_tsv = "neg_representatives.tsv"

# 5-fold training split
train_folds_tsv = "training_set_with_folds.tsv"
benchmark_tsv = "benchmark_set.tsv"

# Representative FASTA files
pos_fasta = "pos_clusters_rep_seq.fasta"
neg_fasta = "neg_clusters_rep_seq.fasta"

# Output files
train_out = "training_set_with_sequences.tsv"
bench_out = "benchmark_set_with_sequences.tsv"

# -------------------------------
# Step 2: Load representative FASTAs
# -------------------------------
def load_fasta_dict(fasta_file):
    """Returns a dict of {SequenceID: sequence}"""
    return {record.id: str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")}

pos_seqs = load_fasta_dict(pos_fasta)
neg_seqs = load_fasta_dict(neg_fasta)

all_seqs = {**pos_seqs, **neg_seqs}
print(f"✅ Loaded {len(all_seqs)} total representative sequences.")

# -------------------------------
# Step 3: Load TSVs
# -------------------------------
train_df = pd.read_csv(train_folds_tsv, sep="\t")
bench_df = pd.read_csv(benchmark_tsv, sep="\t")

# Combine representative TSVs for ID lookup
pos_ids = set(pd.read_csv(pos_reps_tsv, sep="\t")["EntryID"])
neg_ids = set(pd.read_csv(neg_reps_tsv, sep="\t")["EntryID"])
rep_ids = pos_ids.union(neg_ids)

# -------------------------------
# Step 4: Merge sequences safely
# -------------------------------
def merge_sequences(df, all_sequences, rep_ids):
    """Add sequence column only for valid representative IDs"""
    sequences = []
    missing_count = 0
    for entry in df["EntryID"]:
        if entry in rep_ids:
            sequences.append(all_sequences.get(entry, ""))
        else:
            sequences.append("")
            missing_count += 1
    if missing_count > 0:
        print(f"⚠️ Warning: {missing_count} sequences not found for entries in 'EntryID'.")
    df["Sequence"] = sequences
    return df

train_df = merge_sequences(train_df, all_seqs, rep_ids)
bench_df = merge_sequences(bench_df, all_seqs, rep_ids)

# -------------------------------
# Step 5: Save outputs
# -------------------------------
train_df.to_csv(train_out, sep="\t", index=False)
bench_df.to_csv(bench_out, sep="\t", index=False)

print(f"✅ Final merged datasets saved successfully:\n  • {train_out}\n  • {bench_out}")
