class ATM:
    def __init__(self,location, cash_inventory = 500000, is_active = True, _admin_key = None):
        self.location = location
        self.cash_inventory = cash_inventory
        self.is_active = is_active
        self.admin_key = _admin_key


    def get_status(self):
        return "ONLINE" if self.is_active else "OFFLINE"

    def change_power_status(self, key_input, new_status):

        if key_input == self.admin_key:
            self.is_active = new_status

            state_str = "ON" if new_status else "OFF"
            print('Access Allowed. ATM {}'.format(state_str))
        else:
            print("Not Allowed. Access Denied.")


    def withdraw(self, user, amount, pin_input):
        if not self.is_active:
            print("Out of service")
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
        print('Sucessful transaction. ${} have been withdrawn. Your new balance: ${}'.format(amount, user.balance))


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
    def reload_atm(self, reload_amount):
        pass




class Account:
    def __init__(self, pin, name, balance):
        self.pin = pin
        self.name = name
        self.balance = balance
    
    def check_funds(self, amount):
        return self.balance >= amount
    
    def deduct(self, amount):
        self.balance -= amount

    


if __name__ == '__main__':

    cajero = ATM("New York", is_active= True, _admin_key = 1234)

    nico = Account(2323, "Nico", 40000)

    #test

    cajero.withdraw(nico, 1040, 5034)

    print(f'Nico balance: {nico.balance}')

    cajero.withdraw(nico, 22000, 2323)

    print(f'Nico balance: {nico.balance}')



