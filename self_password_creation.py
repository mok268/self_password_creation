Name=input("Enter your name here : ")
DOB=input("Enter Your date of birth here :")
gender=input("Enter your gender here : ")
religon=input("Enter your religon here : ")
print(Name)
print(DOB)
print(gender)
print(religon)
print("The password created is : ",Name[0:3]+'_'+Name[-1:-4:-1]+'_'+DOB[-4:]+'_'+gender[-2:-4:-1]+'_'+religon[0:2])