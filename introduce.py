class MyName:
    def __init__(self, name, school):
        self.name = name
        self.school = school

    def introduce(self):
        print('안녕하세요')
        print(f'{self.name}입니다')

object1 = MyName('유경','이화')
object1.introduce()