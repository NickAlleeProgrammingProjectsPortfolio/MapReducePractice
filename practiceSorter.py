# this will take in mapped and spit it out as mappedSorted.txt
## used most code from dr.Case's 2sortshuffle.py
unsorted = open("mapped.txt", "r")
sorted = open("mappedSorted.txt", "w")

dataList = unsorted.readlines()
dataList.sort()

for line in dataList:
    sorted.write(line)

unsorted.close()
sorted.close()