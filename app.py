from Classes.User import User
from Classes.Admin import Admin
from Classes.Developer import Developer

print(User.say_hello(User))

print(Admin.say_hello(Admin))
print(Admin.mend_something(Admin))

print(Developer.say_hello(Developer))
print(Developer.mend_something(Developer))
print(Developer.write_code(Developer))
