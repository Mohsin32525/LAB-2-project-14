import pandas as pd
from sklearn.model_selection import train_test_split

# Paths to your TSVs
pos_file = "positive_representative_data.tsv"
neg_file = "negative_representative_data.tsv"

# Load TSVs
pos_df = pd.read_csv(pos_file, sep="\t")
neg_df = pd.read_csv(neg_file, sep="\t")

# Add Class column
pos_df['Class'] = 'Positive'
neg_df['Class'] = 'Negative'

# Add Set column (will assign training folds later)
pos_df['Set'] = ''
neg_df['Set'] = ''

# Split into training (80%) and benchmarking (20%)
pos_train, pos_benchmark = train_test_split(pos_df, test_size=0.2, random_state=42)
neg_train, neg_benchmark = train_test_split(neg_df, test_size=0.2, random_state=42)

# Assign 'Benchmark' label for benchmarking set
pos_benchmark['Set'] = 'Benchmark'
neg_benchmark['Set'] = 'Benchmark'

# Shuffle training sets and assign cross-validation folds (1-5)
pos_train = pos_train.sample(frac=1, random_state=42).reset_index(drop=True)
neg_train = neg_train.sample(frac=1, random_state=42).reset_index(drop=True)

for i, df in enumerate([pos_train, neg_train]):
    fold_numbers = [1,2,3,4,5] * (len(df)//5 + 1)
    df['Set'] = fold_numbers[:len(df)]

# Combine training sets and benchmarking sets
train_df = pd.concat([pos_train, neg_train]).sample(frac=1, random_state=42).reset_index(drop=True)
benchmark_df = pd.concat([pos_benchmark, neg_benchmark]).sample(frac=1, random_state=42).reset_index(drop=True)

# Optional: Combine all for a single prepare_dataset file
prepare_dataset_df = pd.concat([train_df, benchmark_df]).reset_index(drop=True)

# Save TSVs
train_df.to_csv("train_set.tsv", sep="\t", index=False)
benchmark_df.to_csv("benchmark_set.tsv", sep="\t", index=False)
prepare_dataset_df.to_csv("prepare_dataset.tsv", sep="\t", index=False)

print("Training and benchmarking sets created!")
print(f"Training set size: {len(train_df)}")
print(f"Benchmarking set size: {len(benchmark_df)}")
