#create var x as a string that has decimal char, then we define the number
#to send to the decimal char
x = 'There are %d types of people.' % 10

#creating var binary equal to string "binary"
binary = 'binary'
#ditto
do_not = "don't"
#same as line 1, but there are 2 strings inside instead of 1 decimal
y = 'Those who understand %s and those who %s.' % (binary, do_not)

#print out the vars above
print x
print y

#printing a string that has another string inside of it
print 'I said: %r.' % x
print "I also said: '%s'." % y

#create var hilarious and setting it to the boolean value False
hilarious = False
#create var joke_evaluation and setting to string that takes another var
#in raw format
joke_evaluation = "Isn't that joke so funny?! %r"

#print the var joke_evaluation and sending var hilarious to it's %r char
print joke_evaluation % hilarious

#just setting two more variables as simple strings
w = "This is the left side of..."
e = "a string with a right side."

#here's where it gets tricky - printing variables added together
#you can do this because they are both the same format - string
print w + e
