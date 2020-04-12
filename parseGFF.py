#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

#assignment 6

def gc(sequence):
#calculate GC content:

	count_G = sequence.count('G')
	count_C = sequence.count('C')
	return(count_G +count_C)/len(sequence)

def get_args():
	parser = argparse.ArgumentParser(description = "This script parse a gff file and some other things")

	parser.add_argument("gff_input", help = "name of the GFF file")
	parser.add_argument("fasta_input", help = "name of the fasta file")

	return parser.parse_args()

def parse_fasta():
	return SeqIO.read(args.fasta_input, 'fasta')


def parse_gff(genome):
	with open(args.gff_input, 'r') as gff:
	
		reader=csv.reader(gff, delimiter='\t')
	
		for line in reader:
			if not line:
				continue
			else:
				start = int(line[3])
				end = int(line[4])
				CDS_feature = line[2]
				strand = line[6]
				attributes = line[8]
#assignment 7
				#test whether this is a CDS feature
				if CDS_feature == 'CDS':

					#extract the sequence
					feature_seq = genome[start -1: end]
					print(attributes)
					print(feature_seq)
					feature_GC = gc(feature_seq)
					GCround = round(feature_GC, 2)
					print(GCround)

def main(): #call all previous funtions to cascade down
	genome_sequence = parse_fasta()
	parse_gff(genome_sequence.seq)
#get command-line arguments before calling main():
args = get_args()

#execute the program by calling main (entire script is now a function)
if __name__ == "__main__":
	main()

#assignment 5
#gene_list =[]
#for line in open_file:

	#line = line.rstrip('\n')
	
	#name_split = line.split('\t')

	#gene_name = name_split[8].split(';')

	#split_again = gene_name[0].split('Gene')

	#name_only = split_again[1]
	
	#gene_list.append(name_only)

	#order_list = sorted(gene_list)
	
	#print(order_list)



















