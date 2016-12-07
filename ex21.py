def add(a, b):
    print "ADDING %d + %d" % (a, b)
    print a + b
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(20, 7)
height = subtract(68, 4)
weight = multiply(56, 2)
iq = divide(1000, 1)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

def combinedfunctions(a):
    whatform = age + (height - (weight * (iq / a)))
    print whatform

print "That becomes:",what, "\nCan you do it by hand?"
combinedfunctions(2)
