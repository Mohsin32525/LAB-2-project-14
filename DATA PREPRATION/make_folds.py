# scripts/make_folds.py
import pandas as pd
from sklearn.model_selection import StratifiedKFold
import sys

# inputs
pos_file = sys.argv[1]
neg_file = sys.argv[2]
out_file = sys.argv[3]

# load training data
pos = pd.read_csv(pos_file, sep="\t")
neg = pd.read_csv(neg_file, sep="\t")

# add labels
pos["label"] = 1
neg["label"] = 0

# merge
df = pd.concat([pos, neg]).reset_index(drop=True)

# stratified 5-fold split
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
df["fold"] = -1
for fold, (_, val_idx) in enumerate(skf.split(df, df["label"])):
    df.loc[val_idx, "fold"] = fold

# save
df.to_csv(out_file, sep="\t", index=False)
