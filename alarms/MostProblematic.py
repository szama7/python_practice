import ListSorting
from collections import Counter

ListSorting.store_blocks()
computer_units = []
for list in ListSorting.allBlocks:
    computer_units.append(list[1].split()[len(list[1].split()) - 1])

print Counter(computer_units)
