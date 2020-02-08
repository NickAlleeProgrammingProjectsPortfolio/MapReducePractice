# this will take in mappedSorted.txt and reduce it into a file named mappedAndReduced.txt

## possible reduce ideas
## for each store, find the most used payment type
### i think this will require our data to be sorted.

## used most code from dr.Case's 2sortshuffle.py
startingF = open("02.txt","r")
outF = open("r.txt", "w")

thisCategory = ""
totaler = 0.0

for line in startingF:
    line = line.strip().split('\t')
    category, value = line
    if (category != ""):
        if category != thisCategory:
            outF.write(thisCategory + '    ' + str(totaler))

            thisCategory = category
            totaler = 0.0
    totaler += value

outF.write(thisCategory + '    ' + str(totaler))

startingF.close()
outF.close()