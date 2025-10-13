import pandas as pd
from sklearn.model_selection import KFold

# Load the training set
train_df = pd.read_csv("train_set.tsv", sep="\t")

# Initialize 5-fold cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Assign fold numbers (1–5)
train_df["Set"] = 0
for fold, (_, val_idx) in enumerate(kf.split(train_df), start=1):
    train_df.loc[val_idx, "Set"] = fold

# Save updated training file
train_df.to_csv("train_set_folds.tsv", sep="\t", index=False)
print("5-fold training set created successfully!")
