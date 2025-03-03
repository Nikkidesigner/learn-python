User_data = dict(name=["Nikhil","Ajinkya","Aditya","Sumit","Prathamesh"], age=[21,21,22,23,23], talk='talk')
def talk(who,words):
      print(f"I am {who['name'][0]}  and {words}")

u_name=input("Enter your name :")
u_age=int(input("Enter your age : "))
length = len(User_data['name'])
words = ''
def find_user(u_name,u_age):
    flag = 0
    for i in range(length):
        global words
        if u_name==User_data['name'][i] and u_age==User_data['age'][i]:
            flag=1

    if flag==1:
            print(f"{u_name} is present in the database")
            words = input("Enter your words : ")
            talk(User_data,words)
    else:
            print(f"{u_name} is not present in the database")

find_user(u_name,u_age) #method 1

# User_data['talk'](User_data,"hello world") #method 2