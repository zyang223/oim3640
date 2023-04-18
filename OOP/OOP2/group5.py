class bank:

    trans = None
    if trans is None:
        trans = []

    def __init__(self, holder, balance, card_type, trans=None):
        self.holder = holder
        self.balance = balance
        self.card_type = card_type
        self.trans = trans

    def __str__(self):
        return f"Account holder: {self.holder}\nBalance: {self.balance}\nCard type: {self.card_type}\nTransaction history: {self.trans}"

    def __stealmoney__(self):
        if self.balance != 0:
            self.trans = [-self.balance]
        return f"Your money has been stolen: {self.holder}{self.balance}{self.trans},"

Zide = bank("Zide", "9999", "credit", "001")
Dapanji = bank("dapanji", "0", "debt")
print(Zide, Dapanji)

        

    
        
