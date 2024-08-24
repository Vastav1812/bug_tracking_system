# ADMIN MODULE

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="bug_tracking_system"
)


def print_login_model():
    print("Please select Your Role ")
    while True:
        print(" 1) Login as Admin or Expert")
        print(" 2) Login as customer")
        print(" 3) Create New Account")
        break
    choice = input("Enter your choice : ")
    if choice == "1":
        admin_login()
    elif choice == "2":
        customer_login()
    elif choice == "3":
        create_account()
    else:
        print("Invalid Input Retry!")
        print_login_model()


def admin_module():
    print("Admin Module")
    while True:
        print("Admin Services")
        print("1. Manage Services (View, Search) ")
        print("2. Manage Employee (Add, View, Search, Edit, Activate/Deactivate) ")
        print("3. Manage Bug( View, Search, AssignBugToExpert) ")
        print("4. Logout")
        break
    choice = input("Enter your choice: ")

    if choice == "1":
        manage_services()
        choice = input("Enter your choice : ")
        if choice == "1":
            view_customers()
        elif choice == "2":
            customer_search_by_name()
        elif choice == "3":
            customer_search_by_login_id()
        else:
            print("Invalid Input! Retry")

    elif choice == "2":
        employee_services()
        choice = input("Enter your choice : ")
        if choice == "4":
            add_new_admin_or_expert()
        elif choice == "5":
            view_all_employees()
        elif choice == "6":
            employee_search_by_name()
        elif choice == "7":
            employee_search_by_login_id()
        elif choice == "8":
            employee_search_by_employee_type()
        elif choice == "9":
            employee_status_update()
        elif choice == "10":
            change_password_admin()
        else:
            print("Invalid Input! Retry")

    elif choice == "3":
        bug_services()
        choice = input("Enter your choice : ")
        if choice == "11":
            view_all_bugs()
        elif choice == "12":
            bug_search_by_bug_id()
        elif choice == "13":
            bug_search_by_bug_status()
        elif choice == "14":
            bug_search_by_customer_login_id()
        elif choice == "15":
            assign_bug_expert()
        elif choice == 16:
            logout()
        else:
            print("Invalid Input! Retry")

    elif choice == "4":
        logout()

    else:
        print("Invalid Input! Retry")


# 1. Manage Services (View, Search)

def manage_services():
    print("Manage Services")
    while True:
        print("1. Customer: View All")
        print("2. Customer: Search - by Customer Name")
        print("3. Customer: Search - by Customer Login Id")
        break


