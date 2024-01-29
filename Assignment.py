class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


def sort_employees(employees, sort_param):
    if sort_param == 1:
        return sorted(employees, key=lambda x: x.age)
    elif sort_param == 2:
        return sorted(employees, key=lambda x: x.name)
    elif sort_param == 3:
        return sorted(employees, key=lambda x: x.salary)
    else:
        return employees


if __name__ == "__main__":
    
    employee_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000)
    ]

    print("Choose Sorting Parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    sort_parameter = int(input("Enter your choice: "))

    sorted_employees = sort_employees(employee_data, sort_parameter)

    print("\nSorted Employee Data:")
    for emp in sorted_employees:
        print(emp)
