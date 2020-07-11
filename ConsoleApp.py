'Create a console application for an IT Academy with the following features:'
'1. The academy program should have a fixed course of study.'
'2. If a new student is interested in the academy program the student can inquiry about the course of study.'
'3. Student Registration with Rs 20000(deposit). Students are allowed to pay in two installments with Rs 10000 each.'
'4. Display all the students information from the academy with their payments and remaining payments.'
'5. Update the student information if needed.'
'6. Delete the student information he/she left the program.'
'7. Return the deposit amount(Rs 20000) to the students,'
'after the successful completion of the course and check the balance.'

import csv
import os
import pickle

'class of studentdata with object'
class studata(object):
    def __init__(s):
        s.admno = 0
        s.name = ""
        s.address = ""
        s.contact = ""
        s.email = ""
        s.dob = ""

    'function to get data from user'
    def create_studata(s):
        s.admno = int(input("Enter admission number: "))
        name =  input("Enter student complete name: ")
        s.name = name.upper()
        address = input("Enter your address: ")
        s.address = address.upper()
        s.contact = input("Enter your mobile number: ")
        s.email = input("Enter your email id: ")
        s.dob = input("Enter date of birth: ")

    'function to show data on screen'
    def show_studata(s):
        print("Admission No.: ", s.admno)
        print("Student Complete Name: ", s.name)
        print("Address: ", s.address)
        print("Contact: ", s.contact)
        print("Email ID: ", s.email)
        print("Date of Birth: ", s.dob)

    'function to get new data from user'
    def modify(s):
        print("Admission No.: ", s.admno)
        name = input("Enter student complete name: ")
        s.name = name.upper()
        address = input("Enter your address: ")
        s.address = address.upper()
        s.contact = input("Enter your mobile number: ")
        s.email = input("Enter your email id: ")
        dob = input("Enter date of birth: ")

    'function to show data in tabular format'
    def report(s):
        print("%-15s" % s.admno, "%-20s" % s.name.strip(), "%-20s" % s.address,
              "%-20s" % s.contact, "%-20s" % s.email, "%-20s" % s.dob)


    def retadmno(s):
        return s.admno

    def retcontact(s):
        return s.contact

    def retname(s):
        return s.name

    def retaddress(s):
        return s.address

    def retdob(s):
        return s.dob

    def retemail(s):
        return s.email


'class of feedata with object'
class feedata(object):
    def __init__(s):
        s.trno = 0
        s.admno = 0
        s.name = ""
        s.fmonth = ""
        s.famnt = 0
        s.fremaining = 0
        s.date = ""

    'function to get data from user'
    def getFeeData(s):
        flag = 0
        try:
            inFile = open("student.dat", "rb")
            n = int(input("Enter the Admission number: "))
            while True:
                stu = pickle.load(inFile)
                if stu.retadmno() == n:
                    s.trno = int(input("Enter a transaction number: "))
                    s.admno = n
                    s.name = stu.name
                    fm = input("Enter the fee quarter: ")
                    s.fmonth = fm.upper()
                    s.famnt = int(input("Enter the fee of student: "))
                    if s.famnt == 20000:
                        print("Student paid complete fees.")
                    elif s.famnt < 20000 or s.famnt == 10000:
                         print("Students are allowed to pay in two installments with Rs 10000 each.")
                    else:
                        print("No Admission.")
                    s.fremaining = int(input("Enter the remaining payment: "))
                    s.date = input("Enter the fee date: ")
                    flag = 1
        except EOFError:
            inFile.close()
            if flag == 0:
                print("Admission number not exist ")
            return flag
        except IOError:
            print(" studata.dat : File could not be open !! Press any Key...")
        return flag

    'function to show data from user'
    def show_feedata(s):
        print("Transaction number: ", s.trno)
        print("Admission No.: ", s.admno)
        print("Student Complete Name: ", s.name)
        print("Fee Quarter: ", s.fmonth)
        print("Fee Amount: ", s.famnt)
        print("Fee Remaining: ", s.fremaining)
        print("Fee Date: ", s.date)

    'function to modify data from user'
    def modify(s):
        print("Transaction number: ", s.trno)
        s.admno = int(input("Enter admission  number: "))
        name = input("Enter student complete name: ")
        s.name = name.upper()
        fm = input("Enter the fee quarter: ")
        s.fmonth = fm.upper()
        s.famnt = int(input("Enter the fee of the student: "))
        s.fremaining = int(input("Enter the remaining fee to submit: "))
        s.date = input("Enter the fee date: ")

    'function to show data in tabular format'
    def report(s):
        print("%-10s" % s.trno, "%-20s" % s.name, "%-10s" % s.fmonth, "%-9s" % s.famnt,
              "%-10s" % s.fremaining)

    def rettrno(s):
        return s.trno

    def retadmno(s):
        return s.admno

    def retname(s):
        return s.name

    def retfmonth(s):
        return s.fmonth

    def retfamnt(s):
        return s.famnt

    def retfremaining(s):
        return s.fremaining

    def retdate(s):
        return s.date