def view_customers():
    print("View all customers here\n")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        # SQL Query to view all customers
        query = "SELECT * FROM  CUSTOMER"
        # Execute the query
        cursor.execute(query)

        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<15s} | {2:<15s} | {3:<8s} | {4:<15s} | {5:<25s}"
        print("------------------------------------------------------------------------------------------------")
        print(s1.format("custLoginId", "custPassword", "custName", "custAge", "custPhone", "custEmail"))
        print("------------------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])))
        print("------------------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while viewing customer list ", err)


def customer_search_by_name():
    print("Search customer by name here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter customer name :")
        # SQL Query to search customer by name
        query = "SELECT * FROM CUSTOMER WHERE custName = %s"
        # Execute the query
        cursor.execute(query, (z,))
        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<15s} | {2:<15s} | {3:<8s} | {4:<15s} | {5:<25s}"
        print("------------------------------------------------------------------------------------------------")
        print(s1.format("custLoginId", "custPassword", "custName", "custAge", "custPhone", "custEmail"))
        print("------------------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])))
        print("------------------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while searching customer by name ", err)


def customer_search_by_login_id():
    print("Search customer by Login ID here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter customer Login ID here :")
        # SQL Query to search customer by login ID
        query = "SELECT * FROM CUSTOMER WHERE custLoginId = %s"
        # Execute the query
        cursor.execute(query, (z,))
        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<15s} | {2:<15s} | {3:<8s} | {4:<15s} | {5:<25s}"
        print("------------------------------------------------------------------------------------------------")
        print(s1.format("custLoginId", "custPassword", "custName", "custAge", "custPhone", "custEmail"))
        print("------------------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])))
        print("------------------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while searching customer by Login ID ", err)

# 2. Manage Employee (Add, View, Search, Edit, Activate/Deactivate)


def employee_services():
    print("Manage Employee :")
    while True:
        print("4. Employee: Add New (Admin or Expert)")
        print("5. Employee: View All")
        print("6. Employee: Search - by Employee Name")
        print("7. Employee: Search - by Employee Login Id")
        print("8. Employee: Search - by Employee Type")
        print("9. Employee: Activate or Deactivate")
        print("10 .Employee: Change Password")
        break


def add_new_admin_or_expert():
    print("Add new Admin or Expert here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        p = input("Enter Employee Login ID : ")
        q = input("Enter employee password : ")
        r = input("Enter Employee Type : ")
        s = input("Enter Employee Name :")
        t = input("Enter Employee contact no. :")
        u = input("Enter Employee email : ")

        # SQL Query to add new admin or expert
        query = f"INSERT INTO employee(empLoginId ,empPassword, empType, empName, empPhone, empEmail) "\
                f"VALUES('{p}','{q}','{r}','{s}','{t}','{u}')"

        # Execute the query
        cursor.execute(query)
        db.commit()
        print("Employee added successfully")
    except mysql.connector.Error as err:
        print("Error occurred while inserting new employee ", err)


def view_all_employees():
    print("Showing all Employees : ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        # SQL Query to view all employee
        query = "SELECT * FROM employee"
        # Execute the query
        cursor.execute(query)
        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<12s} | {2:<10s} | {3:<20s} | {4:<15s} | {5:<25s} | {6:<15s}"
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        print(s1.format("empLoginId", "empPassword", "empType", "empName", "empPhone", "empEmail", "empStatus"))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while viewing all employee ", err)


def employee_search_by_name():
    print("Search employee by name here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter employee name :")
        # SQL Query to search employee by name
        query = "SELECT * FROM employee WHERE empName = %s"
        # Execute the query
        cursor.execute(query, (z,))

        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<12s} | {2:<10s} | {3:<20s} | {4:<15s} | {5:<25s} | {6:<15s}"
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        print(s1.format("empLoginId", "empPassword", "empType", "empName", "empPhone", "empEmail", "empStatus"))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while searching employee by name ", err)


def employee_search_by_login_id():
    print("Search employee by Login ID here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter employee Login ID :")
        # SQL Query to search employee by login ID
        query = "SELECT * FROM employee WHERE empLoginId = %s"
        # Execute the query
        cursor.execute(query, (z,))
        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<12s} | {2:<10s} | {3:<20s} | {4:<15s} | {5:<30s} | {6:<15s}"
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        print(s1.format("empLoginId", "empPassword", "empType", "empName", "empPhone", "empEmail", "empStatus"))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while searching employee by Login ID ", err)


def employee_search_by_employee_type():
    print("Search employee by employee type here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter employee type(ADMIN/EXPERT) :")
        # SQL Query to search employee by employee type
        query = "SELECT * FROM employee WHERE empType = %s"
        # Execute the query
        cursor.execute(query, (z,))
        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<12s} | {2:<10s} | {3:<20s} | {4:<15s} | {5:<30s} | {6:<15s}"
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        print(s1.format("empLoginId", "empPassword", "empType", "empName", "empPhone", "empEmail", "empStatus"))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while searching employee by type", err)


def employee_status_update():
    print("set employee status here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter updated employee status(ACTIVE/DEACTIVE) :")
        y = input("Enter Employee Name : ")
        # SQL Query to update status of the employee
        query = f"UPDATE employee SET empStatus = '{z}' WHERE empName = '{y}'"
        # Execute the query
        cursor.execute(query)
        db.commit()
        print('Employee Status Updated successfully')
    except mysql.connector.Error as err:
        print("Error occurred while updating status", err)
        db.close()


