#from sys import argv
#opens module import to read arguments from command line

#script, filename = argv
#unpacks argv and gives variablesin it names

filename = raw_input("file to open?: ")

txt = open(filename)
#creates var "txt" and sets value to a file object
#this is first time we've used open module, it gives you read function

print "Here's your file %r:" % filename
print txt.read()
#print what can be read from txt var (txt is a file object)

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
