def break_words(stuff):
    '''This function will break up words for us.'''
    words = stuff.split(' ')    #words will be a list
    return words

def sort_words(words):
    '''Sorts the words.'''
    return sorted(words)    #sorted is built-in function

def print_first_word(words):
    '''Prints the first word after popping it off.'''
    word = words.pop(0)     #pop removes item at index and returns it
    print word

def print_last_word(words):
    '''Prints the last word after popping it off.'''
    word = words.pop(-1)    #-1 is default and specifies the last item
    print word

def sort_sentence(sentence):
    '''Takes in a full sentence and returns sorted words.'''
    words = break_words(sentence)   #splits sentence into list of words
    return sort_words(words)    #sorts list of words alphabetically

def print_first_and_last(sentence):
    '''Prints the first and last words of a sentence.'''
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    #nothing returned

def print_first_and_last_word_sorted(sentence):
    '''Sorts the words then prints the first and last one.'''
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
