print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
#escapes contraction x2 (no \ printed), prints slash, newline, tab

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "----------"
print poem
print "----------"

seven = 12 - 2 + 3 - 6
print "This should be seven: %s" % seven
#setting var five to a math expression with values, order of ops?
#prints value of var five as a string inside explicit string

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 438
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / float(10)

print "We can also do that this way:"
print "We'd have %0.2f beans, %0.2f jars, and %0.2f crates." % secret_formula(start_point)
