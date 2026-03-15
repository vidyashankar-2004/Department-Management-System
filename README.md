# Department-Management-System
Project Description: Department Management System 
The Department Management System is a web-based application developed using Python 
Django that allows organizations or institutions to manage department information digitally. 
The system helps in maintaining structured department records, assigning responsibilities, and 
organizing departmental data through a secure and centralized platform. 



Purpose of the Project 
The main objective of this project is to provide a centralized system to add, view, update, 
delete, and manage departments, reducing manual record-keeping and improving 
organizational efficiency. 



Key Features of the Project 



Authentication Module 
● Secure login and logout system 
● Only authenticated users can access department data 
● Role-based access can be extended (Admin / Staff) 



Department Management Module 
Users can: 
● Add new departments 
● View department details 
● Edit department information 
● Delete departments 
● Manage department active/inactive status 



Department Fields 
Each department record contains the following details: 
● Department Name 
● Department Code 
● Department Description 
● Head of Department (HOD) 
● Contact Email 
● Contact Phone Number 
● Department Location 
● Status (Active / Inactive) 
Created by
● Created At 



Additional Functionalities 
● Search departments by name or code 
● Pagination for large department lists 
● Export department data to CSV 
● Status-based filtering 


User Interface 
● Clean and professional design 
● Bootstrap-based responsive layout 
● Icon-based actions (Add, Edit, Delete) 
● Tooltips for better user experience 
● Reusable base template for consistency 


Pages Included 
● Login Page 
● Department List Page 
● Add Department Page 
● Edit Department Page 
● Admin Panel (Django Admin) 


Media & Static Handling 
● Static files for CSS and layout styling 
● Proper configuration for static content handling 


Testing & Validation 
● Authentication testing 
● CRUD operations testing 
● Search and pagination testing 
● CSV export validation 


# Connect to the SQLite database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Execute a query to fetch all departments
    cursor.execute("SELECT * FROM department_department")
    departments = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Return the list of departments as JSON response
    return JsonResponse({'departments': departments})
