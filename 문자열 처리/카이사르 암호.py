import string
import operator

# letter_count is {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1, 'f': -1, 'g': -1, 'h': -1, 'i': -1, 'j': -1, 'k': -1, 'l': -1, 'm': -1, 'n': -1, 'o': -1, 'p': -1, 'q': -1, 'r': -1, 's': -1, 't': -1, 'u': -1, 'v': -1, 'w': -1, 'x': -1, 'y': -1, 'z': -1}
letter_count = dict((letter, -1) for letter in string.ascii_lowercase); l=[]; rl=[]

l = input(); 
Ceasor_Key = []

for i in letter_count.keys():
    Ceasor_Key.append(i.upper());

for i in l:
    for j in range(len(Ceasor_Key)):
        if Ceasor_Key[j] == i:
            print(Ceasor_Key[j-3], end='');

#1


    


