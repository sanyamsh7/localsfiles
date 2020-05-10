#SCAN() scans the sentence by breaking them into a list of words
#and returning a list of tuples describing the type of each word in sentence.
def scan(stuff):
    lexicons = [["north", "south", "west", "east", "up", "down", "left", "right", "back"],
                ["go", "stop", "kill", "eat"], ['the', 'in', 'of', 'from', 'at', 'it'],
                ["door", "bear", "princess", "cabinet"]]
    result = []
    words = stuff.split()
    for word in words:
        try:
            if word.lower() in lexicons[0]:
                result.append(('direction', word))
            elif word.lower() in lexicons[1]:
                result.append(('verb', word))
            elif word.lower() in lexicons[2]:
                result.append(('stop', word))
            elif word.lower() in lexicons[3]:
                result.append(('noun', word))
            elif convert_number(word) == int(word):
                 result.append(('number', int(word)))
        except ValueError:
            result.append(('error', word))
    return result
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
print(scan("3 91234"))
print(scan("ASDFSDFSASDF"))
print(scan("bear IAS PRINCESS")) 
            
        

