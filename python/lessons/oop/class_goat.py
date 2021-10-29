class Goat:
    age=0
    name=""
    def show (self): # функция в классе это МЕТОД класса. self -обязательная ссылка на объект для которого вызван этот метод
        print(self.age)
        print (self.name)

a=Goat()
a.age=2
a.name="Зорька"
b=Goat()
b.age=1
b.name="Ночка"
a.show()
b.show()
