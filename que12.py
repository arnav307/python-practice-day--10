person1={"pranav":986134384,
        "arnav":938384832,
        "kabindra":9374873323}
print("The list of dictionaries: ",person1)
person1.update({"swornim":9384439384})
print("The modified code: ",person1)
del person1["arnav"]
print("After deleting arnav friend: ",person1)
person1["kabindra"]=9775757
print("After changing the value",person1)

key="kabindra"
exists=False
for i in person1:
    if key in person1:
        exists=True

if exists:
    print("yes it exists")
else:
    print("No it doesnt exist")