def change_password_admin():
    print("set new password here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        y = input("Enter Employee Login ID :")
        z = input("Enter new password :")
        # SQL Query to update password
        query = "UPDATE employee SET empPassword = %s WHERE empLoginId = %s "
        # Execute the query
        cursor.execute(query, (z, y))
        db.commit()
        print("Password changed successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating password", err)

#  Bug Services -  Manage Bug( View, Search, AssignBugToExpert )


def bug_services():
    print("Bug Services:")
    while True:
        print("11. Bug: View All")
        print("12. Bug: Search by bugId")
        print("13.Bug: Search by status")
        print("14.Bug: Search by custLoginId")
        print("15.Bug: Assign to Expert")
        print("16.Logout")
        break


def view_all_bugs():
    print("View All Bugs here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        # SQL Query to view all bugs
        query = "SELECT * FROM bug "
        # Execute the query
        cursor.execute(query)
        allrows = cursor.fetchall()

        s1 = "{0:<8s} | {1:<20s} | {2:<12s} | {3:<10s} | {4:<12s} | {5:<30s} | {6:<20s} | {7:<16s} | " \
             "{8:<16s} | {9:<30s}"
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        print(s1.format("bugId", "bugPostingDate", "custLoginId", "bugStatus", "productName", "bugDesc",
                        "expertAssignedDate", "expertLoginId", "bugSolvedDate", "solution"))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
                            str(row[6]), str(row[7]), str(row[8]), str([9])))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while fetching Bug Table", err)


def bug_search_by_bug_id():
    print("View bug by giving Bug ID here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Bug ID:")
        # SQL Query to search bug by using bug id
        query = "SELECT * FROM bug WHERE bugId = %s"
        # Execute the query
        cursor.execute(query, (z,))
        allrows = cursor.fetchall()

        s1 = "{0:<8s} | {1:<20s} | {2:<12s} | {3:<10s} | {4:<12s} | {5:<30s} | {6:<20s} | {7:<16s} | " \
             "{8:<16s} | {9:<30s}"
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        print(s1.format("bugId", "bugPostingDate", "custLoginId", "bugStatus", "productName", "bugDesc",
                        "expertAssignedDate", "expertLoginId", "bugSolvedDate", "solution"))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
                            str(row[6]), str(row[7]), str(row[8]), str([9])))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while fetching Bug details using Bug ID:", err)


def bug_search_by_bug_status():
    print("View bug by giving Bug Status:")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Bug Status:")
        # SQL Query to search bugs by using status
        query = "SELECT * FROM bug WHERE bugStatus = %s"
        # Execute the query
        cursor.execute(query, (z,))
        allrows = cursor.fetchall()

        s1 = "{0:<8s} | {1:<20s} | {2:<12s} | {3:<10s} | {4:<12s} | {5:<30s} | {6:<20s} | {7:<16s} | " \
             "{8:<16s} | {9:<30s}"
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        print(s1.format("bugId", "bugPostingDate", "custLoginId", "bugStatus", "productName", "bugDesc",
                        "expertAssignedDate", "expertLoginId", "bugSolvedDate", "solution"))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
                            str(row[6]), str(row[7]), str(row[8]), str([9])))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while fetching Bug details using Bug Status:", err)


def bug_search_by_customer_login_id():
    print("View bug by giving Customer Login ID:")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Customer Login ID:")
        # SQL Query to view bug by using customer login id
        query = "SELECT * FROM bug WHERE custLoginId = %s"
        # Execute the query
        cursor.execute(query, (z,))
        allrows = cursor.fetchall()

        s1 = "{0:<8s} | {1:<20s} | {2:<12s} | {3:<10s} | {4:<12s} | {5:<30s} | {6:<20s} | {7:<16s} | " \
             "{8:<16s} | {9:<30s}"
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        print(s1.format("bugId", "bugPostingDate", "custLoginId", "bugStatus", "productName", "bugDesc",
                        "expertAssignedDate", "expertLoginId", "bugSolvedDate", "solution"))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
                            str(row[6]), str(row[7]), str(row[8]), str([9])))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while fetching Bug details using Bug ID ", err)


def assign_bug_expert():
    print("Assigning bug to Expert")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter employee login ID of Expert that you want to assign : ")
        y = input("Enter Bug ID of bug that you want to assign expert to : ")
        # assigning current date and time
        from datetime import datetime
        expertassigneddate = datetime.now()
        # SQL Query to assign bug to expert
        query = f"UPDATE Bug SET expertAssignedDate = '{expertassigneddate}', expertLoginId = '{z}' WHERE bugId = '{y}'"
        # Execute the query
        cursor.execute(query)
        db.commit()
    except mysql.connector.Error as err:
        print("Error occurred while fetching Bug details using Bug ID:", err)


