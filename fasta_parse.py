#!/usr/bin/env python
# coding: utf-8

# In[11]:


from Bio import SeqIO, Entrez 
import pandas as pd
import sys 


def parse(files):
    data = []
    
    for file in files:
        with open(file,"r") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                fasta_id = record.id
                sequence = str(record.seq)
                first_10_aa = sequence[:10]
                length = len(sequence)
                num_c = sequence.count("C")

                data.append([fasta_id, first_10_aa, length, num_c])
    return data


# In[13]:


def main():
    
    fasta_file_input = input().strip().split()
    data = parse(fasta_file_input)
    
    df = pd.DataFrame(data, columns=['ID', 'First_10_AA', 'Length', 'Number_C'])
    df.to_csv('protein_info.csv', index=False)
    
if __name__ == "__main__":
    main()                                 
                                    


# In[ ]:





# In[ ]:




