import pandas as pd

# Load training set
train_file = "data/train_set.tsv"  # correct folder path
train_df = pd.read_csv(train_file, sep='\t')

# Check the first few rows
print(train_df.head())
