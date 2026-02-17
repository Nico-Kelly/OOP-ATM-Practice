from ATM_Practice import ATM, Account, Technician, Administration
import pytest

@pytest.fixture
def nico():
    nico = Account(_pin=2026, name="Nico", _balance=500, _active=True)
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


@pytest.fixture(autouse=True)
def reset_counters():

    ATM.number_of_atms = 0
    Account.number_of_accounts = 0
    yield
# ATM CLASS TESTS

def test_create_from_str():

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


def test_block_user_from_atm(atm_new_york, nico, atm_admin):
    atm_admin.block_user(atm_new_york, nico)
    assert nico._active is False



#  Technician Class tests

def test_turn_off_and_on_atm(atm_new_york, atm_technician):

    atm_technician.turn_off_atm(atm_new_york)

    assert atm_new_york.is_active == False

    atm_technician.turning_on_atm(atm_new_york)
    
    assert atm_new_york.is_active == True


# Account class tests
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



