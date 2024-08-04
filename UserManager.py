class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def addUser(self, name):
        user_id = self.next_id
        self.users[user_id] = name
        self.next_id += 1
        return user_id

    def getUser(self, user_id):
        return self.users.get(user_id, None)

    def deleteUser(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def findUserByName(self, name):
        return [user_id for user_id, user_name in self.users.items() if user_name == name]

# Пример использования
user_manager = UserManager()

# Добавление пользователей
id1 = user_manager.addUser("Alice")
id2 = user_manager.addUser("Bob")
id3 = user_manager.addUser("Alice")

print("ID добавленных пользователей:", id1, id2, id3)

# Получение пользователей по идентификатору
print("Имя пользователя с ID 1:", user_manager.getUser(id1))
print("Имя пользователя с ID 2:", user_manager.getUser(id2))
print("Имя пользователя с ID 3:", user_manager.getUser(id3))

# Удаление пользователей
print("Удаление пользователя с ID 2:", user_manager.deleteUser(id2))
print("Удаление пользователя с ID 2 снова (должно быть False):", user_manager.deleteUser(id2))

# Поиск пользователей по имени
print("Пользователи с именем 'Alice':", user_manager.findUserByName("Alice"))
print("Пользователи с именем 'Bob':", user_manager.findUserByName("Bob"))
print("Пользователи с именем 'Charlie':", user_manager.findUserByName("Charlie"))
