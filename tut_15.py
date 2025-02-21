from sys import argv 
script, username = argv
print(f"hello {username} this is python.")
prompt = '>'

print("Do you like python language or java language ? : ")
likes = input(prompt)

print("Do you live in pune of baner ? : ")
live = input(prompt)

print(f"""
        So {username} according to the information given by you , you like {likes} as a programming language.
        You live in {live} so we have our coaching center present there.
""")