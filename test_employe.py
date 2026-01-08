from bank import bank_details
def test_bank_details():
    expected_output=(
        "accountnumber:1234567\n"
        "accountholdername:naveen\n"
        "accounttype:savings\n"
        "balance:10000\n"

    )
    assert bank_details("1234567","naveen","savings",10000)==expected_output
