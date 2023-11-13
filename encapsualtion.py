#an object is an instance of the class,its a concrete realization of the classe blue print
#an object have attributes and methods associated with them 
#encapsualation is concept of bundling data and methods
#thst r thast that thsth thst that that thar thst that 
#that operate oon on that data into a single unit ,i.e,class 
#in python you can control acess to  attributes using access specifiers 
#in pyythjon you can control acess to attributes using access specifiers like public ,privste proivate,protected

#init is not required in the class ,but its commonly used to set up initial state  of an object
#thisn  commbiantion is essential for working with object oriented python programming

#encapsulation 
class bankaccount:
    def __init__(self,acnum,balance):
        self.acnum=acnum
        self.__balance=balance   #private attribute
    def getbalance(self):
        return self.__balance
    def deposite(self,amount):
        self.__balance+=amount
    
#creating objects (instance )of class
#creating bank account
account=bankaccount("12345",5000)

#access #attribuytes# attributes and calling methods
print(account.getbalance())

#add the money and modify the balance
account.deposite(500) 
account.getbalance()
        
