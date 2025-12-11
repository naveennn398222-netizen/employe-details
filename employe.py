def employee_details(name, emp_id, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department  : {department}\n"
        f"Salary      : {salary}"
    )
    return result
if __name__ == "__main__":
    name = "furkhan"
    emp_id = "E1001"
    department = "kitchen"
    salary = 250
    print(employee_details(name, emp_id, department, salary))
