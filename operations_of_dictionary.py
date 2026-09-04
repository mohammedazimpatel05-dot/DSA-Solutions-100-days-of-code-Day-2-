s = {
    "name": "ABC",
    "age": 24,
    "course": "BCA"
}

print("1, original Dictionary", s)
print("2, name", s["name"])
s["city"] = "balgavi"
print("3, add", s)
del s["city"]
print("4, after deleting", s)