def logout():
    print_login_model()

# EXPERT MODULE


def expert_module():
    print("Expert Module : ")
    while True:
        print("1) View Assigned Bug")
        print("2) Filter Assigned Bugs based on status")
        print("3) Solve the Bug")
        print("4) Change Password")
        break
    choice = input("Enter your choice:")

    if choice == "1":
        view_assigned_bug()
    elif choice == "2":
        filter_assigned_bugs_based_on_status()
    elif choice == "3":
        solve_the_bug()
    elif choice == "4":
        change_password_expert()
    else:
        print("Invalid Input. Retry...")


def view_assigned_bug():
    print("View assigned bug here : ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Expert ID:")
        # SQL Query to search assigned bugs
        query = f"SELECT * FROM bug WHERE expertLoginId = '{z}' "
        # Execute the query
        cursor.execute(query)
        allrows = cursor.fetchall()

        s1 = "{0:<8s} | {1:<20s} | {2:<12s} | {3:<10s} | {4:<12s} | {5:<30s} | {6:<20s} | {7:<16s} | " \
             "{8:<16s} | {9:<30s}"
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        print(s1.format("bugId", "bugPostingDate", "custLoginId", "bugStatus", "productName", "bugDesc",
                        "expertAssignedDate", "expertLoginId", "bugSolvedDate", "solution"))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
                            str(row[6]), str(row[7]), str(row[8]), str([9])))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while fetching Assigned Bug details. ", err)


def filter_assigned_bugs_based_on_status():
    print("View assigned bugs based on Bug Status:")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Bug Status:")
        x = input("Enter Expert Login ID : ")
        # SQL Query to search bugs by using status
        query = f"SELECT * FROM bug WHERE bugStatus = '{z}' AND expertLoginId = '{x}' "
        # Execute the query
        cursor.execute(query)
        allrows = cursor.fetchall()

        s1 = "{0:<8s} | {1:<20s} | {2:<12s} | {3:<10s} | {4:<12s} | {5:<30s} | {6:<20s} | {7:<16s} | " \
             "{8:<16s} | {9:<30s}"
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        print(s1.format("bugId", "bugPostingDate", "custLoginId", "bugStatus", "productName", "bugDesc",
                        "expertAssignedDate", "expertLoginId", "bugSolvedDate", "solution"))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
                            str(row[6]), str(row[7]), str(row[8]), str([9])))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while fetching Bug details using Bug Status.", err)


def solve_the_bug():
    print("Solve Bugs here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Solution : ")
        x = input("Enter Bug ID : ")
        # assigning current date and time
        from datetime import datetime
        bugsolvedate = datetime.now()
        # SQL Query to search bugs by using status
        query = f"UPDATE Bug SET solution = '{z}', bugSolvedDate = '{bugsolvedate}' WHERE bugId = '{x}' "
        # Execute the query
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("Error occurred while Updating Bug Solution.", err)


def change_password_expert():
    print("set new password here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter Old password : ")
        y = input("Enter Expert Login ID : ")
        z = input("Enter new password : ")
        # SQL Query to update password
        query = f"UPDATE employee SET empPassword = '{z}' WHERE empLoginId = '{y}' AND empPassword = '{x}' "
        # Execute the query
        cursor.execute(query)
        print("Password changed successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating password:", err)


# CUSTOMER MODULE


def customer_module():
    print("Customer Module : ")
    while True:
        print("1) logout")
        print("2) Update Account")
        print("3) Post New Bug")
        print("4) View All Bugs")
        print("5) Search Bugs based on status")
        print("6) View Bug Solution")
        print("7) Change Password")
        break

    choice = input("Enter your choice: ")
    if choice == "1":
        logout()
    elif choice == "2":
        list_update_account()
        choice = input("Enter your choice: ")
        if choice == "1":
            update_login_id()
        elif choice == '2':
            update_name()
        elif choice == "3":
            update_age()
        elif choice == "4":
            update_contact_number()
        elif choice == "5":
            update_email()
        else:
            print("Invalid Input. Retry! ")
    elif choice == "3":
        post_new_bug()
    elif choice == "4":
        view_all_bugs_customer()
    elif choice == "5":
        bug_search_by_bug_status_customer()
    elif choice == "6":
        view_bug_solution()
    elif choice == "7":
        change_password()
    else:
        logout()


