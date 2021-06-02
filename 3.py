class Student:
    def __init__(self,grade,name,roll,phn):
        print('Student admitted')
        self.grade=grade
        self.name=name
        self.roll=roll
        self.phn=phn
class Sport(Student):
    def __init__(self,grade,name,roll,phn,sport):
        self.grade=grade
        self.name=name
        self.roll=roll
        self.phn=phn
        self.sport=sport
    def showAttributes(self):
        print('Grade    :\t',self.grade)
        print('Name     :\t',self.name)
        print('Roll No  :\t',self.roll)
        print('Phone No :\t',self.phn)
        print('Sport    :\t',self.sport)
        print('\n')
    def changePhn(self,phn):
        self.phn=phn
        print('Phone number changed')
        self.showAttributes()
        print('\n')
    def showSport(self):
        print(self.name,'plays',self.sport)
        print('\n')
    def changeSport(self,sport):
        self.sport=sport
        print('Sport changed')
        self.showAttributes()
        print('\n')
    def __del__(self):
        print(self.name,'doesn\'t play sports anymore.')
st1=Student("2nd","Venu","21","6301677089")        
sp1=Sport("2nd","Venu","21","6301677089","Basket Ball")
sp1.showAttributes()
sp1.showSport()
sp1.changePhn("7993273965")
sp1.changeSport("Football")
del sp1


        