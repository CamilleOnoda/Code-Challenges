"""
Everything Be True
Check if the predicate (second argument) is truthy on all elements of a collection (first argument).

In other words, you are given an array collection of objects. The predicate pre 
will be an object property and you need to return true if its value is truthy. 
Otherwise, return false.

Remember, you can access object properties through either dot notation or [] notation."""

def truthCheck(collection, pre):
  for object in collection:
    if not object.get(pre):
       return False
  return True

result = truthCheck([{"name": "Quincy", "username": "QuincyLarson"}, {"name": "Naomi", "username": "nhcarrigan"}, {"name": "Camperbot"}], "username")
print(result)