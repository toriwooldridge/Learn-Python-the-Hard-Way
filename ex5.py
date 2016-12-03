name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
#adding string vars within the parenthesis
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# Try to write some variables that convert the inches and pounds
#to centimeters and kilograms.
# Do not just type in the measurements. Work out the math in Python.

def in2cm(x):
    y = x*2.54
    print y

def lbs2kg(x):
    y = x*.45
    print y

in2cm(height)
lbs2kg(weight)
