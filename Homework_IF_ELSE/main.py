year = int(input("Introduceti anul: "))
required_range = year > 1900 and year < 2022

if required_range == 1:
    age = 2022 - year

if age > 0 and age < 4:
    print("baby")
elif age < 10:
    print("kid")
elif age < 16:
    print("teen")
elif age < 19:
    print("young")
elif age < 51:
    print("adult")
else:
    print("old")
