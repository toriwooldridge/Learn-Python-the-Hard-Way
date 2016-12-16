animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

questionlist = ['the animal at 1', 'the third animal',
'the first animal', 'the animal at 3', 'the fifth animal',
'the animal at 2', 'the sixth animal', 'the animal at 4']

answerkey = ['python', 'peacock', 'bear', 'kangaroo', 'whale',
'peacock', 'platypus', 'whale']

print "Use this list to answer the questions: \n", animals, "\n"

b = 0
for answer in answerkey:
    print "What is %s?" % questionlist[b]
    x = raw_input("> ")
    if x in answer:
        print "YES!"
    else:
        print "NO!"
    b += 1
