from student_impl import StudentImpl



class Account(StudentImpl):
    # made constractor
    def __init__(self, name, dept, cradit, amount, waver):
        super(Account, self).__init__(name = name, dept=dept)
        self.cradit = cradit
        self.amount = amount
        self.waver = waver
        self.payment = 0.0

    def get_total_sFee(self):
        return self.cradit * self.amount

    def get_payment(self):
        if self.waver == 0:
            self.payment = self.cradit * self.amount
            return self.payment 
        else:
            self.payment = (self.cradit * self.amount) - self.waver
            return self.payment

    def make_payment(self, amount):
        self.payment = self.payment - amount
        return self.payment
        


# Here account is an object and inharitance
account = Account('Pavel', 'MBA', 20, 4000, 20000)
print(account.getName(), account.getDept())
print(account.get_total_sFee())
print(account.get_payment())
print(account.make_payment(20000))
