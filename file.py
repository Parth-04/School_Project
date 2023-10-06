import mysql.connector as sql
import random
import datetime
import csv

# Connecting to mysql server
mycon = sql.connect(host='localhost', user='root', passwd='computerpass123', database='jee_reg')

if mycon.is_connected():
    print("Connected Successfully! ")
else:
    print("Server Connection Error!")

# Creating cursor to execute queries
cur = mycon.cursor()

# Creating a table to contain candidate log-in information
cur.execute("CREATE TABLE IF NOT EXISTS login_info (Username varchar(20) Primary Key, Password varchar(20))")
mycon.commit()
# Login:
print("Welcome! ")
print("Choose one of the following options :"'\n'
      "1. To register enter (1)"'\n'
      "2. To login enter (2)"'\n'
      "3. Quit")

b = True
while b:
    ch = int(input("Enter you choice - "))
    if ch == 1:
        user_name = input("Enter username - ")
        passwd = input("Enter password ")
        q1 = 'select * from login_info'
        cur.execute(q1)
        inf = cur.fetchall()
        mycon.commit()
        login_list = []
        for j in inf:
            for i in j:
                login_list.append(i)
        # To check if username - password combination already exists in the reg_infobase
        if user_name in login_list:
            print("Username already exists. Please use a different username! ")
        else:
            val = (user_name, passwd)
            cur.execute("insert into login_info (Username, Password) values(%s,%s)", (user_name, passwd))
            mycon.commit()
            print("Account registered successfully !")

    elif ch == 2:
        usern = input("Enter your username - ")
        passw = input("Enter your password - ")
        q2 = 'select * from login_info'
        cur.execute(q2)
        dat = cur.fetchall()
        mycon.commit()
        if (usern, passw) in dat:
            print("Login successfull ! ")
            a = True
            break
        else:
            print("Entered username and password combination is incorrect please try again ! ")
            a = False
        print(dat)

    elif ch == 3:
        print("Quitting ! ")
        break
    else:
        print("Please enter a valid input! ")

mycon.commit()

cur.execute("CREATE TABLE IF NOT EXISTS reg_details (Reg_no int Primary Key, Name varchar(50), Gender varchar(2), Dob date, Name_father varchar(50), Name_mother varchar(50), Add1 varchar(50), Add2 varchar(50), State varchar(15), District varchar(15), pin int, mobile varchar(15), email_id varchar(50), aadhar_no varchar(25), quali varchar(25), marks_l1 int)")

# Registration:
while a:
    print("Choose one of the following options : "'\n'
          "1. To register for the exam (1)"'\n'
          "2. To view exam details (2)"'\n'
          "3. To enter Level - 1 Marks (3)"'\n'
          "4. To check eligibility for Level - 2 (4)"'\n'
          "5. Quit (5)"'\n')

    choice = int(input("Enter choice : "))

    if choice == 1:
        print("Enter the following details : ")
        reg_no = random.randrange(10000000, 100000000)
        name = input("Enter your name - ")
        gender = input("Enter your gender (M/F) - ")
        DOB = input("Enter your Date of Birth (YYYY-MM-DD) - ")
        name_father = input("Enter your father's name - ")
        name_mother = input("Enter your mother's name - ")
        add_1 = input("Enter address line 1 - ")
        add_2 = input("Enter address line 2 - ")
        state = input("Enter your state - ")
        district = input("Enter your district - ")
        pin = input("Enter your local pin code - ")
        mob = input("Enter your mobile number ")
        email = input("Enter your email id - ")
        aadhar = input("Enter your aadhar card number ")
        qual = input("Enter your academic qualification - ")
        cur.execute("insert into reg_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            reg_no, name, gender, DOB, name_father, name_mother, add_1, add_2, state, district, pin, mob, email, aadhar, qual, 0))
        print('\n''\n')
        print('Your registration number is - ', reg_no)
        print("Please note your registration number ")
        print('\n''\n')
        mycon.commit()

    elif choice == 2:
        cur = mycon.cursor()
        reg_no = int(input("Enter your registration number - "))
        cur.execute("select * from reg_details where reg_no = {}".format(reg_no))
        reg_info = cur.fetchall()
        reg_info = list(reg_info[0])
        print("Registration number  = ", reg_info[0])
        print("Candidates Name = ", reg_info[1])
        print("Gender = ", reg_info[2])
        print("Date of Birth = ", reg_info[3])
        print("Father's Name = ", reg_info[4])
        print("Mother's Name = ", reg_info[5])
        print("Address Line 1 = ", reg_info[6])
        print("Address Line 2 = ", reg_info[7])
        print("State = ", reg_info[8])
        print("District = ", reg_info[9])
        print("Pin Code = ", reg_info[10])
        print("Mobile Number = ", reg_info[11])   
        print("Email Address = ", reg_info[12])
        print("Aadhar Card Number = ", reg_info[13])
        print("Academic qualification = ", reg_info[14])
        print("\n")
        mycon.commit()

    elif choice == 3:
        reg_no = int(input("Enter your registration number - "))
        m1 = int(input("Enter your marks for Level-1 - "))
        cur.execute("update reg_details set marks_l1 = {} where Reg_no = {}".format(m1, reg_no))
        mycon.commit()
        print("Marks updated successfully")

    elif choice == 4:
        cur.execute("select avg(marks_l1) from reg_details")
        m = cur.fetchall()
        for i in m:
            for j in i:
                marks_avg = int(j)

        reg_no = int(input("Enter your registration number - "))
        cur.execute("select marks_l1 from reg_details where Reg_no = {}".format(reg_no))
        l = cur.fetchall()
        for i in l:
            for j in i:
                marks = int(j)

        if marks >= marks_avg:
            print("You are eligible for round 2 !")
        else:
            print("Sorry, you are not eligible for round 2!")
        print("The average marks are ", marks_avg)

    elif choice == 5:
        print("Quitting")
        break

    else:
        print("Please enter a valid input")