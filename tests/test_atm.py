from ATM_Practice import ATM, Account, Technician, Administration




# ATM CLASS TESTS

def test_account_string_representation():

    nico = Account(1234, "Nico", 100, active=True)
    blocked_user = Account(1234, "banned", 0, active=False)

    assert str(nico) == "You are Nico, your account is currently online"
    assert "currently disabled" in str(blocked_user)

def test_initial_balance():

    pepe = Account(1234, "Pepe", 500, active=True)
    assert pepe.balance == 500

def test_change_power_status():

    atm = ATM("New Jersey", 10000, is_active=True, _admin_key= 129)
    atm.change_power_status(129, new_status= False)

    assert atm.is_active == False

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
    
    Johnny.block_user(cajero, nico)
    assert nico.active is False

def test_how_many_atm():
    ATM.number_of_atms = 0 #manual reset

    cajero = ATM("New York", is_active= True, _admin_key = 1234)
    dublin_ATM = ATM("Dublin", is_active=False, _admin_key= 3950)
    
    assert ATM.how_many_atm() == 2
    

#  Technician Class tests

def test_turn_off_atm():
    
    box = ATM("Colorado", 1000, is_active=True, _admin_key = 130)
    george = Technician("George", 130)

    george.turn_off_atm(box)

    assert box.is_active == False

    
# Account class tests
def test_how_many_users():

    Account.number_of_accounts = 0

    nico = Account(2026, "Nick", 0, active=True)

    assert Account.how_many_accounts() == 1

