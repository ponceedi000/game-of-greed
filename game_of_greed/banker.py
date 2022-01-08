# class Banker():
#     def __init__(self):
#         self.balance = 0
#         self.shelved = 0

#     def shelf(self,num):
#         self.shelved += num
#         return self.shelved

#     def bank(self):
#         self.balance += self.shelved
#         self.shelved = 0
#         return self.balance

#     def clear_shelf(self):
#         self.shelved = 0




class Banker:
    """Banker is reponsible for tracking points "on the shelf" and "in the bank"
    version_1
    """
    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def bank(self):
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def shelf(self, amt):
        self.shelved += amt

    def clear_shelf(self):
        self.shelved = 0