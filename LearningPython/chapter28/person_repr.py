"""
    Script add __repr__ overload methods for printing objects
"""


class Person:
    def __init__(self, name, job='dev', pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', 'dev', 10000)
    print(bob)
    print(sue)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(.01)
    print(sue)