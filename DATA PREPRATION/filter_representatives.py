# scripts/filter_representatives.py
import pandas as pd
from Bio import SeqIO
import sys

tsv_file = sys.argv[1]       # input TSV
rep_fasta = sys.argv[2]      # representative FASTA
out_tsv = sys.argv[3]        # output TSV

# load representative IDs from fasta
rep_ids = {rec.id for rec in SeqIO.parse(rep_fasta, "fasta")}

# load TSV
df = pd.read_csv(tsv_file, sep="\t")

# use the first column (Accession) as identifier
id_col = df.columns[0]

# filter rows where Accession is in representative IDs
df_filtered = df[df[id_col].isin(rep_ids)]

# save
df_filtered.to_csv(out_tsv, sep="\t", index=False)
