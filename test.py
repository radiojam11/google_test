
a= [5,10,15,10,5,2, 5]
"""
a = data.pop(5)
print(data)
print(a)
"""

can = [a.pop(a.index(i, a.index(i)+1)) for i in a if a.count(i) > 1]
print(a)
print(can)
