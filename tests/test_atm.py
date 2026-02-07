from ATM_Practice import ATM, Account, Technician, Administration

def test__account_string_representation():

    nico = Account(1234, "Nico", 100, active=True)
    blocked_user = Account(1234, "banned", 0, active=False)


    assert str(nico) == "You are Nico, your account is currently online"
    assert "currently disabled" in str(blocked_user)



def test_initial_balance():

    pepe = Account(1234, "Pepe", 500, active=True)
    assert pepe.balance == 500


def test_withdraw_balance():

    cajero = ATM("New York", is_active= True, _admin_key = 1234)

    nico = Account(2323, "Nico", 40000)

    cajero.withdraw(nico, 1, 2323)

    assert nico.balance == 39999


def test_atm_reload():

    cajero = ATM("New York", is_active= True, _admin_key = 1234)

    jorge = Technician("Jorge", 1234)

    jorge.reload_atm(cajero, 1)

    assert cajero.cash_inventory == 500001

def test_block_user_from_atm():
    cajero = ATM("New York", is_active= True, _admin_key = 1234)
    Johnny = Administration("Johnny Guitar", 1234)
    nico = Account(1453, "Nico", 10)
    
    assert Johnny.block_user(cajero, nico) == (f"Suspicious activity alert. {nico} is blocked from this {cajero.location} ATM, for more info contact with the bank")