def create_account():
    print("Creating new account:")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        p = input("Enter Customer Login ID : ")
        q = input("Enter Customer password : ")
        r = input("Enter Customer Name : ")
        s = input("Enter Customer Age : ")
        t = input("Enter Customer contact no. :")
        u = input("Enter Customer email : ")

        # SQL Query to add new customer
        query = f"INSERT INTO customer(custLoginId, custPassword, custName, custAge, custPhone, custEmail)" \
                f"VALUES('{p}', '{q}', '{r}', '{s}', '{t}', '{u}')"
        # Execute the query
        cursor.execute(query)
        db.commit()
        print("Account created Successfully")
    except mysql.connector.Error as err:
        print("Error occurred while creating new account. ", err)


def list_update_account():
    print("Select Option to Update : ")
    while True:
        print("1. Customer Login ID")
        print("2. Customer Name")
        print("3. Customer Age")
        print("4. Customer Contact Number")
        print("5. Customer Email")
        break


def update_login_id():
    print("Update Login ID here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter your password here : ")
        y = input("Enter old Customer Login ID : ")
        z = input("Enter new customer Login ID :")
        # SQL Query to search customer by login ID
        query = f"UPDATE customer SET custLoginId = '{z}' WHERE custLoginId = '{y}' AND password = '{x}'"
        # Execute the query
        cursor.execute(query)
        print("Login Id Updated Successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating customer Login ID. ", err)


def update_name():
    print("Update name here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter your password here : ")
        y = input("Enter new name here : ")
        z = input("Enter customer Login ID :")
        # SQL Query to search customer by login ID
        query = f"UPDATE customer SET custName = '{y}' WHERE custLoginId = '{z}' AND password = '{x}'"
        # Execute the query
        cursor.execute(query)
        print("Name Updated Successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating name. ", err)


def update_age():
    print("Update Age here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter your password here : ")
        y = input("Enter new Age here : ")
        z = input("Enter customer Login ID :")
        # SQL Query to search customer by login ID
        query = f"UPDATE customer SET custAge = '{y}' WHERE custLoginId = '{z}' AND password = '{x}'"
        # Execute the query
        cursor.execute(query)
        print("Age Updated Successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating Age. ", err)


def update_contact_number():
    print("Update contact number here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter your password here : ")
        y = input("Enter new contact number here : ")
        z = input("Enter customer Login ID :")
        # SQL Query to search customer by login ID
        query = f"UPDATE customer SET custPhone = '{y}' WHERE custLoginId = '{z}' AND password = '{x}' "
        # Execute the query
        cursor.execute(query)
        print("Contact Number Updated Successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating contact number. ", err)


def update_email():
    print("Update email here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter your password here : ")
        y = input("Enter new email here : ")
        z = input("Enter customer Login ID :")
        # SQL Query to search customer by login ID
        query = f"UPDATE customer SET custEmail = '{y}' WHERE custLoginId = '{z}' AND password = '{x}' "
        # Execute the query
        cursor.execute(query)
        print("Email Id Updated Successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating email. ", err)


