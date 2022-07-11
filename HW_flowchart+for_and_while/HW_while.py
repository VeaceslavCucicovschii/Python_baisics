print("Before")
start_n = int(input("start_n = "))
end_n = int(input("end_n = "))

if start_n < end_n:
    while start_n <= end_n:
        print(start_n)
        start_n += 1
else:
    while start_n >= end_n:
        print(start_n)
        start_n -= 1

print("After")
