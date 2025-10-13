import pandas as pd
from sklearn.model_selection import train_test_split

# Load TSVs
pos_df = pd.read_csv("data/positive_representative_data.tsv", sep="\t")
neg_df = pd.read_csv("data/negative_representative_data.tsv", sep="\t")

# Split positive sequences (80% train, 20% benchmark)
pos_train, pos_benchmark = train_test_split(pos_df, test_size=0.2, random_state=42)

# Split negative sequences (80% train, 20% benchmark)
neg_train, neg_benchmark = train_test_split(neg_df, test_size=0.2, random_state=42)

# Merge positive and negative sets
train_df = pd.concat([pos_train, neg_train]).sample(frac=1, random_state=42)  # shuffle
benchmark_df = pd.concat([pos_benchmark, neg_benchmark]).sample(frac=1, random_state=42)

# Save output files
train_df.to_csv("train_set.tsv", sep="\t", index=False)
benchmark_df.to_csv("benchmark_set.tsv", sep="\t", index=False)

print("Training and benchmarking sets created!")
print(f"Training set size: {len(train_df)}")
print(f"Benchmarking set size: {len(benchmark_df)}")

