from ATM_Practice import ATM, Account, Technician, Administration

def test__account_string_representation():

    nico = Account(1234, "Nico", 100, active=True)
    blocked_user = Account(1234, "banned", 0, active=False)


    assert str(nico) == "You are Nico, your account is currently online"
    assert "currently disabled" in str(blocked_user)



def test_initial_balance():

    pepe = Account(1234, "Pepe", 500, active=True)
    assert pepe.balance == 500