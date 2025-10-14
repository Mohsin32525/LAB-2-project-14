#!/usr/bin/env python3
import pandas as pd
from sklearn.model_selection import StratifiedKFold

# Load training set
data = pd.read_csv("training_set.tsv", sep="\t")

# 5-fold stratified split
kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
data["Set"] = None
for i, (_, val_index) in enumerate(kf.split(data, data["Class"])):
    data.loc[val_index, "Set"] = f"Fold_{i+1}"

# Save
data.to_csv("training_set_with_folds.tsv", sep="\t", index=False)
print("✅ 5-fold cross-validation subsets created: training_set_with_folds.tsv")
