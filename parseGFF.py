#! /usr/bin/env python3

import csv
import argparse

#assignment 6
parser = argparse.ArgumentParser(description = "This script parse a gff file and some other things")

parser.add_argument("gff_input", help = "name of the GFF file")
parser.add_argument("fasta_input", help = "name of the fasta file")

args = parser.parse_args()

gene_list = []

with open(args.gff_input, 'r') as gff:
	
	reader=csv.reader(gff, delimiter='\t')
	
	for line in reader:
		if not line:
			continue
		else:
			start = line[3]
			end = line[4]
			print(start, end)
#assignment 5
#for line in open_file:

	#line = line.rstrip('\n')
	
	#name_split = line.split('\t')

	#gene_name = name_split[8].split(';')

	#split_again = gene_name[0].split('Gene')

	#name_only = split_again[1]
	
	#gene_list.append(name_only)

	#order_list = sorted(gene_list)
	
	#print(order_list)

gff.close()


















