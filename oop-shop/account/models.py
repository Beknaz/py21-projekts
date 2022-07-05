import permissions

class User:
    objects = []
    def __init__(self, email, name, sex):
        self.email = email
        self.name = name
        self.sex = sex
        self.__password = None
        self.is_authenticated = False
        print(f"Успешно создан{self.email}")
        User.objects.append(self)
        
    def resister(self, password, password_confirm):
        if password != password_confirm:
            raise Exception("Пароли не совпадают")
        self.__password = password
        print(f"Регистрация успешна {self.email}")

    def login(self, password):
        if self.__password != password:
            raise Exception("Пароль не верный")
        self.is_authenticated = True
        print(f"Успешно залогинился юзер {self.email}")

    def logout(self):
        permissions.login_required(self)
        self.is_authenticated = False
        print(f"Успешно вышел{self.email}")