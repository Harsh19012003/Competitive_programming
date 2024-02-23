class Student:
    # ive used getters and setters for assigning and retreiving object's attributes
    # related to 
    def get_name(self):
        return self.name
    def set_name(self, a):
        self.name = a

    # related to barnch
    def get_branch(self):
        return self.branch
    def set_branch(self, a):
        self.branch = a

    # related to subsyaytem
    def get_subsystem(self):
        return self.subsystem
    def set_subsystem(self, a):
        self.subsystem = a

    # related to id where id is set to private
    def get_id_no(self):
        return self.__id_no
    def set_id_no(self, a):
        self.__id_no = a

    # related to email
    def get_email(self):
        return self.email
    def set_email(self, a):
        self.email = a

    
# x is one student
x = Student()

# using the set function
print("Enter name: ")
name = input()
x.set_name(name)

print("Enter branch: ")
branch = input()
x.set_branch(branch)

print("Enter subsystem: ")
subsystem = input()
x.set_subsystem(subsystem)

print("Enter id_no: ")
id_no = input()
x.set_id_no(id_no)

print("Enter email: ")
email = input()
x.set_email(email)

# using the get function printing everyything
print(x.name)
print(x.get_branch())
print(x.get_subsystem())
print(x.get_id_no())
print(x.get_email())
