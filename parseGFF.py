#! /usr/bin/env python3

my_file = "watermelon.gff"
open_file = open(my_file)
read_file = open_file.read().rstrip('\n')

if "similar" != read_file:
	split_word = read_file.split()
	remove_word = ['atpB-rbcL','ndhC-trnV','trnG-trfM','trnfM-rps14','trnL-trnL','trnM','psbM-trnD','trnT-psbD', 'rps12-trnV','petG-trnW','trnW','trnP', 'psbC', 'psbD','trnD', 'trnC', 'rpoB-trnC', 'rpoB', 'rpl32-trnL','trnH-psbA','tRNH','trnI(TAT)','with','rRNA','mRNA', 'repeat','codon,','codon"','region', 'terminus', 'predicted', 'editing', 'gene,','loop','repeat_region','codon', 'start', 'stop', 'subunit', 'possibly', 'of', 'not', 'gene', 'for', 'IR', 'ID', 'PubMed', 'C', 'DNA,', 'editting', 'gene', 'generation', 'inverted','(SSC)','RNA','type', 'within', 'tRNA', 'chloroplast-like', 'to', 'spacer', 'similar', 'see', 'misc_feature', 'intron', 'exon', 'larger', 'intact', 'green', 'grey47', 'functional', 'from', 'fragment', 'expanded', 'editting', 'embedded', 'creates', 'determined', 'codon', 'cis-spliced','GenBank', 'chloroplast', ';','Gene', 'Citrullus', 'lanatus', 'COLOR', 'blue', 'red', 'black', 'CDS', '+', '-', '.', 'LSC', 'Note', 'DNA', 'U', 'anticodon', '(LSC)', '/']
	remove_total = remove_word
	split_word.sort()
	x = [u for u in split_word if u not in remove_total]
	del x[0:488]
	print(x)


open_file.close()
