#! /usr/bin/env python3

input = 'watermelon.gff'

open_file = open(input, 'r')

gene_list = []

for line in open_file:

	line = line.rstrip('\n')
	
	name_split = line.split('\t')

	gene_name = name_split[8].split(';')

	split_again = gene_name[0].split('Gene')

	name_only = split_again[1]
	
	gene_list.append(name_only)

	order_list = sorted(gene_list)
	
	print(order_list)

open_file.close()


















