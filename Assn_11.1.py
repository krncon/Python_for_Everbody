import re
fname = raw_input("Enter file: ")
handle = open(fname)
numlist = list()
for line in handle:
    line = line.rstrip()
    newNumbers = re.findall('[0-9]+',line)
    if len(newNumbers) == 0 : continue
    for num in newNumbers:
        num = int(num)
        numlist.append(num)
count = len(numlist)
total = sum(numlist)
print 'File contains ',count,' values with a sum of ',total
