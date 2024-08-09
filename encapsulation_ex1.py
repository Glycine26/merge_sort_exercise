"Incase of encapsulation, '__'(double underscore) written previous to variable name, that value is encapsulated"
"The attributes Acct_no & password should be private (not directly accessible from outside the class)."
"In Python, private attributes are typically prefixed with a double underscore (__)."

class MyBankAccount():
    def __init__(self, name:str, Acct_no:int, Acct_balance:int, password:str):
        self.name = name
        self.__Acct_no = Acct_no
        self.Acct_balance = Acct_balance
        self.__password = password
        
    def balance_info(self,password:str):
        if password == self.__password:
            msg1 = f"Your acoount balance is: {self.Acct_balance}"
            return msg1
        
    def money_withdraw_info(self,password:str,):
        money_draw = int(input("Enter the amount to with draw: "))
        if password == self.__password and self.Acct_balance >= money_draw:
            self.Acct_balance-=money_draw
            return self.Acct_balance
    def money_credit_info(self,password:str):
        money_cred = int(input("Enter the amount to deposit: "))
        if password == self.__password:
            self.Acct_balance+=money_cred
            return self.Acct_balance

account_detail = MyBankAccount("Shri.Diganth", 2020, 10000, "abc123")
print(account_detail.balance_info("abc123"))
print(account_detail.money_credit_info("abc123"))
print(account_detail.money_withdraw_info("abc123"))
