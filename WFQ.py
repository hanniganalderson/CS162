#CS162 WFQ Week 3
#Create 3 different kinds of queues
premium = []
standard = []
economy = []

# Input packets, pasted from .py file
input_packets = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen",
                 "E Mike", "E Joe", "P Dee", "E Vicky", "E George",
                 "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
                 "P Dee", "S Bill", "S Chase", "E Price", "P Dee",
                 "E Sue"]
#For loop to split packet and get rank based on first letter
for packet in input_packets:
    #split packet
    piece = packet.split()
    #rank determined by first letter
    rank = piece[0]
#If elif statements to append rank to packet
    if rank == "P":
        premium.append(packet)
    elif rank == "S":
        standard.append(packet)
    elif rank == "E":
        economy.append(packet)

#while loop to dequeue packets in order
while premium or standard or economy:
#3 for premium
    for i in range(3):
        if premium:
            print(premium.pop(0))

#2 for standard
    for i in range(2):
        if standard:
            print(standard.pop(0))

#1 for economy
    for i in range(1):
        if economy:
            print(economy.pop(0))
