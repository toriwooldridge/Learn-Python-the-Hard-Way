print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating cheesecake. What do you do?"
    print "1. Take the cake."
    print "2. Scream."
    print "3. Stare into the depths of his soul."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear ate your face off. Great work!"
    elif bear == "2":
        print "The bear ate your legs off. Brilliant!"
    elif int(bear) >= 3 and int(bear) <7:
        print """You are wise beyond your years. Bear senses your superiority and bows before you."""
    else:
        print "Well, doing %s is probably better because the bear ran away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Well played!"
    else:
        print "The insanity rots your eyes into a pool a muck. Hurrah!"
else:
    print "You stumble around and fall on a knife and die. Good job, pal!"
