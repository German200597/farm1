class Cow:
  def __init__(self, name, weight, sound = 'mooo'):
    self.name = name
    self.weight = weight
Manka = Cow('Манка', 1)
сow_list = [Manka]

class Goat:
  def __init__(self, name, weight, sound = 'mee'):
    self.name = name
    self.weight = weight
Horn = Goat('Рога', 2) 
Hoof = Goat('Копыта', 10)
goat_list = [Horn, Hoof]

class Goose:
  def __init__(self, name, weight, sound = 'grrr'):
    self.name = name
    self.weight = weight
grey_goose = Goose('Серый', 3 )
white_goose = Goose('Белый', 4)
goose_list = [grey_goose, white_goose]

class Sheep:
  def __init__(self, name, weight, sound = 'myaa'):
    self.name = name
    self.weight = weight 
Barashek = Sheep('Кудрявый', 5)
Kudryaviy = Sheep('Барашек', 6)
sheep_list = [Barashek, Kudryaviy]


class Chick:
  def __init__(self, name, weight, sound = 'ku-ka-re-ku'):
    self.name = name
    self.weight = weight
Koko = Chick('Koko', 7)
Kukareku = Chick('Кукареку', 8)
chick_list = [Koko, Kukareku]


class Duck:
  def __init__(self, name, weight, sound = 'ku-ka-re-ku'):
    self.name = name
    self.weight = weight
Kryakva = Duck('Кряква', 9 )
duck_list = [Kryakva]


def milk():
  cow_goat = сow_list + goat_list
  for i in cow_goat:
    print(f'{i.name}: животное подоили')
milk()  

def feed():
  animals_list = сow_list+goat_list+sheep_list+chick_list+duck_list+goose_list
  for i in animals_list:
    print(f'{i.name}: животное покормили')
feed()

def collect():
  goose_chick_duck = goose_list+chick_list+duck_list
  for i in goose_chick_duck:
    print(f'{i.name}: яйца собраны')
collect()    

def shear():
  for i in sheep_list:
    print(f'{i.name}: животное постригли')
shear()  

def sum_weight(name, animal_type):
  summa=0
  for i in animal_type:
    summa+= i.weight
  print(f'Общий веc {name} — {summa} кг')


def max_weight(animal_type):
  for i in animal_type:
    weight = 0
    if i.weight > weight:
      weight = i.weight    
  print(f'Самое тяжелое животное в этой категории: {weight}')   
  
sum_weight('коров', сow_list) 
sum_weight('гусей', goose_list)
sum_weight('уток', duck_list)  
sum_weight('овец', sheep_list)
sum_weight('куриц', chick_list)  
sum_weight('коз', goat_list)  

max_weight(сow_list) 
max_weight(goose_list)
max_weight(duck_list)  
max_weight(sheep_list)
max_weight(chick_list) 
max_weight(goat_list)





























      










#  
  
  




