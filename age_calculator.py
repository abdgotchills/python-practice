print("Age Calculator!!")
while True:
    enter_date = input("Enter Date(In Digit): ")
    enter_month = input("Enter Month(In Digit): ")
    enter_year = input("Enter Year(In Digit): ")
    print("You're Date of birth is: " + enter_date +
          "/" +enter_month+"/"+enter_year)
    age = str(2026-int(enter_year))
    print("You Will Be " + age + " Years Old in 2026")
    