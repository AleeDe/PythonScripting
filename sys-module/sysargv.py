#sys Module // used to show information or intereact with system and interpreter
import sys
print(sys.version)  #used to view the version of python

#sys.argv has similar function of $# in zsh 
# it show all the arggument in the Script 
# print(sys.argv)

if len(sys.argv) <1:
    print("Usage: python [script-name.py] <arg1> ....")
    sys.exit(1)
i=0
while (i<len(sys.argv)):
    print(f"Argument {i} is {sys.argv[i]}")
    i+=1
    

