for i in range(2):
    roll_num = int(input("Enter Your Roll Number  "))
    Name = str(input("Enter Your Name  "))
    Age = int(input("Enter Your Age  "))
    Marks = int(input("Enter Your Marks  "))

if Marks > 100:
    print("Please Enter Marks Below 100")
    Marks = int(input("Enter Your Marks  "))
    pass
else:
    print('Roll Number', 'Name', 'Age', 'Marks')
    Data = [roll_num, Name, Age, Marks]
    for i in Data:
        print(Data)
    pass
pass