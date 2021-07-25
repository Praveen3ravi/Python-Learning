input = 'ATGCTTAG'
codon = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
tem=''
print(codon['T'])
for i in input:
    tem+=codon[i]
print(tem)