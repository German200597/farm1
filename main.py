class Animal:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  def feed(self):
     print ('Животное покормили')


grey_goose = Animal('Cерый', 10)    
white_goose = Animal('Белый', 9)
Manka = Animal('Манка', 25)
Barashek = Animal('Барашек', 27)
Kudryaviy = Animal('Кудрявый', 28)
Koko = Animal('Коко', 7)
Kukareku = Animal('Кукареку', 8)
Kryakva = Animal('Кряква', 6)
Horn = Animal('Рога', 16)
Hoof = Animal('Копыта', 15)

print(Koko.feed())


class Goose:
   sound = 'grrrr'
grey_goose = Goose()
white_goose = Goose()

class Cow:
  sound = 'mooo'
Manka = Cow()

class Goat:
  sound = 'meeee'
Horn = Goat()
Hoof = Goat()

class Sheep:
  sound = 'mee' 
Barashek = Sheep()
Kudryaviy = Sheep()


class Chick:
  sound = 'ku-ka-re-ku'
Koko = Chick()
Kukareku = Chick()

class Duck:
  sound = 'krya'
Kryakva = Duck()

class Milking: 
  def milk():
    return('Животное подоили')









#  
  
  




