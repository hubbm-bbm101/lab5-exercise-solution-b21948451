e_mail = input("Enter your e mail==")
et = False
dot = False
checker = False
for i in e_mail:
    if i == "@":
        et = True
    if i == ".":
        dot = True
if et and dot == True:
    checker = True
print("Your e mail is" , checker)