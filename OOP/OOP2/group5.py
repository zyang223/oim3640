class bank:

    trans=None
    if trans ==None:
        trans=[]

    def __init__(self,holder,balance,card_type,trans):
        self.holder=holder
        self.balance=balance
        self.card_type=card_type
        self.trans=
    def __str__(self):
        return f"Account holder: {self.holder}\nBalance: {self.balance}\nCard type: {self.card_type}\nTransaction history: {self.trans}"

    
    

Zide=bank("Zide","9999","credit"," 001")
print(Zide)
        

    
        
