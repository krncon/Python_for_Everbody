fname = raw_input('Enter file:')
if len(fname) < 1 : fname = 'mbox-short.txt'
handle = open(fname)

counts = dict()
for line in handle:
    if not line.startswith('From '): continue
    words = line.split()
    name = words[1]
    counts[name] = counts.get(name,0) + 1

topname = None
topcount = None
for name,count in counts.items():
    if topcount is None or count > topcount:
        topname = name
        topcount = count

print topname,topcount
