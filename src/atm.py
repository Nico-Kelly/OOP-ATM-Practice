import datetime


class ATM:
    number_of_atms = 0

    def __init__(self, location, _cash_inventory=500000, _is_active=True, _admin_key=None):
        self.location = location
        self._cash_inventory = _cash_inventory
        self._is_active = _is_active
        self.admin_key = _admin_key
        self.closed_on_sundays()
        ATM.number_of_atms += 1

    @property
    def cash_inventory(self):
        return self._cash_inventory

    @property
    def is_active(self):
        return self._is_active

    @classmethod
    def create_atm_from_string(cls, data_string):
        # Creates an ATM instance with the format location-cash inventory- is active - admin key
        location, cash_str, is_active_str, admin_key_str = data_string.split(',')

        cash_inventory = int(cash_str)

        admin_key = int(admin_key_str)

        is_active = is_active_str.strip() == "True"

        return cls(location, cash_inventory, is_active, admin_key)

    @classmethod
    def how_many_atm(cls):
        how_m = cls.number_of_atms
        return how_m

    def __repr__(self):
        return f"ATM Located in {self.location}"

    def __str__(self):
        if self.is_active == True:
            return f"This is {self.location} ATM, currently active"
        else:
            return f"This is {self.location} ATM, currently out of service"

    def get_status(self):
        return "ONLINE" if self.is_active else "OFFLINE"

    def change_power_status(self, key_input, new_status):

        if key_input == self.admin_key:
            self._is_active = new_status

            state_str = "ON" if new_status else "OFF"
            return f'Access Allowed. ATM {state_str}'
        else:
            return "Not Allowed. Access Denied."

    def closed_on_sundays(self):
        date_today = datetime.datetime.now().weekday()
        # date_today = 6
        if date_today == 6:
            # self._is_active = False
            return "Sorry ATM closed"

    def withdraw(self, user, amount, pin_input):

        if not self.is_active:
            return "Out of service"

        if not user.is_active:
            return "Blocked Account"

        if amount > self.cash_inventory:
            return "ATM Machine has not enough exchange"

        if pin_input != user.pin:
            return "Error, wrong PIN"

        if not user.check_funds(amount):
            return "Error: Insufficient funds"

        user.deduct(amount)
        self._cash_inventory -= amount
        return f'Successful transaction. ${amount} have been withdrawn. Your new balance: ${user.balance}'

    def reload_inventory(self, key_input, reload_amount):

        if key_input == self.admin_key:
            self._cash_inventory += reload_amount
            print(f"Successfully reloaded ${reload_amount}")
            print(f"Current ATM inventory: ${self._cash_inventory}")
        else:
            print(f"Not Allowed. Access Denied.")

    def empty_atm(self):
        if self._cash_inventory == 0:
            return "Out of Service"