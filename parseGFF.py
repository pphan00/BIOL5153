#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO
import re
from collections import defaultdict

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
#assignment 9
	#define dictionary
	genes_with_introns = defaultdict(dict)

	#open and parse argument
	with open(args.gff_input, 'r') as gff:
	
		reader=csv.reader(gff, delimiter='\t')
	
		for line in reader:
			if not line:
				continue
			else:
				organism = line[0].replace(" ", "_")
				start = int(line[3])
				end = int(line[4])
				CDS_feature = line[2]
				strand = line[6]
				attributes = line[8]
#assignment 7
				#test whether this is a CDS feature
				#if CDS_feature == 'CDS':

				#extract the sequence
				feature_seq = genome[start -1: end]

				#reverse complement freature_seq 
				if strand == '-':
					feature_seq = revcomp(feature_seq)

				#extract gene name
				b = re.search("Gene\s+(\S+)\s+", attributes)
				Gene_Name = b.group(1)

				#print(Gene_Name)

				#extract exon number
				a = re.search("exon\s+(\d+)", attributes)

				#test whether there are multiple exons
				if a:
					exon_number = a.group(1)
					#print(Gene_Name, exon_number)

					# dictionary called cds where: key = gene name, value = another dictionary (key : exon numebr, value = sequence of that exon)
					genes_with_introns[Gene_Name][exon_number] = feature_seq

				#single intronless genes evaluated as false and end up here
				#all of these single intronless gene will be printed out in FASTA format as there is no need to store them
				else:
					#print fasta format
					print(">" + organism + "_" + Gene_Name)
					print(feature_seq)

	#loop over genes_with_intron (key = gene name, value = dictionary of exon) dictionary and print the CDS sequence
	print()
	print("now looping over our dictionary")

	for gene_id, whatever in genes_with_introns.items():
		print(">" + organism + "_" + gene_id)

		#loop over all exon for this 1 gene (key = exon number, value = sequence)
		for exon_num, exon_seq in sorted(genes_with_introns[gene_id].items()):
			print(exon_seq, end = '')

		#line break at the end
		print()

					#print(attributes)
					#feature_GC = gc(feature_seq)
					#GCround = round(feature_GC, 2)
					#print(GCround)
def codon2aa(codon):
	codon_dict = {'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'TAA':'O', 'TAC':'Y', 'TAG':'O', 'TAT':'Y', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TGA':'O', 'TGC':'C', 'TGG':'W', 'TGT':'C', 'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F'}

	return(codon_dict.get(codon, '-'))

def revcomp(seq):
	return seq.reverse_complement()

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



















