class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if self.is_valid(email):
            self._email = email
        else:
            self._email = '(missing email)'

    def who_I_am(self):
        return self.name + ' ' + self.email

    @staticmethod
    def is_valid(email):
        #use the module re (regular expression) for a correct solution
        name_domain = email.split('@')
        if len(name_domain) != 2:
            return False
        name, domain = name_domain

        if len(name) < 1 or len(domain) < 4:
            return False
        return True



class Supplier(Contact):
    def order(self, an_order):
        print("this is your order: ", an_order)

class Friend(Contact):
    def __init__(self, name, email, phone=''):
        super().__init__(name, email)
        self.phone = phone

if __name__ == '__main__':
    c = Contact('John Red', 'john@gmail.com')
    s = Supplier('Jim Black', 'jim@gmail.com')
    f1 = Friend('Sue Whita', 'sue@gmail.com', '123123')
    f2 = Friend('Ann Gray', 'ann.gmail.com', '777777')

    print(c.who_I_am())
    print(s.who_I_am())
    s.order('a_thing')
    print(f1.who_I_am(), ' ', f1.phone)
    print(f2.who_I_am(), ' ', f2.phone)
    f2.email='correct.email@abc.de'
    print(f2.who_I_am(), ' ', f2.phone)
