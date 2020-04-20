#! /usr/bin/env python3

import re

concert = "Katherine went to the concert to see Catheryn and the Cathryn's. She ran into her friend Kathryn, who introduced Katherine to her friend Catherine. Toghether, they enjoyed the concert while texting inaudible snippets to their mutual friend, Kathrin. Their mercurial friend, katharine, felt left out."

match = re.findall("[k|K|C]ath[a|e]?r[y|i]ne?", concert)

if match:
	print(match)
	split = re.split("\s", match)
	print(split[0])
else:
	print("No match")
















