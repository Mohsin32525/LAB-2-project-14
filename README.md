# LAB-2-project-14
This repository contains files and codes of the project for the Laboratory of Bioinformatics 2 course

POSITIVE SET: 2,949 PROTEINS This is the Query of Uniprot search for positive set from graphical interface: (existence:1) AND (length:[40 TO ]) AND (reviewed:true) AND (taxonomy_id:2759) AND (fragment:false) AND (ft_signal_exp:)

API URL using the search endpoint for positive set This endpoint is lighter and returns chunks of 500 at a time and requires pagination.: https://rest.uniprot.org/uniprotkb/search?compressed=true&format=fasta&query=%28%28existence%3A1%29+AND+%28length%3A%5B40+TO+*%5D%29+AND+%28reviewed%3Atrue%29+AND+%28taxonomy_id%3A2759%29+AND+%28fragment%3Afalse%29+AND+%28ft_signal_exp%3A*%29%29&size=500

NEGATIVE SET: 20,615 PROTEINS This is the Query of Uniprot search for negative set from graphical interface: (existence:1) AND (length:[40 TO ]) AND (reviewed:true) AND (taxonomy_id:2759) AND (fragment:false) NOT (ft_signal:) AND ((cc_scl_term_exp:SL-0091) OR (cc_scl_term_exp:SL-0191) OR (cc_scl_term_exp:SL-0173) OR (cc_scl_term_exp:SL-0209) OR (cc_scl_term_exp:SL-0204) OR (cc_scl_term_exp:SL-0039))

API URL using the search endpoint for negative set This endpoint is lighter and returns chunks of 500 at a time and requires pagination. https://rest.uniprot.org/uniprotkb/search?compressed=true&format=fasta&query=%28%28existence%3A1%29+AND+%28length%3A%5B40+TO+*%5D%29+AND+%28reviewed%3Atrue%29+AND+%28taxonomy_id%3A2759%29+AND+%28fragment%3Afalse%29+NOT+%28ft_signal%3A*%29+AND+%28%28cc_scl_term_exp%3ASL-0091%29+OR+%28cc_scl_term_exp%3ASL-0191%29+OR+%28cc_scl_term_exp%3ASL-0173%29+OR+%28cc_scl_term_exp%3ASL-0209%29+OR+%28cc_scl_term_exp%3ASL-0204%29+OR+%28cc_scl_term_exp%3ASL-0039%29%29%29&size=500

About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 0 watching
Forks
 0 forks
Report repository
Releases
No releases published
Packages
No packages published
Contributors
4
@MOHSIN 
@RAJAB
@HASSAN
@NADIR
Languages
Python
100.0%
Footer
