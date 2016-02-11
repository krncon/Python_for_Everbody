fname = raw_input('Enter file name: ')
fh = open(fname)
lst = list()
for line in fh:
    for i in line.split():
        if i in lst: continue
        lst.append(i)
lst.sort()
print lst
