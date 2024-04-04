#!/usr/bin/env python
# coding: utf-8

# In[10]:


from Bio import SeqIO
from Bio.Seq import Seq
import pandas as pd
import sys 

def parse(fasta_file):
    records = SeqIO.parse(fasta_file, "fasta")

    for record in records:
        sequence = record.seq
        genome_length = len(sequence)
        gc_content = (sequence.count("G") + sequence.count("C")) / genome_length * 100
        forward_strand_count = sequence.count("ATG")
        reverse_complement_count = Seq(str(sequence)).reverse_complement().count("ATG")
        return genome_length, gc_content, forward_strand_count, reverse_complement_count


# In[16]:


def main():
    
    fasta_file = "GCA_000287275.1.fasta"
    genome_length, gc_content, forward_strand_count, reverse_complement_count = parse(fasta_file)
    
    data = [[genome_length, gc_content, forward_strand_count, reverse_complement_count]]
    df = pd.DataFrame(data, columns=['Length_of_genome', 'GC_Content', 'ATG_forward', 'ATG_reverse'])

    df.to_csv('ruddi.csv', index=False)
    
if __name__ == "__main__":
    main()


# In[ ]:




