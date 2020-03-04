#!/usr/env python3
input = "dna.txt"
inputfile = open(input, "r")
dna_sequence = inputfile.read().lower()
print(dna_sequence)
a_count = dna_sequence.count("a")
g_count = dna_sequence.count("g")
t_count = dna_sequence.count("t")
c_count = dna_sequence.count("c")
total_length = len(dna_sequence)
aper = a_count/total_length*100
tper = t_count/total_length*100
cper = c_count/total_length*100
gper = g_count/total_length*100
print("Percent A : " + str(aper) + "%")
print("Percent T : " + str(tper) + "%")
print("Percent G : " + str(gper) + "%")
print("Percent C : " + str(cper) + "%")
inputfile.close()
