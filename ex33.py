i = 0
numbers = []

def whilefunction(a):
    global i
    """the i in line 9 is local with no assignment, I'm choosing to set
    this local i to the global i by pulling the global i into the local scope"""
    while i < a:
        print "i starts at: %d" % i
        numbers.append(i)
        #appending i to numbers list, so first iteration numbers = [0]
        i += 1
        #increment i by 1 each iteration of while loop
        print "i is now: %d \n\n" % i

largestnumber = raw_input("Largest number you want in the list?: ")
whilefunction(int(largestnumber) + 1)

print "Numbers in the list: "
for num in numbers:
    """for loops by definition iterate over a list, so even though num seems
    undefined, it sets to the first value in the list"""
    print num

print "The full list: ", numbers
