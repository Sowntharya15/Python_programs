#check if the passwords are matching :
class Password:
    #private modifier
    __password = 1234
    def passWordchecker(self,password):
        return self.__password == password

user = Password()
variable = int(input())
print(user.passWordchecker(variable))