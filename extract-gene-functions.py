#!/users/path/to/conda_environment/environment_name/bin/python3
# set the path to your python version like this

# import libraries to use
import pandas as pd
import os
import glob

os.chdir('/path/to/anvio/gene_functions_txt_files/') # change directory if necessary

# read in source files, which contain gene function calls corresponding to each MAG, genome, or sample (I'm using MAG) 
source_files = sorted(glob.glob('*/gene_functions.txt'))

# for-loop to read in each of the files, add the MAG name as a new column, and append them
# my file names look like this: 'MAG_001/gene_functions.txt', so the MAG name is the first seven characters of the file
dataframes = []
for file in source_files:
   df = pd.read_table(file, delimiter = '\t')
   df['MAG'] = file[0:7]
   dataframes.append(df)

# concatenate the dataframes corresponding to each MAG together
df_all = pd.concat(dataframes)

# write out all the functions as a large text file
df_all.to_csv('all_MAG_functions.txt', sep='\t', index=False, header=True)

# optional: filter the dataframe for certain functions 
# here are two carbohydrate-active enzymes (CAZymes) that are enriched in one set of my  MAGs
df_hits = df_all[df_all.function.str.startswith('GT27') | df_all.function.str.startswith('GH79')]

# write out the filtered list with only these function hits
df_hits.to_csv('growth_assoc_cazyme_functions.txt', sep='\t', index=False, header=True)
