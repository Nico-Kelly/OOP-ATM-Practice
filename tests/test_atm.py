from ATM_Practice import ATM, Account, Other_Bank_Account, Technician, Administration
import pytest

@pytest.fixture
def nico():
    nico = Account(_pin=2026, name="Nico", _balance=500, _active=True, _credit_score = 55, _debt = 0)
    return nico

@pytest.fixture
def blocked_user():
    blocked_user = Account(_pin=2026, name="blocked", _balance=500, _active=False)
    return blocked_user

@pytest.fixture
def atm_new_york():
    cajero = ATM("New York", _cash_inventory=1000, _admin_key = 129)
    return cajero

@pytest.fixture
def atm_technician():
    atm_technician = Technician("George", 129)
    return atm_technician

@pytest.fixture
def atm_admin():
    atm_admin= Administration("Johnny Guitar", 1234)
    return atm_admin

@pytest.fixture #just for the admin and technician create from str tests
def johnny():
    johnny_c = "Johnny Cash, 1234"
    return johnny_c

#other b account fixtures
@pytest.fixture
def homero():
    homero = Other_Bank_Account(1234, "Homero", _balance = 5000, _active = True, _credit_score = 49)
    return homero

@pytest.fixture

def marge():
    marge = Other_Bank_Account(1234, "Marge", _balance = 10000, _active = True, _credit_score = 55, _debt = 0)
    return marge

@pytest.fixture(autouse=True)
def reset_counters():

    ATM.number_of_atms = 0
    Account.number_of_accounts = 0
    yield
# ATM CLASS TESTS

def test_create_atm_from_str():

    atm_str = "New York,50000,True,1234"

    new_york_str_atm = ATM.create_atm_from_string(atm_str)
    assert new_york_str_atm.__repr__() == f"ATM Located in New York"
    assert new_york_str_atm.cash_inventory == 50000
    assert new_york_str_atm.is_active is True
    assert new_york_str_atm.admin_key == 1234

def test_cash_inventory_is_protected(atm_new_york):

    assert atm_new_york.cash_inventory == 1000
    with pytest.raises(AttributeError):
        atm_new_york.cash_inventory = 5000

def test_change_power_status(atm_new_york):
    atm_new_york.change_power_status(129, new_status= False)

    assert atm_new_york._is_active == False

def test_withdraw_balance(atm_new_york, nico):
    
    atm_new_york.withdraw(nico, 1, 2026)
    assert nico.balance == 499

def test_atm_reload(atm_technician, atm_new_york):

    atm_technician.reload_atm(atm_new_york, 1)

    assert atm_new_york.cash_inventory == 1001

def test_denied_atm_reload(atm_technician,atm_new_york):

    initial_cash = atm_new_york.cash_inventory

    atm_technician._key = 1
    atm_technician.reload_atm(atm_new_york, 1000)

    assert atm_new_york.cash_inventory == initial_cash
    

def test_how_many_atm():

    cajero = ATM("New York", _admin_key = 1234)
    dublin_ATM = ATM("Dublin", _admin_key= 3950)
    
    assert ATM.how_many_atm() == 2
    
#Admin class tests

def test_create_admin_from_str(johnny):

    test_adm_str = Administration.create_admin_from_string(johnny)
    assert test_adm_str.__str__() == f"Johnny Cash is an authorized ATM Administrator"
    assert test_adm_str.key == 1234

def test_block_user_from_atm(atm_new_york, nico, atm_admin, homero): #updated this test to check that it blocks other_bank_account instances properly
    atm_admin.block_user(atm_new_york, nico)
    assert nico._active is False
    atm_admin.block_user(atm_new_york, homero)
    assert homero._active is False

#  Technician Class tests

def test_create_technician_from_str(johnny):

    test_technician_str = Technician.create_technician_from_string(johnny)
    assert test_technician_str.__str__() == f"Johnny Cash is an authorized ATM Technician"
    assert test_technician_str._key == 1234


def test_turn_off_and_on_atm(atm_new_york, atm_technician):

    atm_technician.turn_off_atm(atm_new_york)

    assert atm_new_york.is_active == False

    atm_technician.turning_on_atm(atm_new_york)
    
    assert atm_new_york.is_active == True


# Account class tests

def test_create_account_from_str():

    willie = "1694,Willie Nelson,1000,True"
    test_account_str = Account.create_account_from_string(willie)

    assert test_account_str.__repr__() == f"Account name: Willie Nelson \n pin: 1694,\n balance: 1000,\n active: True"
    assert test_account_str.pin == 1694
    assert test_account_str.name == "Willie Nelson"
    assert test_account_str.is_active is True
    assert test_account_str.balance == 1000


def test_how_many_users(nico):

    assert Account.how_many_accounts() == 1

def test_account_string_representation(nico, blocked_user):

    assert str(nico) == "You are Nico, your account is currently online"
    assert "currently disabled" in str(blocked_user)


def test_checkfund(nico):

    assert nico.check_funds(500) == True
    assert nico.check_funds(501) == False

def test_deduct(nico):

    nico.deduct(10)
    assert nico.balance == 490

def test_loan(nico):
    result = nico.request_loan(500)
    
    assert result is True
    assert nico.balance == 1000
    assert nico._debt == 500

#other account tests

def test_if_other_bank_account_inherits_properly(homero):
    
    assert homero.is_active is True
    assert homero.balance == 5000
    assert homero.pin == 1234
    assert homero.name == "Homero"
    assert homero._credit_score == 49

def test_Other_b_account_request_loan(homero):
    result = homero.request_loan(1000)

    assert result is False
    assert homero.balance == 5000

def test_other_bank_debt_after_loan(marge):
    marge.request_loan(100)
    assert marge.balance == 10100
    assert marge._debt == 110
def test_other_bank_account_fee(homero):
    homero.deduct(1000)

    assert homero.balance == 3900 # it has a 10% fee


