from sys import argv
#importing a command called exists
from os.path import exists

#unpacking argv
script, from_file, to_file = argv

indata = open(from_file).read()

#in_file = open(from_file, 'r')?
print "The input file is %d bytes long." % len(indata)
print "Does the output file exist? %r" % exists(to_file)
print "Hit RETURN to copy %s to %s, CTRL-C to abort." % (from_file, to_file)
raw_input()

out_file = open(to_file, 'w').write(indata)
print out_file
