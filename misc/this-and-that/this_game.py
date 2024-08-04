# You could spend time debugging OR play my game pls

import random as p,os as s;a,r=print('Welcome to my number guessing game'),(500,1)
def i(x):
    while True:
        try: return int(input(x))
        except ValueError: print('Invalid input')
while a!='n':
    n,t,g,v=p.randint(r[1],r[0]),0,i('Guess a number between 1 and 500:\n>'),r[1]
    while g!=n:t+=1;g=i('Your last guess was too high! Try again:\n>')if g>n else i('Your last guess was too low! Try again:\n>')
    a=(input('Well done, you guessed the number in '+str(t)+' attempts\nWould you like to play again? [y]es or [n]o:\n>')).lower()
print('Thanks for playing, have a nice day!')
try:
    with open(s.path.join(s.path.dirname(s.path.abspath(__file__)),'that_game.py'),'r')as file:g=file.read()
    with open(s.path.join(s.path.dirname(s.path.abspath(__file__)),'this_game.py'),'r')as file:t=file.read().count('s')
    n+=1;e=''.join([chr((ord(c)-ord('a'if c.islower()else 'A')+3)%26+ord('a'if c.islower()else 'A'))if c.isalpha()and sum(r)+t==555 else c for c in g]) #dont bother just play my game pls
    with open("that_game.py",'w') as file:file.write(e)
except FileNotFoundError:print("Make sure that_game.py is in the same directory")
except:print(''.join([chr(ord(p)-v) for p in "Zpv!uipvhiu!zpv!dpvme!feju!nz!dpef!ivi@!Usz!bhbjo"]))

# Do not edit this comment pls: iEYsW{io4c_mc_CB3_gRo3u}
