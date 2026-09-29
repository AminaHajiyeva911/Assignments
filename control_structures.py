#Grading_System
exam_mark=int(input("input your exam mark: "))
if exam_mark >=90 :
    grade='A'
elif exam_mark >=75 and exam_mark <=89 :
    grade='B'
elif exam_mark >=50 and exam_mark <=74 :
    grade='C'
else:
    grade='F'
print(f'User grade is {grade}')

#Multiplication_Table
number=int(input("input your number: "))
i=1
while i<11 :
    print(f'{number}*{i}={number*i}')
    i+=1

#Password_Retry_System
correct_password=input("input correct password: ")
max_lim=1
while True:
    if max_lim <=3:
        password=input("input password: ")
        if password==correct_password:
            print("It is correct password")
            break
    else:
        print("No attempts remaining")
        break
    max_lim+=1