'function for converting the user data into binary inside a (.dat) file'
def write_studata():
    try:
        st = studata()
        outFile = open("student.dat", "ab")
        st.create_studata()
        pickle.dump(st, outFile)
        outFile.close()
        print("Student details added Successfully")
        print("YOUR ADMISSION NUMBER IS: ", st.retadmno())
    except:
        pass

'function for converting the user data into binary inside a (.dat) file.'
def write_feedata():
    try:
        fe = feedata()
        outFile = open("feedata.dat", "ab")
        flag = fe.getFeeData()
        if flag == 1:
            pickle.dump(fe, outFile)
            print("FEE DATA CREATED SUCCESSFULLY")
            print("YOUR TRANSACTION NUMBER IS: ", fe.rettrno())
        outFile.close()

    except:
        pass



'function to display student details given by the user and retrieve from a (.dat) file'
def display_studata(n):
    flag = 0
    try:
        inFile = open("student.dat", "rb")
        print("STUDENT DETAILS")
        while True:
            st = pickle.load(inFile)
            if st.retadmno() == n:
                st.show_studata()
                flag = 1
    except EOFError:
        inFile.close()
        if flag == 0:
            print("student data not exist ")
    except IOError:
        print("File could not be open !! Press any Key...")



'function to display fee details given by the user and retrieve from a (.dat) file'
def display_feedata(n):
    flag = 0
    try:
        inFile = open("feedata.dat", "rb")
        print("\n")
        print("FEE DETAILS")
        while True:
            fe = pickle.load(inFile)
            if fe.rettrno() == n:
                fe.show_feedata()
                flag = 1
    except EOFError:
        inFile.close
        if flag == 0:
            print("THIS TRANSACTION NUMBER DOES NOT EXIST")
    except IOError:
        print("File could not be open !! Press any Key...")


