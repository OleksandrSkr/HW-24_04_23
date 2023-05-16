class Developer:
    def __init__ (self, login, password, skill):
        self._login = login
        self._password = password
        self._skill = skill
        
    def say_hello (self):
        return "Hello world"
#        print("Hello World")
    def mend_something (self):
        return "01101101"
#        print("01101101")
    
    def write_code (self):
        return [0,1,0,0,1,0]
#        print([0, 1, 0, 0, 1, 0])
 