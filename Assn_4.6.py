def computepay(h,r):
    if h > 40:
        return 40*r + (h -40)*1.5*r
    else:
        return h*r

h = float(raw_input("Enter Hours: "))
r = float(raw_input("Enter Rate per Hour: "))
print computepay(h,r)