class Account:
    number_of_accounts = 0

    def __init__(self, _pin, name, _balance, _active=True, _credit_score=50, _debt=0):
        self._pin = _pin
        self.name = name
        self._balance = _balance
        self._active = _active
        self._credit_score = _credit_score
        self._debt = _debt

        Account.number_of_accounts += 1

    @classmethod
    def create_account_from_string(cls, data_string):
        pin_str, name, balance_str, active_str = data_string.split(',')
        _pin = int(pin_str)
        _balance = int(balance_str)
        _active = active_str.strip() == "True"

        return cls(_pin, name, _balance, _active)

    @property
    def pin(self):
        return self._pin

    @property
    def balance(self):
        return self._balance

    @property
    def is_active(self):
        return self._active

    @property
    def debt(self):
        return self._debt

    def __repr__(self):
        return f"Account name: {self.name} \n pin: {self._pin},\n balance: {self._balance},\n active: {self._active}"

    def __str__(self):

        if self._active == True:
            return f"You are {self.name}, your account is currently online"
        else:
            return f"You are {self.name}, your account is currently disabled, please contact with the bank for further information"

    @classmethod
    def how_many_accounts(cls):
        how_m = cls.number_of_accounts
        return how_m

    def check_funds(self, amount):
        return self._balance >= amount

    def deduct(self, amount):
        if amount <= 0:
            raise ValueError("Amount MUST be positive")
        self._balance -= amount

    def request_loan(self, amount):
        if self.is_active:
            if self._credit_score > 50:
                self._balance += amount
                self._debt += amount
                return True
            return False
        return False


class Other_Bank_Account(Account):

    def __init__(self, _pin, name, _balance, _active=True, _credit_score=49, _debt=None, ):
        super().__init__(_pin, name, _balance, _active, _credit_score, _debt)

    def deduct(self, amount):
        fee = amount * 0.10
        total_amount = amount + fee
        self._balance -= total_amount

    def request_loan(self, amount):
        approved_loan = super().request_loan(amount)

        if approved_loan:
            fee = amount * 0.10
            self._debt += fee
            return True
        return False

