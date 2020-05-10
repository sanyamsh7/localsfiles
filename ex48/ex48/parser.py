class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    """this function returns the type of the word in the
        list of tuple of words """
    if word_list:
        word =  word_list[0]
        return word[0]
    else:
        return None
        
def match(word_list, expecting):
    """this function returns the word if the word is of the expecetd
        type of word"""
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    """this returns word of type verb else raises an exception"""
    skip(word_list, 'stop')
    if peek(word_list)=='verb':
        return match(word_list, 'verb')
    else:
        raise ParserError('expected a verb next.')

def parse_object(word_list):
    ''''this returns  the object if it is of type 'direction' and 'noun'.'''
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word =='noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError('expected a noun or directon nex.')

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word =='verb':
        return ('noun', 'player')
    else:
        raise ParserError('expected a verb next.')

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    return Sentence(subj, verb, obj)
    
