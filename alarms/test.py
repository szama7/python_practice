import ListSorting


list = ["    <HIST> MSS53                  STU-1       SWITCH    2013-07-03  00:07:15.71",
    "* NOTICE STU-1      1A001-07    OL1_SX",
    "(0176) 0154 INTERCEPTION NOTICE",
    "A008 00000000 0000 00000000 00000000"]

print list[1].split()[len(list[1].split())-1]
ListSorting.store_blocks()
ListSorting.sort_list()

