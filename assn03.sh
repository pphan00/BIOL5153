#assn03

#assn03_01 
#! /bin/bash
for x in {808..8008}; do
echo "TR-$x"
done

#assn03_02
#! /bin/bash
alias c='clear'
alias e='exit'
alias ls='ls -al'
done

#assn03_03
ls -dq *.fasta*| wc -l
#15085

#assn03_04
ls -dq *.tre*| wc -l
#14640

#assn03_05
ls -dq *.sched*| wc -l
#15262

#assn03_06
#445
#difference between 03 and 04

#assn03_07
grep 'Program Return Code:' *.sched > assn03_07.md| sort -u| wc -l; grep 'Program Retrun Code: 0' assn03_07.md | sort -u| wc -l; grep -v 'Program Return COde: 0' assn03_07.md | sort -u| wc -l
#15261 total number of *.sched files with string 'Program Return Code' 
#15217 total number of *.sched files with string 'Program Return Code:0'
#44 total number of *sched file without string 'Program Return Code: 0'

#assn03_08
#All FASTA files without a corresponding tree is pooled together in a different folder 'no tree'
#! /bin/bash
for x in *.fasta; do
write_raxml_job_script.py $x > $x.pbs
done