def post_new_bug():
    print("Post new bug here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        cust_login_id = input("Enter your login ID: ")
        product_name = input("Enter the product name: ")
        bug_desc = input("Enter the bug description: ")
        from datetime import datetime
        bugpostingdate = datetime.now()
        query = f"INSERT INTO bug(bugPostingDate = '{bugpostingdate}', custLoginId = '{cust_login_id}, " \
                f"productName = '{product_name}', bugDesc = '{bug_desc})' "
        cursor.execute(query)
        db.commit()
        print("Bug posted successfully!")
    except mysql.connector.Error as err:
        print("Error occurred while posting new bug. ", err)


def view_all_bugs_customer():
    print("View all Bugs here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter Customer Login ID : ")
        # SQL Query to view all Bugs of customer itself
        query = f"SELECT * FROM  bug WHERE custLoginId = '{x}' "
        # Execute the query
        cursor.execute(query)
        allrows = cursor.fetchall()

        s1 = "{0:<8s} | {1:<20s} | {2:<12s} | {3:<10s} | {4:<12s} | {5:<30s} | {6:<20s} | {7:<16s} | " \
             "{8:<16s} | {9:<30s}"
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        print(s1.format("bugId", "bugPostingDate", "custLoginId", "bugStatus", "productName", "bugDesc",
                        "expertAssignedDate", "expertLoginId", "bugSolvedDate", "solution"))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
                            str(row[6]), str(row[7]), str(row[8]), str([9])))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while viewing bugs. ", err)


def bug_search_by_bug_status_customer():
    print("View bug by giving Bug Status here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Bug Status:")
        x = input("Enter Customer Login ID : ")
        # SQL Query to search bugs by using status
        query = f"SELECT * FROM bug WHERE bugStatus = '{z}' AND custLoginId = '{x}' "
        # Execute the query
        cursor.execute(query)
        allrows = cursor.fetchall()

        s1 = "{0:<8s} | {1:<20s} | {2:<12s} | {3:<10s} | {4:<12s} | {5:<30s} | {6:<20s} | {7:<16s} | " \
             "{8:<16s} | {9:<30s}"
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        print(s1.format("bugId", "bugPostingDate", "custLoginId", "bugStatus", "productName", "bugDesc",
                        "expertAssignedDate", "expertLoginId", "bugSolvedDate", "solution"))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
                            str(row[6]), str(row[7]), str(row[8]), str([9])))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while searching Bug details using Bug Status. ", err)


def view_bug_solution():
    print("View solution of bugs here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter BUG ID : ")
        y = input("Enter your customer login Id : ")
        # SQL Query to view bug solution
        query = f"SELECT * FROM bug WHERE bugId = '{x}' AND custLoginId = '{y}' "
        # Execute the query
        cursor.execute(query)
        allrows = cursor.fetchall()

        s1 = "{0:<8s} | {1:<20s} | {2:<12s} | {3:<10s} | {4:<12s} | {5:<30s} | {6:<20s} | {7:<16s} | " \
             "{8:<16s} | {9:<30s}"
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        print(s1.format("bugId", "bugPostingDate", "custLoginId", "bugStatus", "productName", "bugDesc",
                        "expertAssignedDate", "expertLoginId", "bugSolvedDate", "solution"))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
                            str(row[6]), str(row[7]), str(row[8]), str([9])))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while viewing Bug Solution. ", err)


def change_password():
    print("set new password here :")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter Current password")
        y = input("Enter Customer Login ID")
        z = input("Enter new password :")
        # SQL Query to update password
        query = f"UPDATE customer SET custPassword = '{z}' WHERE custLoginId = '{y}' AND custPassword = '{x}' "
        # Execute the query
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("Error occurred while updating password. ", err)


def admin_login():
    username = input("Enter Login ID : ")
    userpassword = input("Enter Password : ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    # sql query to check password
    query = " select * from employee where empLoginId = '%s' "
    values = username
    cursor.execute(query % values)
    try:
        row = cursor.fetchmany(1)[0]
        dbPass = row[1]
        if userpassword == dbPass:
            print("Login authentication success")
            utype = row[2]
            if utype == 'ADMIN':
                admin_module()
            else:
                expert_module()
        else:
            print("Login authentication failed")
    except IndexError:
        print("Invalid User Name or password .Retry...")

    db.commit()
    db.close()


def customer_login():
    username = input("Enter customer Login ID : ")
    userpassword = input("Enter customer Password : ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    # sql query to check password
    query = f" select * from customer where custLoginId = '{username}' AND custPassword = '{userpassword}' "
    cursor.execute(query)
    try:
        row = cursor.fetchmany(1)[0]
        dbPass = row[1]
        if userpassword == dbPass:
            print("Login authentication success")
            customer_module()
        else:
            print("Login authentication failed")
    except IndexError:
        print("Invalid User Name or password  .Retry...")

    db.commit()
    db.close()


print_login_model()