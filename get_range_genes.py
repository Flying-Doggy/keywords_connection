#!/usr/bin/env python
# encoding: utf-8

import sys

target_gene=sys.argv[1]
bed_file=sys.argv[2]+'.bed'

extension=int(sys.argv[3])


lines=open(bed_file,'r').readlines()

#get the information of the target gene
for i in range(len(lines)):
    temp=lines[i].split('\t')
    if temp[3]==target_gene:
        target_index=i
        target_chr=temp[0]
        target_site=int(temp[1])
        break

result=[]
# search the neighbor genes around the target gene
for i in lines[target_index-500:target_index+500]:
    temp=i.split('\t')
    if temp[0]==target_chr and int(temp[1])>=target_site-extension and int(temp[1])<=target_site+extension:
       result.append(i)
        
outfile_bed=open("266930_col/"+bed_file,'w')
for i in result:
    outfile_bed.write(i)
outfile_bed.close()

#extract the protein sequence of the ranged region
gene_list=[]
outfile_pep=open("266930_col/"+sys.argv[2]+'.pep','w')

for i in result:
    gene_list.append(i.split('\t')[3])

pep_lines=open(sys.argv[2]+'.pep','r').readlines()

#judge whether to write down the records
input_swtich=0
for i in pep_lines:
    if i[0]=='>':
        temp_gene=i.split(' ')[0][1:]
        if temp_gene in gene_list:
            input_swtich=1
        else:
            input_swtich=0
    if input_swtich:
        outfile_pep.write(i)
outfile_pep.close()
