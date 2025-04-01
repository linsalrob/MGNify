# MGNify

Code for working with the MGNIfy API

The MGNify API provides access to a large collection of metagenomic data, including raw sequencing reads, assembled
genomes, and associated metadata. This code provides a simple interface for querying the API and downloading data.

The base URL for the API is [https://www.ebi.ac.uk/metagenomics/api/](https://www.ebi.ac.uk/metagenomics/api/) and
the documentation can be found
at [https://www.ebi.ac.uk/metagenomics/api/docs/](https://www.ebi.ac.uk/metagenomics/api/docs/).


- [Find samples by country][examples/find_samples_by_country.py]

This code queries the MGNify API for samples downloads the associated metadata. It summarises the counts per country
