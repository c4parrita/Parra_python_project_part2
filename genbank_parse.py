#!/usr/bin/env python
# coding: utf-8

# In[13]:


from Bio import SeqIO, Entrez 
import pandas as pd
import sys 


def parse(files):
    
    data = []
    
    for file in files:
        with open(file,"r") as handle:
            for record in SeqIO.parse(handle, "genbank"):
                accession = record.id
                features_count = len(record.features)
                source = record.annotations.get('source', '')
                taxonomy = record.annotations.get('taxonomy', [])

                family = taxonomy[-3]
                genus = taxonomy[-2]
                species = taxonomy[-1]

                data.append([accession, family, genus, species, features_count, source])
    return data 


# In[14]:


def main():
    gb_files_input = input().strip().split()

    data = parse(gb_files_input)
    
    df = pd.DataFrame(data, columns=['Accession', 'Family', 'Genus', 'Species', 'Num_Features', 'Source'])
    
    df.to_csv('genbank_parse.csv', index=False)
    
if __name__ == "__main__":
    main()


# In[ ]:




