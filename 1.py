class Car:
    def __init__(self, name, model, color, hp):
        print('Car created')
        self.model=model
        self.name=name
        self.color=color
        self.hp=hp
    def showFeatures(self):
        print('A ',self.color,self.name,self.model,'car with ',self.hp,'horse power is created.')
    def changeName(self,name):
        self.name=name
    def changeColor(self,color):
        self.color=color
    def __del__(self):
        print('Car is destroyed.')
c1 = Car("Audi","Q7","Black","250")  
c1.showFeatures()
c1.changeName("Benz")
c1.changeColor("Silver")
c1.showFeatures()
del c1