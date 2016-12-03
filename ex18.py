#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    #function named "print_two", takes "args" (2 values) as input
    #unpacks args and renames each value, must have 2 values
    #print arg1 and arg2 on one line in raw format

#whats up with the *? combines everything you give it into a list

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    #given arg1 and arg2 up front, less code

#this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this takes no arguments
def print_none():
    print "I got nothin'."

print_two("Tori", "Wooldridge")
print_two_again("Tori", "Wooldridge")
print_one("First!")
print_none()
