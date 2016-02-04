fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File cannot be opened',fname
    exit()

conf_values = []

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    else:
        extract_float = float(line.split(':')[1].strip())
        conf_values.append(extract_float)

print "Average spam confidence: " + str(sum(conf_values)/len(conf_values))
