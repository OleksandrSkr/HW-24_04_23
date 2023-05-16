import unittest

from Classes.User import User
from Classes.Admin import Admin
from Classes.Developer import Developer

class TestStringMethods(unittest.TestCase):

    def test_is_string(self):
        a = User.say_hello(User)
        self.assertTrue(type(a), str)


    def test_is_number(self):
        d = Admin.mend_something(Admin)
        self.assertTrue(type(d), int)
 

    def test_is_list(self):
        c = Developer.write_code(Developer)
        self.assertTrue(type(c), list)  
        
    def test_items_is_numbers(self):
        d = Developer.write_code(Developer)
        for item in d:
            self.assertTrue(type(item), int)

if __name__ == '__main__':
    unittest.main()