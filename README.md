# portfolio
A collection of scripts and workflows that folks on the internet might find useful.

## anvio accessory functions
I highly recommend [anvio](https://anvio.org/) for pretty much anything related to microbial 'omics.   

### extract-gene-functions.py
Gene functions can be exported from anvio [contigs databases](https://anvio.org/help/main/artifacts/contigs-db/) using the anvio command [anvi-export-functions](https://anvio.org/help/main/programs/anvi-export-functions/).   
Maybe you have many contigs dbs (each corresponding to genomes or MAGs) that you want to export gene functions from. [This simple python script](https://github.com/sklasek/portfolio/blob/main/extract-gene-functions.py) exports genes from multiple sources and binds them into one text file, adding a column corresponding to the source database. 

### import-whokaryote-gene-calls-to-anvio.py
[Whokaryote](https://github.com/LottePronk/whokaryote) is a tool for classifying contigs by domain of origin (eukaryotic vs prokaryotic). 
By default, it will perform gene calling on contigs using [Prodigal](https://github.com/hyattpd/Prodigal). 
Anvio users with samples containing both bacteria/archaea and eukaryotes may choose to run this step before generating a contigs database, but there's no need to rerun prokaryotic gene calling again. [import-whokaryote-gene-calls-to-anvio.py](https://github.com/sklasek/portfolio/blob/main/import-whokaryote-gene-calls-to-anvio.py) reformats the file output by whokaryote (called contigs_genes.gff) into an [external_gene_calls.txt](https://anvio.org/help/8/artifacts/external-gene-calls/) that can be imported into an anvio contigs database. 
This might work with other .gff output formats but I haven't tested it extensively. 
Additional functionality could also use the contigs_proteins.faa output file so anvi-gen-contigs-db doesn't need to bother with translating.   
