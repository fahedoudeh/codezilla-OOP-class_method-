class Employee:
    def calculate_salary(self, hours_worked, hourly_rate):
        return(hours_worked * hourly_rate)
    
    def print_info(self, name, age, job_title):
        print(f"Name: {name}\nAga: {age}\nJob Title: {job_title}")



new_employee = Employee()   
print(new_employee.calculate_salary(16, 4)) 

name = input("Enter name: ").strip().title()
age = int(input("Enter age: "))
title = input("Enter job title: ").strip().title()
new_employee.print_info(name, age, title)