from abc import ABC, abstractmethod

# As we have to make Account as Abstract class ,Account class extends ABC
#---Abstract class consists of constuctor unlike interface ----#
class Account(ABC):
    
    def __init__(self,amount,num_of_years):
        self.amount = amount
        self.num_of_years = num_of_years
        self.min_balance = None
        self.rate = None


    @abstractmethod
    def set_interest_rate(self):
        pass

    @abstractmethod    
    def set_min_balance(self):
        pass

    def total_interest(self):
        return self.amount * self.num_of_years * self.rate  #----I = p*n*R/100-----#

class savings_account(Account):
    def __init__(self,amount,num_of_years):
        super().__init__(amount,num_of_years)

    def set_interest_rate(self):
        self.rate = 5/100  # ----5 % for savings(say) ------#

    def set_min_balance(self):
        self.min_balance = 10000

class current_account(Account):
    def __init__(self,amount,num_of_years):
        super().__init__(amount,num_of_years)


    def set_interest_rate(self):
        self.rate = 3/100  # ----5 % for current(say) ------#

    def set_min_balance(self):
        self.min_balance = 2000


amount, num_of_years = list(map(int,input('Enter deposit amount and number of years for savings account : ').split(',')))
new_savings_ac = savings_account(amount,num_of_years)
new_savings_ac.set_interest_rate()
new_savings_ac.set_min_balance()
print('Total Interest in Savings A/c => ',new_savings_ac.total_interest())


amount, num_of_years = list(map(int,input('Enter deposit amount and number of years for current account : ').split(',')))
new_curr_ac = current_account(amount,num_of_years)
new_curr_ac.set_interest_rate()
new_curr_ac.set_min_balance()
print('Total Interest in Current A/c => ',new_curr_ac.total_interest())
