import datetime
class ATM:
    def __init__(self,location, cash_inventory = 500000, is_active = True, _admin_key = None):
        self.location = location
        self.cash_inventory = cash_inventory
        self.is_active = is_active
        self.admin_key = _admin_key
        self.closed_on_sundays()


    def __repr__(self):
        return f"ATM Located in {self.location}"

    def get_status(self):
        return "ONLINE" if self.is_active else "OFFLINE"

    def change_power_status(self, key_input, new_status):

        if key_input == self.admin_key:
            self.is_active = new_status

            state_str = "ON" if new_status else "OFF"
            print('Access Allowed. ATM {}'.format(state_str))
        else:
            print("Not Allowed. Access Denied.")
    
    def closed_on_sundays(self):
        date_today = datetime.datetime.now().weekday()
        #date_today = 6
        if date_today == 6:
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

class Technician:
    def __init__(self,name, key):
        self.name = name
        self.key = key

    def turn_off_atm(self,atm_instance): 
        print('{} Turning down ATM... '.format(self.name))
        atm_instance.change_power_status(self.key, new_status = False)

    def turning_on_atm(self, atm_instance):
        print('{} Turning on ATM...'.format(self.name))
        atm_instance.change_power_status(self.key, new_status = True)

    def reload_atm(self, atm_instance, reload_amount):
        print(f"{self.name} is attempting to reload the ATM.. ")
        atm_instance.reload_inventory(key_input=self.key, reload_amount=reload_amount)
class Administration:

    def __init__(self, name, key):
        self.name = name
        self.key = key

    def block_user(self, atm_instance, account_to_block):
        print(f"Suspicious activity alert. {account_to_block} is blocked from this {atm_instance}, for more info contact with the bank")
        account_to_block.active = False
class Account:
    def __init__(self, pin, name, balance, active=True):
        self.pin = pin
        self.name = name
        self.balance = balance
        self.active = active
    
    def check_funds(self, amount):
        return self.balance >= amount
    
    def deduct(self, amount):
        self.balance -= amount

    def __repr__(self):
        return f"{self.name}"

if __name__ == '__main__':

    cajero = ATM("New York", is_active= True, _admin_key = 1234)

    nico = Account(2323, "Nico", 40000)

    #test

    cajero.withdraw(nico, 1040, 5034)

    print(f'Nico balance: {nico.balance}')

    cajero.withdraw(nico, 1, 2323)

    print(f'Nico balance: {nico.balance}')

    print(cajero.cash_inventory)

# atm reload test

jorge = Technician("Jorge", 1234)

jorge.reload_atm(cajero, 1) #should be 500000 again

# block account test

Merli = Administration("Merlina", 1234)

Merli.block_user(cajero, nico)


#Trying to withdraw from a blocked account 

cajero.withdraw(nico,100,2323) #passed