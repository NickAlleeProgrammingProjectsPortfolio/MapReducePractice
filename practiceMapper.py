## this will take in d.txt and map it to another file named mapped.txt

#dr case wants us to map out the category number and the value
## mapper ideas
## map out store name and payment type
## used most code from dr.Case's 2sortshuffle.py

input = open("purchases.txt", "r")
output = open("mapped.txt", "w")

for line in input:
    datalist = line.strip().split("    ")
    date, time,store, category, value, paymentType = datalist
    output.write(category + "\t" + value + "\n")

input.close()
output.close()
