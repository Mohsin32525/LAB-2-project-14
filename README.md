# LAB-2-project-14
Laboratory of Bioinformatics 2 – Project Files

This repository includes all the scripts and data used for the Laboratory of Bioinformatics 2 course project. It focuses on preparing and analyzing protein datasets retrieved from UniProt.

Positive Protein Set


Number of proteins: 2,949

Selection criteria: Proteins were retrieved from UniProt using the following filters: existence level = 1, length ≥ 40 amino acids, reviewed entries, taxonomy ID = 2759, non-fragmented, and containing annotated signal peptides.(existence:1) AND (length:[40 TO ]) AND (reviewed:true) AND (taxonomy_id:2759) AND (fragment:false) AND (ft_signal_exp:)

API Endpoint:
https://rest.uniprot.org/uniprotkb/search?compressed=true&format=fasta&query=%28%28existence%3A1%29+AND+%28length%3A%5B40+TO+*%5D%29+AND+%28reviewed%3Atrue%29+AND+%28taxonomy_id%3A2759%29+AND+%28fragment%3Afalse%29+AND+%28ft_signal_exp%3A*%29%29&size=500


Negative Protein Set

Number of proteins: 20,615

Selection criteria: Proteins without annotated signal peptides but meeting other quality criteria: existence = 1, length ≥ 40, reviewed, taxonomy ID = 2759, and non-fragmented.(existence:1) AND (length:[40 TO ]) AND (reviewed:true) AND (taxonomy_id:2759) AND (fragment:false) NOT (ft_signal:) AND ((cc_scl_term_exp:SL-0091) OR (cc_scl_term_exp:SL-0191) OR (cc_scl_term_exp:SL-0173) OR (cc_scl_term_exp:SL-0209) OR (cc_scl_term_exp:SL-0204) OR (cc_scl_term_exp:SL-0039))

API Endpoint:
https://rest.uniprot.org/uniprotkb/search?compressed=true&format=fasta&query=%28%28existence%3A1%29+AND+%28length%3A%5B40+TO+*%5D%29+AND+%28reviewed%3Atrue%29+AND+%28taxonomy_id%3A2759%29+AND+%28fragment%3Afalse%29+NOT+%28ft_signal%3A*%29+AND+%28%28cc_scl_term_exp%3ASL-0091%29+OR+%28cc_scl_term_exp%3ASL-0191%29+OR+%28cc_scl_term_exp%3ASL-0173%29+OR+%28cc_scl_term_exp%3ASL-0209%29+OR+%28cc_scl_term_exp%3ASL-0204%29+OR+%28cc_scl_term_exp%3ASL-0039%29%29%29&size=500
Notes: This endpoint also returns results in chunks of 500 and requires pagination.

Project Overview

The repository provides a foundation for protein sequence analysis, useful for tasks such as signal peptide prediction, dataset preparation, or other bioinformatics workflows. All codes are implemented in Python.

Contributors
four
MOHSIN

RAJAB

HASSAN

NADIR

Languages

Python – 100%
