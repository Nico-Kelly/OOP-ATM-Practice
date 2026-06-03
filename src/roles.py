class Technician:
    def __init__(self, name, _key):
        self.name = name
        self._key = _key

    def __repr__(self):
        return f"Technician: {self.name} \n Key: {self.key}"

    def __str__(self):
        return f"{self.name} is an authorized ATM Technician"

    @classmethod
    def create_technician_from_string(cls, data_string):
        name, key_str = data_string.split(',')
        key = int(key_str)
        return cls(name, key)

    @property
    def key(self):
        return self._key

    def turn_off_atm(self, atm_instance):
        atm_instance.change_power_status(self._key, new_status=False)
        return ('{} Turning down ATM... '.format(self.name))

    def turning_on_atm(self, atm_instance):
        atm_instance.change_power_status(self._key, new_status=True)
        return ('{} Turning on ATM...'.format(self.name))

    def reload_atm(self, atm_instance, reload_amount):
        atm_instance.reload_inventory(key_input=self._key, reload_amount=reload_amount)
        return (f"{self.name} is attempting to reload the ATM.. ")


class Administration:

    def __init__(self, name, key):
        self.name = name
        self._key = key

    @classmethod
    def create_admin_from_string(cls, data_string):
        name, key_str = data_string.split(',')
        key = int(key_str)
        return cls(name, key)

    @property
    def key(self):
        return self._key

    def __repr__(self):
        return f"Administrator: {self.name} \n Key: {self._key}"

    def __str__(self):
        return f"{self.name} is an authorized ATM Administrator"

    def block_user(self, atm_instance, account_to_block):
        account_to_block._active = False
        return (
            f"Suspicious activity alert. {account_to_block} is blocked from this {atm_instance}, for more info contact with the bank")