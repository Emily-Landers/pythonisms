class Stuff:
    def __init__(self, owner, skills, money):
        self.skills = skills
        self.owner = owner
        self.money = money

    def __str__(self):
        return 'Software Dev {} with current skills of {} and money available ${}'.format(self.owner, self.skills, self.money)
    

        
person1 = Stuff('alsoSteve', 'Python snake', 25)
person2 = Stuff('me', 'stuff', 25000)
person3 = Stuff('Test person', 'Python', 10)
print(person1)
print(person2)
print(person3)