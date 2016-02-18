fname = raw_input("Enter file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(fname)

counts = dict()
for line in handle:
    if not line.startswith('From '): continue
    words = line.split()
    time = words[5].split(":")
    hour = time[0]
    counts[hour] = counts.get(hour,0) + 1

countsSorted = sorted([(h,c) for h,c in counts.items()])

for h,c in countsSorted:
    print h,c
