import datetime
class ATM:

    number_of_atms = 0

    def __init__(self,location, cash_inventory = 500000, is_active = True, _admin_key = None):
        self.location = location
        self.cash_inventory = cash_inventory
        self.is_active = is_active
        self.admin_key = _admin_key
        self.closed_on_sundays()

        ATM.number_of_atms += 1

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
            self.is_active = new_status

            state_str = "ON" if new_status else "OFF"
            return('Access Allowed. ATM {}'.format(state_str))
        else:
            return("Not Allowed. Access Denied.")
    
    def closed_on_sundays(self):
        date_today = datetime.datetime.now().weekday()
        #date_today = 6
        if date_today == 5:
            print(f"Sorry ATM closed")
            self.is_active = False
    def withdraw(self, user, amount, pin_input):

        if not self.is_active:
            print("Out of service")
            return
        
        if not user.active:
            print("Blocked Account")
            return
            
        if amount > self.cash_inventory:
            print("ATM Machine has not enough exchange")
            return
        
        if pin_input != user.pin:
            print("Error, wrong PIN")
            return

        if not user.check_funds(amount):
            print("Error: Insufficient funds")
            return      
        
        user.deduct(amount)
        self.cash_inventory -= amount
        print('Successful transaction. ${} have been withdrawn. Your new balance: ${}'.format(amount, user.balance))

    def reload_inventory(self, key_input, reload_amount):

        if key_input == self.admin_key:
                self.cash_inventory += reload_amount
                print(f"Successfully reloaded ${reload_amount}")
                print(f"Current ATM inventory: ${self.cash_inventory}")
        else:
                print(f"Not Allowed. Access Denied.")

    @classmethod
    def how_many_atm(cls):
        how_m = cls.number_of_atms
        return how_m

class Technician:
    def __init__(self,name, key):
        self.name = name
        self.key = key

    def __repr__(self):
        return f"Technician: {self.name} \n Key: {self.key}"
    
    def __str__(self):
        return f"{self.name} is an authorized ATM Technician"

    def turn_off_atm(self,atm_instance): 
        atm_instance.change_power_status(self.key, new_status = False)
        return('{} Turning down ATM... '.format(self.name))
    
    def turning_on_atm(self, atm_instance):
        atm_instance.change_power_status(self.key, new_status = True)
        return('{} Turning on ATM...'.format(self.name))

    def reload_atm(self, atm_instance, reload_amount):
        atm_instance.reload_inventory(key_input=self.key, reload_amount=reload_amount)
        return (f"{self.name} is attempting to reload the ATM.. ")
    
class Administration:

    def __init__(self, name, key):
        self.name = name
        self.key = key
    
    def __repr__(self):
        return f"Administrator: {self.name} \n Key: {self.key}"
    
    def __str__(self):
        return f"{self.name} is an authorized ATM Administrator"

    def block_user(self, atm_instance, account_to_block):
        account_to_block.active = False
        return(f"Suspicious activity alert. {account_to_block} is blocked from this {atm_instance}, for more info contact with the bank")
class Account:

    number_of_accounts = 0
    def __init__(self, pin, name, balance, active=True):
        self.pin = pin
        self.name = name
        self.balance = balance
        self.active = active

        Account.number_of_accounts += 1
    
    def check_funds(self, amount):
        return self.balance >= amount
    
    def deduct(self, amount):
        self.balance -= amount

    def __repr__(self):
        return f"Account name: {self.name} \n pin: {self.pin},\n balance: {self.balance},\n active: {self.active}"
    
    def __str__(self):

        if self.active == True:
            return f"You are {self.name}, your account is currently online"
        else:
            return f"You are {self.name}, your account is currently disabled, please contact with the bank for further information"

    @classmethod
    def how_many_accounts(cls):
        how_m = cls.number_of_accounts
        return how_m
