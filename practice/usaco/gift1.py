'''
ID: tgac2021
LANG: PYTHON3
TASK: gift1
'''
# Input and output
fin = open("gift1.in", "r")
fout = open("gift1.out", "w")

# Read in the file (stripping \n)
lines = [line.strip() for line in fin.readlines()]

# Store NP
NP = int(lines[0])

# Store the friends as a dictionary
friends = dict.fromkeys(lines[1:NP+1], 0)

def gift_giving(friends, gift):
    # the giver
    giver = gift[0]
    
    # the amount, to be divided among (in int)
    amount, divisor = [int(x) for x in gift[1].split()]

    if divisor != 0:
        #  giver keeps reminder, loses amount
        friends[giver] += (amount % divisor) - amount

        # friends get even donation
        donation = int(amount/divisor) 
        for i in range(divisor):
            friends[gift[i + 2]] += donation
    
        # Return where to continue reading in the file
        return divisor + 2 # for reading the giver and gift
    else:
        return 2 # for reading the giver and gift


i = NP+1
while i < len(lines):
    i += gift_giving(friends, lines[i:])

for friend, net_value in friends.items():
    fout.write(f"{friend} {net_value}\n")