class Person:
    __firstname = str()
    __lastname = str()
    __phone = str()

    def __init__(self, firstname: str, lastname: str, phone: str):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_phone(phone)

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_phone(self):
        return self.__phone

    def set_firstname(self, firstname: str):
        self.__firstname = firstname.capitalize()

    def set_lastname(self, lastname: str):
        self.__lastname = lastname.capitalize()

    def set_phone(self, phone: str):
        self.__phone = phone

    def set_firstname_godmode(self, firstname: str):
        self.__firstname = firstname

    def __str__(self):
        # Добавил наименования вводимых данных
        return f'Firstname: {self.__firstname} -- ' \
               f'Lastname: {self.__lastname} -- ' \
               f'Phone: {self.__phone}'

    def to_file(self, filename: str):
        with open(filename, 'a') as file:
            file.write(self.__str__() + '\n')

    def from_file(filename: str):
        res = [line for line in open(filename, 'r')]
        # for i in res:
        #     print(i, end='')
        return res


class Student(Person):
    __group = str()

    def __init__(self, firstname: str, lastname: str, phone: str, group: str):
        super().__init__(firstname, lastname, phone)
        self.set_group(group)

    def get_group(self):
        return self.__group

    def set_group(self, group: str):
        self.__group = group

    def __str__(self):
        # Добавил наименования вводимых данных
        return f'{super().__str__()} -- ' \
               f'Group: {self.__group}'

    def from_file(filename: str):
        # т.к. Person от Student отличается наличием группы =>
        # записываем из всего файла строки с наличием "Group:"
        # как вариант можно сделать в __str__ класса Student приписку что это студент
        # и список из файла составлять не по группе а по "Студенту"
        res = [line for line in open(filename, 'r') if 'Group:' in line]
        # for i in res:
        #     print(i, end='')
        return res


class Teacher(Person):
    __subject = str()

    def __init__(self, firstname: str, lastname: str, phone: str, subject: str):
        super().__init__(firstname, lastname, phone)
        self.set_subject(subject)

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject: str):
        self.__subject = subject

    def __str__(self):
        return f'{super().__str__()} -- ' \
               f'Subject: {self.__subject}'

    def from_file(filename: str):
        # т.к. Person от Teacher отличается наличием Subject=>
        # записываем из всего файла строки с наличием "Subject:"
        # как вариант можно сделать в __str__ класса Teacher приписку что это учитель
        # и список из файла составлять не по предмету а по "Учителю"
        res = [line for line in open(filename, 'r') if 'Subject:' in line]
        # for i in res:
        #     print(i, end='')
        return res


li = []

# для удобства перепроверки все имена поменял на Student
li.append(Student('Student', 'Bulkin', 'trinolyatrulyalya', 'Python11'))
li.append(Student('Student', 'Terkin', '+387415874165', 'Python21'))
li.append(Student('Student', 'Chechetkina', '+04478451235', 'C++14'))
li.append(Student('Student', 'Bulkina', 'trinolyatrulyalya2', 'Python11'))
li.append(Student('Student', 'Fedorov', '0991234756', 'C++17'))
# для удобства перепроверки все имена поменял на Teacher
li.append(Teacher('Teacher', 'Bulkin', 'trinolyatrulyalya', 'Python11'))
li.append(Teacher('Teacher', 'Terkin', '+387415874165', 'Python21'))
li.append(Teacher('Teacher', 'Chechetkina', '+04478451235', 'C++14'))
li.append(Teacher('Teacher', 'Bulkina', 'trinolyatrulyalya2', 'Python11'))
li.append(Teacher('Teacher', 'Fedorov', '0991234756', 'C++17'))
# для удобства перепроверки все имена поменял на Person
li.append(Person('Person', 'Bulkin', 'trinolyatrulyalya'))
li.append(Person('Person', 'Terkin', '+387415874165'))
li.append(Person('Person', 'Chechetkina', '+04478451235'))
li.append(Person('Person', 'Bulkina', 'trinolyatrulyalya2'))
li.append(Person('Person', 'Fedorov', '0991234756'))

# Записываем все введеные данные из списка в файл
for i in li:
    print(i)
    i.to_file('test.txt')

# получаем из файла список всех персон
person_from_file = Person.from_file('test.txt')
print(f'Все записи из файла:\n{person_from_file}')
# получаем из файла только студентов
student_from_file = Student.from_file('test.txt')
print(f'Только студенты из файла:\n{student_from_file}')
# получаем из файла только учителей
teacher_from_file = Teacher.from_file('test.txt')
print(f'Только учителя из файла:\n{teacher_from_file}')
