names = ["Aman", "Rahul", "Avni", "Avantika", "Riya", "Biti"]

result = list(filter(lambda name: name.startswith("A"), names))

print(result)


#  using list comprehension

names = ["Aman", "Rahul", "Avni", "Avantika", "Riya", "Biti"]

result = [name for name in names if name.startswith("A")]

print(result)


# using loops

names = ["Aman", "Rahul", "Avni", "Avantika", "Riya", "Biti"]
result = []

for name in names:
    if name[0] =="A":
        result.append(name)

print(result)     