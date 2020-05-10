#IMPLEMENTING UNIQ COMMAND OF UNIX

import sys
#!/usr/bin/env python3.6

def uniq(file):
    lines = set()
    with open(file) as f:
        lines |= set(f.readlines())
        print(lines)




script, file_name = sys.argv
uniq(file_name)
