#asn01_1
$find $HOME -name "nad.*" -print

#asn01_2
$ps aux|less

#USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
#root         1  0.0  0.0   8892   296 ?        Ssl  19:55   0:00 /init
#root         6  0.0  0.0   8896   204 tty1     Ss   19:55   0:00 /init
#phucphan     7  0.0  0.0  16928  3600 tty1     S    19:55   0:00 -bash
#phucphan    63  0.0  0.0  17380  1920 tty1     R    20:02   0:00 ps aux

#asn01_3
$cd /mnt/c/Users/Dell/Desktop/watermelon_files/; grep 'misc_feature' watermelon.gff; sort -k7g; tee IR_region.gff; less IR_rgff

#asn01_4
$cd /mnt/c/Users/Dell/Desktop/watermelon_files/; grep 'similar to chloroplast IR' watermelon.gff| wc > fragmentcount.gff; grep -v 'similar to chloroplast IR' watermelon.gff| wc >> fragmentcount.gff| less fragmentcount.gff
#There are 141 fragments that are not similar to chloroplast IR DNA while only 3 are similar to chloroplast IR. Therefore , more chloroplast fragments come from outside of IR.

#asn01_5
#! /bin/bash
$cd /mnt/c/Users/Dell/Desktop/watermelon_files/watermelon_nt/; grep 'GGATTC' *.fasta| grep -v 'GAATTC'| tee BamHInotEcoRI.fasta| less BamHI.fasta

#asn01_6
$cd /mnt/c/Users/Dell/Desktop/example_files/; tail -n +500 shaver_etal.csv| head -n 501 > 500.csv| less 500.csv

#asn01_7
$cd /mnt/c/Users/Dell/Desktop/example_files/; sort -k2r fruit.txt| ehad -n 3| sort -k3 > fruit.txt; sort -k2r fruit.txt| tail-n 3| sort -k3 >> fruit2.txt; column fruit2.txt; less fruit2.txt
