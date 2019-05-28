#List
players = [14,28,16]

print(players)

#Adding two lists
crazyPlayerList = players + [13,78,17]

#Adding stuff to players
players.append(20)
players.insert(1,40)
print(players)

#Slicing of list
print(players[1:2])

#Removing 14 from players
players.remove(14)
players.pop(3)
print(players)

#Clear a list
players[:] = [];
print(players)

#Set
setOfNumber = {1,86,79,36,75,75}
print(setOfNumber)
setOfNames = {"Roger", "Brown","Donald"}
print(setOfNames)

if 'Roger' in setOfNames:
    print("You are there")

#Dictionary
students = {
    1:"Ron",
    2:"Tom",
    3:"Gian",
    4:"Xing Xang Zu"
}
#k - key, v - value
for k,v in students.items():
    print(k,v)
