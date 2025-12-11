def employee_details(name, emp_id, department, salary):
    result = (
        f"name:{name}\n"
        f"emp_id:{emp_id}\n"
        f"department:{department}\n"
        f"salary:{salary}\n"
    )
    return result
if __name__ == "__main__":
    name ="furkhan"
    emp_id ="E1001"
    department ="kitchen"
    salary =250
    print(employee_details(name,emp_id,department,salary))
