marks = {
    "Ayushi" : 91,
    "Priyanshi" : 80,
    "Palak" : 35,
    "List" : [91,80,35],
    
}
print( type(marks))
# used for associating key values to the list
print(marks["Ayushi"]) #if key word does not exist in dict it shall give error

# unordered , mutable, indexed, can't contain dublicate keys

print(marks.items()) #gives key paired items in tuples
print(marks.keys()) #gives the keys
marks.update({"Ayushi" : 100 })
print(marks)
print(marks.get("Ayushi")) #if key word does not exist it will show none
print(marks.clear()) #it clears the list 
print(marks.pop)


d = {} # d is an empty dictionary