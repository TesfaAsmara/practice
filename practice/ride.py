# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/usaco/chapter1/ride/ride.ipynb.

# %% auto 0
__all__ = ['fin', 'fout', 'comet', 'group', 'translate']

# %% ../nbs/usaco/chapter1/ride/ride.ipynb 3
'''
ID: tgac2021
LANG: PYTHON3
TASK: ride
'''

# Input and output
fin = open("/Users/tesfaasmara/Documents/GitHub/practice/nbs/usaco/1_2/ride/ride.in", "r")
fout = open("/Users/tesfaasmara/Documents/GitHub/practice/nbs/usaco/1_2/ride/ride.out", "w")

# Read in the comet name, in lowercase
comet = fin.readline().lower()

# Read in the group name, in lowercase
group = fin.readline().lower()

# Translation function
def translate(name):
    num = 1
    for letter in name:
        num *= ord(letter) - 96 # ord("a") = 97, so we translate by 96 to start at 1
    return num % 47 

if translate(comet) == translate(group):
    fout.write("GO\n")
else:
    fout.write("STAY\n")
