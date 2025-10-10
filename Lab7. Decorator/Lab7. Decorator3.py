class User:
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role


class Component:
    def delete_user(self) -> str:
        pass


class DeleteUserComponent(Component):
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def delete_user(self) -> str:
        return f"Пользователь с ID {self.user_id} успешно удален."


class Decorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component

    def delete_user(self) -> str:
        return self._component.delete_user()


class AdminDecorator(Decorator):
    def __init__(self, component: Component, user: User) -> None:
        super().__init__(component)
        self.user = user

    def delete_user(self) -> str:
        if self.user.role != 'admin':
            raise PermissionError(f"Доступ запрещен: '{self.user.username}' не является администратором.")
        return f"{self.user.username} выполнил удаление. {self._component.delete_user()}"


def delete_user(user: User, user_id: int) -> None:
    component = DeleteUserComponent(user_id)
    protected = AdminDecorator(component, user)
    print(protected.delete_user())


if __name__ == "__main__":
    user1 = User("Sonya", "user")
    print(f"Текущий пользователь: {user1.username} ({user1.role})")
    try:
        delete_user(user1, 123)
    except PermissionError as e:
        print(f"Ошибка: {e}")
    print()

    user2 = User("admin_Alex", "admin")
    print(f"Текущий пользователь: {user2.username} ({user2.role})")
    try:
        delete_user(user2, 435342455456)
    except PermissionError as e:
        print(f"Ошибка: {e}")
    print()

    user3 = User("moder_Bill", "moderator")
    print(f"Текущий пользователь: {user3.username} ({user3.role})")
    try:
        delete_user(user3, 789)
    except PermissionError as e:
        print(f"Ошибка: {e}")
    print()

