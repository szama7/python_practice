f = open('alarms.log', 'r')
allBlocks = []
singleBlock = []
temp = []
threestar = []
twostar = []
onestar = []
notice = []
distur = []

def store_blocks():
    for line in f:
        temp.append(line)
    for i in range(len(temp)):
        if temp[i][5:9] == "HIST":
            singleBlock.extend((temp[i], temp[i + 1], temp[i + 2], temp[i + 3]))
            allBlocks.append(singleBlock)
        singleBlock = []
    return allBlocks


def sort_list():
    for i in allBlocks:
        if "*** ALARM" in i[1]:
            threestar.append(i)
        elif "**  ALARM" in i[1]:
            twostar.append(i)
        elif "*   ALARM" in i[1]:
            onestar.append(i)
        elif "NOTICE" in i[1]:
            notice.append(i)
        elif "DISTUR" in i[1]:
            distur.append(i)

def append_lists():
    return threestar + twostar + onestar + notice + distur

if __name__ == '__main__':
    store_blocks()
    sort_list()
    print(len(append_lists()))
