from employe import employee_details
def test_employee_details():
    expected_output=(
        "Employee name:furkhan\n"
        "Employee id:E1001\n"
        "department:kitchen\n"
        "salary:250\n"

    )
    assert employee_details("furkhan","E1001","kitchen",250)==expected_output
