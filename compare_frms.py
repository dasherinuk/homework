class Chicken:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return "Chicken: " + self.name
    
class Pig:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return "Pig: "+ self.name

class Farm:
    def __init__(self,name):
        self.name=name
        self.chicken=[]
        self.pig=[]

    def add_chicken(self,Chicken):
        if type(Chicken)==chicken:
            self.chickens.append(chicken)
    
    def add_pig(self,pig):
        if type(Pig)==pig:
            self.pigs.append(pig)

    def __str__(self):
        result = self.name + "\n"
        for chicken in self.chicken:
            result +=" " + str(chicken)
        result+="\n"
        for  pig in self.pig:
            result +=" " + str(pig)
        return result

    def __eq__(self, farm):
        return len(self.chickens) + len(self.pigs) == len(farm.chickens) + len(farm.pigs) 


    def __lt__(self, farm):
        return len(self.chickens) + len(self.pigs) < len(farm.chickens) + len(farm.pigs) 


f1 = Farm("Farm1")
f2 = Farm("Farm2")

print(f1)
print(f2)

f1.add_chicken(Chicken("Marusya"))
f1.add_pig(Dog("Tusik"))
f1.add_pig(Chicken("Leon"))
f1.add_pig(1)
#h1.dogs.append(45)#error incapsuletion
f2.add_pig(Chicken("Barsik"))
f2.add_chicken(Chicken("Belka"))
f2.add_chicken(900)
#h2.cats.append(100)#error incapsuletion


print(f1)
print(f2)

print(f1==f2)

print(f1<f2)
print(f1>f2)
