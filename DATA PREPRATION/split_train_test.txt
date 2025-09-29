# scripts/split_train_test.py
import pandas as pd
import sys

tsv_file = sys.argv[1]
out_train = sys.argv[2]
out_test = sys.argv[3]

# read input
df = pd.read_csv(tsv_file, sep="\t")

# 80% training, 20% test
train = df.sample(frac=0.8, random_state=42)  # fixed seed for reproducibility
test = df.drop(train.index)

# save
train.to_csv(out_train, sep="\t", index=False)
test.to_csv(out_test, sep="\t", index=False)
