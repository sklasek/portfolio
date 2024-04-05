# portfolio
A collection of scripts and workflows that folks on the internet might find useful.

## extract-gene-functions.py
I highly recommend [anvio](https://anvio.org/) for pretty much anything related to microbial 'omics.   
Gene functions can be exported from anvio [contigs databases](https://anvio.org/help/main/artifacts/contigs-db/) using the anvio command [anvi-export-functions](https://anvio.org/help/main/programs/anvi-export-functions/).   
[This simple python script](https://github.com/sklasek/portfolio/blob/main/extract-gene-functions.py) exports genes from multiple sources (for example, you may have contigs dbs corresponding to many genomes or MAGs) and binds them into one text file, adding a column corresponding to the source database. Please feel free to copy and modify as necessary. 
