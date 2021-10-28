import array
Names_Our_Group=[
["Yaseen"],
["Ban"],
["Teba"],
["Baqer"],
["Mohammed"],
]

print("All The Names: ")
print(Names_Our_Group)

#Insertion
Names_Our_Group.insert(5,["Kareem"])
print('\n'"The Names After Insertion: ")
print(Names_Our_Group)

#Deletion
del Names_Our_Group[2]
print('\n'"The Names After Delete An Name: ")
print(Names_Our_Group)

#Search
searching = Names_Our_Group[1]
print('\n'"Result Of Searching: ")
print(searching)


#Update
Names_Our_Group[0]=["Yasso"]
print('\n'"The Names After Updating: ")
print(Names_Our_Group)
