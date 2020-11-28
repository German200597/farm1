def sound(self):
  print(f'{self.name} подает голос: {self.sound}')

class Animal:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight 
  def feed(self):
    print(f'{self.name}: животное покормили')
  def sound_giving(self):
    print(f'{self.name} подает голос:{self.sound}')

class Milk(Animal):
  def __init__(self, name, weight):
    super().__init__(name, weight)
  def milk(self): 
    print(f'{i.name}: животное подоили')
    
class Egg(Animal):
  def __init__(self, name, weight):
    super().__init__(name, weight)
  def collect(self):
    print(f'{i.name}: яйца собраны')


class Cow(Milk):
  def __init__(self, name, weight):
    super().__init__(name, weight) 
    self.sound = 'mooo'
  def milk(self):
    print(f'{i.name}: животное подоили')
  def sound_giving(self):
    super().sound_giving()



class Goat(Milk):
  def __init__(self, name, weight):
    super().__init__(name, weight)
    self.sound = 'meee'
  def milk(self):
    print(f'{i.name}: животное подоили') 
  def sound_giving(self):
    super().sound_giving()    


class Goose(Egg):
  def __init__(self, name, weight):
      super().__init__(name, weight) 
      self.sound = 'grrr'
  def sound_giving(self):
    super().sound_giving()    
      
class Sheep(Animal):
  def __init__(self, name, weight):
      super().__init__(name, weight)
      self.sound = 'myaa'   
  def shear(self):
    print(f'{i.name}: животное постригли')
  def sound_giving(self):
    super().sound_giving()  
    
class Chick(Egg):
  def __init__(self, name, weight):
    super().__init__(name, weight) 
    self.sound = 'ku-ka-re-ku'
  def sound_giving(self):
    super().sound_giving()  
    

class Duck(Egg):
  def __init__(self, name, weight):
    super().__init__(name, weight) 
    self.sound = 'krya'
  def sound_giving(self):
    super().sound_giving()  
    


Manka = Cow('Манка', 1)
Koko = Chick('Koko', 1)
Kukareku = Chick('Кукареку', 8)
Barashek = Sheep('Барашек', 7)
Kudryaviy = Sheep('Кудрявый', 6)
Kryakva = Duck('Кряква', 9 )
grey_goose = Goose('Серый', 9)
white_goose = Goose('Белый', 4)
Horn = Goat('Рога', 1) 
Hoof = Goat('Копыта', 2)   

сow_list = [Manka] 
goat_list = [Horn, Hoof]
goose_list = [grey_goose, white_goose]
sheep_list = [Barashek, Kudryaviy]
chick_list = [Koko, Kukareku]
duck_list = [Kryakva]
goose_chick_duck = goose_list+chick_list+duck_list
cow_goat = сow_list + goat_list
animals_list = сow_list+goat_list+sheep_list+chick_list+duck_list+goose_list


    
for i in animals_list:
  i.feed()
for i in goose_chick_duck:
  i.collect()
for i in sheep_list:
  i.shear()  
for i in cow_goat:
  i.milk()

for i in animals_list:
  i.sound_giving()  
