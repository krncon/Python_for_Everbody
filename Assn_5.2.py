largest = None
smallest = None
while True:
    entry = raw_input('Enter a Number: ')
    if entry == 'done':
        break
    else:
        try:
            num = int(entry)
        except:
            print "Invalid input"
            continue
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
print "Maximum is",largest
print "Minimum is",smallest



