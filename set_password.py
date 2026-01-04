print("Welcome To Password selector. You're new password must begin with "
      "only one Capital Order "
      "\nand have at least one numerical digit and lowercase order")
while True:
        password = input("Enter New Password: ")
        if len(password)==0:
            print("Your Password Is Empty")
            continue
        elif password.isalpha():
            print("Password Must Have At Least One Numerical No.")
        elif password.isdecimal():
            print("Password Must Have At Least One Alphabet")
        elif password.isupper():
            print("Password Must Have One Lower Case Order")
        elif password.islower():
            print("Password Must Have Begin With Upper Case Order")
        elif password.istitle():
            break
print("Password Updated Successfully \nLength of your password is " + str(len(password)))

