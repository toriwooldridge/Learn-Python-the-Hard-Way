from sys import argv
#open the import module so we can use variables from command line

script, user_name, os = argv
#setting names of variables given on command line

prompt = '> '
#creating a new text variable named prompt with value "> "

print "Hi %s, I'm the %s script." % (user_name, script)
#printing text, inside are two variables, the 2 vars are argv

print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
#creating var likes to accept user input for value

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer with %r operating system. Nice.
""" % (likes, lives, computer, os)
