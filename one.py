#Write a python program using dictionary to get the transverse of dna sequence ?
# input = 'ATGCTTAG'
# output = 'TACGAATC'
# codon = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
# if A:
#     print(dict(A,T))
#     if T:
#         print(dict(T,A))
#         if C:
#             print(dict(C,G))
#             if G:
#                 print(dict(G,C))
# else:
#     print("Out of Sequence")
codon = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

str_input_val = input()

str_output_val = ""

for x in str_input_val:
    str_output_val += codon[x]

print(str_output_val)