'function to modify the student record'
def modify_studata(n):
    found = 0
    try:
        inFile = open("student.dat", "rb")
        outFile = open("temp.dat", "wb")
        while True:
            st = pickle.load(inFile)
            if st.retadmno() == n:
                st.show_studata()
                print("Enter The New Details of Account")
                st.modify()
                pickle.dump(st, outFile)
                print("Record Updated")
                found = 1
            else:
                pickle.dump(st, outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found == 0:
            print("Record Not Found ")

    except IOError:
        print("File could not be open !! Press any Key...")

    os.remove("student.dat")
    os.rename("temp.dat", "student.dat")


'function to modify the fee details of a student'
def modify_feedata(n):
    found = 0
    try:
        inFile = open("feedata.dat", "rb")
        outFile = open("temp.dat", "ab")
        while True:
            fe = pickle.load(inFile)
            if fe.rettrno() == n:
                fe.show_feedata()
                print("ENTER THE NEW DETAILS OF THE STUDENT")
                fe.modify()
                pickle.dump(fe, outFile)
                print("RECORD UPDATED")
                found = 1
            else:
                pickle.dump(fe, outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found == 0:
            print("RECORD NOT FOUND ")

    except IOError:
        print("File could not be open !! Press any Key...")

    os.remove("feedata.dat")
    os.rename("temp.dat", "feedata.dat")


'function to delete a student from record through their admission number'
def delete_studata(n):
    found = 0

    try:
        inFile = open("student.dat", "rb")
        outFile = open("temp.dat", "wb")
        while True:
            st = pickle.load(inFile)
            if st.retadmno() == n:
                found = 1
                print("Record Deleted ..")
            # elif s.famnt == 20000:
            #     print("Collect Your Deposit of Rs 20000 from administration or reception")
            else:
                pickle.dump(st, outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found == 0:
            print("Record Not Found")

    except IOError:
        print("File could not be open !! Press any Key...")

    os.remove("student.dat")
    os.rename("temp.dat", "student.dat")


'function to delete fee details of specific students through their transaction number from the record'
def delete_feedata(n):
    found = 0

    try:
        inFile = open("feedata.dat", "rb")
        outFile = open("temp.dat", "wb")
        while True:
            fe = pickle.load(inFile)
            if fe.rettrno() == n:
                found = 1
                print("RECORD DELETED ..")
            # elif s.famnt == 20000:
            #     print("Collect Your Deposit of Rs 20000 from administration or reception")
            else:
                pickle.dump(fe, outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found == 0:
            print("RECORD NOT FOUND")

    except IOError:
        print("File could not be open !! Press any Key...")

    os.remove("feedata.dat")
    os.rename("temp.dat", "feedata.dat")


'function to display all student details'
def display_allStudent():
    print("STUDENT DATA LIST")
    print("%-16s" % "Adm No.", "%-20s" % "Name", "%-20s" % "Address", "%-20s" % "Contact", "%-20s" % "Email",
          "%-20s" % "Date of Birth")
    try:
        inFile = open("student.dat", "rb")
        while True:
            st = pickle.load(inFile)
            st.report()

    except EOFError:
        inFile.close()

    except IOError:
        print("File could not be open !! Press any Key...")



'function to display all students fee details'
def display_allFee():
    print("STUDENT FEE DATA LIST")
    print("%-10s" % "TR.NO.", "%-20s" % "NAME", "%-10s" % "MONTH", "%-9s" % "AMOUNT",
          "%-10s" % "REMAINING PAYMENT")
    try:
        inFile = open("feedata.dat", "rb")
        while True:
            fe = pickle.load(inFile)
            fe.report()

    except EOFError:
        inFile.close()

    except IOError:
        print("File could not be open !! Press any Key...")


'function of fee menu with its features'
def FeeMenu():
    while True:
        print("FEE MENU:")
        print("1. ADD NEW FEE DETAILS")
        print("2. SHOW FEE DETAILS")
        print("3. SHOW FEE DETAILS OF ALL STUDENT")
        print("4. DELETE FEE DETAILS")
        print("5. MODIFY FEE DETAILS")
        print("6. EXIT")
        print("\n")

        try:
            ch = int(input("ENTER YOUR CHOICE(1~6): "))
            print("\n")
            if ch == 1:
                write_feedata()

            elif ch == 2:
                num = int(input("ENTER TRANSACTION NUMBER: "))
                display_feedata(num)

            elif ch == 3:
                display_allFee()

            elif ch == 4:
                num = int(input("ENTER TRANSACTION NUMBER: "))
                delete_feedata(num)

            elif ch == 5:
                num = int(input("ENTER TRANSACTION NUMBER: "))
                modify_feedata(num)

            elif ch == 6:
                break

            else:
                print("INPUT CORRECT CHOICE...(1~6)")

        except NameError:
            print("INPUT CORRECT CHOICE...(1~6)")



'function of student menu with its features'
def StudentMenu():
    while True:
        print("STUDENT MENU:")

        print("1. New Admission")
        print("2. Modify Student ")
        print("3. Delete Student")
        print("4. All Student List")
        print("5. Return to Main Menu")
        print("\n")

        try:
            ch = int(input("Enter Your Choice(1~5): "))
            print("\n")
            if ch == 1:
                write_studata()

            elif ch == 2:
                num = int(input("\n\nEnter Admission Number : "))
                modify_studata(num)

            elif ch == 3:
                num = int(input("\n\nEnter Admission Number : "))
                delete_studata(num)

            elif ch == 4:
                display_allStudent()

            elif ch == 5:
                break

            else:
                print("Input correct choice...(1-5)")

        except NameError:
            print("Input correct choice...(1-5)")


'function of fixed courses'
def FixedCourses():
    print("LIST OF COURSES:")

    print("1. PYTHON")
    print("2. DJANGO ")
    print("3. HTML")
    print("4. CSS")
    print("5. JAVASCRIPT")
    print("\n")

'function of Inquiry where a new student can send their query'
def Inquiry():
    print("Please Feel Free To Ask Any Questions That You Might Have:")
    print(input("Enter your queries: "))
    print("\n")

'Introductory Function with main menu'
def intro():
    print("-------------Console Applicaiton for IT Academy---------------")

'main menu features and some messages'
intro()
while True:
    print("MAIN MENU:")
    print("1. FIXED COURSES")
    print("2. STUDENT MENU")
    print("3. FEE MENU ")
    print("4. INQUIRY(about the available course of study)")
    print("5. Exit")
    print("\n")

    try:
        ch = int(input("Enter Your Choice(1~5): "))

        if ch == 1:
            FixedCourses()

        elif ch == 2:
            StudentMenu()

        elif ch == 3:
            FeeMenu()

        elif ch == 4:
            Inquiry()

        elif ch == 5:
            break

        else:
            print("Input correct choice...(1-5)")

    except NameError:
        print("Input correct choice...(1-5)")

input("Please Contact Administration Department for more information. "
      "And Don't Forget To Collect Your Deposit after completion of your course.(press any key for further message.)")
input("Congratulations and best wishes for your next adventure!\n..(press any key to exit)")



