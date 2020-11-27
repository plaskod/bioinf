#!/usr/bin/env python3

import collections
import requests

webpage = 'http://www.ebi.ac.uk/ena/data/view/'
api='&display=fasta'
links=[f"{webpage}BN{i:0>6}{api}" for i in range(1,5)]

for link in map(requests.get,links):
    if link.status_code >= 300:
        print(f"Failed to open: {file.status_code}")
        continue

    lines=link.iter_lines()
    next(lines)
    neucl_count=collections.defaultdict(int)
    for line in lines:
        for c in line:
            neucl_count[c]+=1

    print("Neuclotides counts: ")
    print(*(f"{chr(neuclotide)} : {count}" for (neuclotide, count) in neucl_count.items()),sep='\n')
