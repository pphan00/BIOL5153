#! /usr/bin/env python3

import re

concert = "Katherine went to the concert to see Catheryn and the Cathryn's. She ran into her friend Kathryn, who introduced Katherine to her friend Catherine. Toghether, they enjoyed the concert while texting inaudible snippets to their mutual friend, Kathrin. Their mercurial friend, katharine, felt left out."

pattern = "[k|K|C]ath[a|e]?r[y|i]ne?"

match = re.finditer(pattern, concert)

for y in match:
	result = y.group(0)
	print(result)
	#for x in y:
		#print(x)
	print("Length of match: " + str(len(result)))
	print("First character: " + str(result[0]))
	print("Last character: "+ str(result[-1]))
	match_start = y.start()
	match_end = y.end()
	print("Position of first character is: " + str(match_start))
	print("Position of last character is: " + str(match_end))

















