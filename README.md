# Python Dictionary Operations

This repository contains basic operations performed on Python dictionaries, including creation, accessing elements, adding new key-value pairs, and deleting elements.

---

## Code Breakdown

```python
# 1. Creating a Dictionary
s = {
    "name": "ABC",
    "age": 24,
    "course": "BCA"
}

# 2. Accessing Elements
print("1, original Dictionary", s)
print("2, name", s["name"])

# 3. Adding a New Key-Value Pair
s["city"] = "balgavi"
print("3, add", s)

# 4. Deleting a Key-Value Pair
del s["city"]
print("4, after deleting", s)
#output
1, original Dictionary {'name': 'ABC', 'age': 24, 'course': 'BCA'}
2, name ABC
3, add {'name': 'ABC', 'age': 24, 'course': 'BCA', 'city': 'balgavi'}
4, after deleting {'name': 'ABC', 'age': 24, 'course': 'BCA'}
