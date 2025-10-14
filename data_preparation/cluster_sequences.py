#!/usr/bin/env python3
import subprocess

# Input FASTA files
positive_input = "positive_dataset.fasta"
negative_input = "negative_dataset.fasta"

# Output prefixes
pos_prefix = "pos_clusters"
neg_prefix = "neg_clusters"

# Temporary folders
tmp_pos = "tmp_pos"
tmp_neg = "tmp_neg"

# Run MMseqs2 clustering
def run_mmseqs(input_file, prefix, tmp_dir):
    cmd = [
        "mmseqs", "easy-cluster", input_file, prefix, tmp_dir,
        "--min-seq-id", "0.3",
        "-c", "0.4",
        "--cov-mode", "0",
        "--cluster-mode", "1"
    ]
    print(f"\nRunning MMseqs2 clustering for {input_file}...")
    subprocess.run(cmd, check=True)
    print(f"✅ Clustering completed for {input_file}")
    print(f"Generated files: {prefix}_rep_seq.fasta, {prefix}_cluster.tsv")

run_mmseqs(positive_input, pos_prefix, tmp_pos)
run_mmseqs(negative_input, neg_prefix, tmp_neg)
print("\nAll clustering runs completed successfully.")
