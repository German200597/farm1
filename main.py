class Cow:
  sound = 'mooo' 
Manka = Cow()


class Goat:
  sound = 'meeee'  
Horn = Goat() 
Hoof = Goat()

class Goose:
  sound = 'grrrr' 
grey_goose = Goose()
white_goose = Goose()

class Sheep:
  sound = 'mee' 
Barashek = Sheep()
Kudryaviy = Sheep()



class Chick:
  sound = 'ku-ka-re-ku'
Koko = Chick()
Koko.name = 'Коко'
Koko.weight = 2
Kukareku = Chick()


class Duck:
  sound = 'krya'
Kryakva = Duck()



class Animal:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  def interaction(self):
    if isinstance(self, Animal): 
      self.status_one = f' {self.name}: животное покормили'
      print(self.status_one)
  
    if isinstance(self, Cow) or isinstance(self, Goat):
      self.status_two = f' {self.name}: животное подоили'
      print(self.status_two)
    else:
      print(f' {self.name}: животное не надо доить')
  
    if isinstance(self, Sheep):
      self.status_three = f' {self.name}: животное постригли'
      print(self.status_three)    
    else:
      print(f' {self.name}: животное не надо cтричь')
  
    if isinstance(self, Goose) or isinstance(self, Chick) or isinstance(self, Duck):
      self.status_four = f' {self.name}: яйца собрали'
      print(self.status_four)    
    else:
      print(f' {self.name}: у животного не надо собирать яйца')


animal_list = dict()
def animal_counting(animal):
  if isinstance(animal, Animal):
    animal_list[animal.name] = animal.weight
    next
  else:
    return animal_list

grey_goose = Animal('Серый', 9)
white_goose = Animal('Белый', 8)
Manka = Animal('Манка', 25)
Horn = Animal('Рога', 6)
Hoof = Animal('Копыта', 3)
Barashek = Animal('Барашек', 8)
Kudryaviy = Animal('Кудрявый', 10)
Koko = Animal('Коко', 4)
Kukareku = Animal('Кукареку', 11)
Kryakva = Animal('Кряква', 10)

animal_counting(grey_goose)
animal_counting(white_goose)
animal_counting(Manka)
animal_counting(Horn)
animal_counting(Hoof)
animal_counting(Barashek)
animal_counting(Kudryaviy)
animal_counting(Koko)
animal_counting(Kukareku)
animal_counting(Kryakva)

def weight_counting():
  summa=0
  for i in animal_list.values():
    summa+= i
  print(f'Общий веc животных — {summa} кг')

def heaviest():
  maximum = max(animal_list.values())
  for key, value in animal_list.items():
    if value == maximum:
      print(f'{key} — самое тяжелое животное')

weight_counting()       
heaviest()  

Manka.interaction()
grey_goose.interaction()
white_goose.interaction()
Horn.interaction()
Hoof.interaction()
Barashek.interaction()
Kudryaviy.interaction()
Koko.interaction()
Kukareku.interaction()
Kryakva.interaction()






























      










#  
  
  




