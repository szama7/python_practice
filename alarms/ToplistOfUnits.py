import ListSorting
from collections import Counter

ListSorting.store_blocks()
ListSorting.sort_list()
computer_units = []

for i in range(0, len(ListSorting.threestar)):
    computer_units.append(ListSorting.threestar[i][0].split()[2])

for i in range(0, len(ListSorting.twostar)):
    computer_units.append(ListSorting.twostar[i][0].split()[2])

print Counter(computer_units)