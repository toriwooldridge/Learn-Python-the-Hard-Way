def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #create function that takes two arguments
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket.\n"
    #print esveral statements, enter arg values with decimal format, return

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 30, 5 + 7)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +900)

def my_own_function(*french_toast):
    #create a function that takes one argument
    print "Do you have %d eggs to make %d pieces of french toast?\n" % (french_toast[0] - 2 , french_toast[1])
    #print a statement containing vars from the argument, did some math

eggs  = raw_input("How many eggs?: ")
toast = raw_input("How much toast?: ")
#create vars eggs and toast

my_own_function(int(eggs) + 2 , int(toast))
#call my function, pass eggs and toast vars to it after converting to int
#and do so more math there
