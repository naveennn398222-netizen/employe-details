def bank_details(accountnumber,accountholdername, accounttype, balance):
    result = (
        f"accountnumber:{accountnumber}\n"
        f"accountname:{accountholdername}\n"
        f"type:{accounttype}\n"
        f"balance:{balance}\n"
    )
    return result
if __name__ == "__main__":
    accountnumber ="1234567"
    accountholdername ="name"
    accounttype ="savings"
    balance =10000
    print(bank_details(accountnumber,accountholdername,accounttype,balance))
