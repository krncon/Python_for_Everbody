fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File cannot be opened',fname
    exit()
for line in fh:
    line = line.rstrip()
    print line.upper()
    
