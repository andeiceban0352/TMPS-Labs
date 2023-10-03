from bank.domain.models.customer import Customer

class RegularCustomer(Customer):
    def add_account(self, account):
        self.accounts.append(account)

class VIPCustomer(Customer):
    def __init__(self, customer_id, name, accounts, vip_points=0):
        super().__init__(customer_id, name, accounts)
        self._vip_points = vip_points

    @property
    def vip_points(self):
        return self._vip_points

    def add_account(self, account):
        self.accounts.append(account)

    def earn_vip_points(self, points):
        self._vip_points += points

