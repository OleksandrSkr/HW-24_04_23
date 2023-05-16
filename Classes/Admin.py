class Admin:
    def __init__ (self, login, password, rights ):
        self._login = login
        self._password = password
        self._rights = rights
    
    def say_hello(self):
        return "Hello world"
#        print("Hello World")
    def mend_something(self):
        return "01101101"
#        print("01101101")