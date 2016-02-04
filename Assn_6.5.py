text = "X-DSPAM-Confidence:    0.8475"
colonpos = text.find(':')
text2 = text[colonpos+1:]
num = float(text2)
print num
