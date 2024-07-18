#abstraction and encapsulation

#create  Account class with 2 attributes- balance & account no.
#create methods for debit, credit and priniting the balance

class Account:
    def __init__(self, bal,acc_no):
        self.bal= bal
        self.acc_no= acc_no

    #debit
    def debit(self, amount):
        self.bal = -amount
        print ( "Money is debited from your account ***** " )

    def credit(self, amount):
        self.bal= amount
        print(" Money is credited in  your account ***** " )
        

    def avl_bal (self):
        return self.bal

    
c1= Account(4500, 767676767)
print(c1.acc_no)

c1.avl_bal()