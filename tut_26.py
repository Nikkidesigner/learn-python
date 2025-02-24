from dis import dis

cars =10
people = 20
code = """
if cars > people:
     print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
     print("We can't decide.")
"""
dis(code)