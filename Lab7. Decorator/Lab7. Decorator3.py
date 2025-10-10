class User:
    def __init__(self, username: str, role: str):
        self._username = username
        self._role = role

    @property
    def role(self):
        return self._role

    @property
    def username(self):
        return self._username


class Component:
    def __init__(self):
        self.delete = None

    def delete_user(self) -> str:
        pass


class DeleteUserComponent(Component):
    def __init__(self, user_id: int) -> None:
        super().__init__()
        self._user_id = user_id

    def delete_user(self) -> str:
        return f"Пользователь с ID {self._user_id} успешно удален!"


class Decorator(Component):
    def __init__(self, component: Component) -> None:
        super().__init__()
        self._component = component

    def delete_user(self) -> str:
        return self._component.delete_user()


class AdminDecorator(Decorator):
    def __init__(self, component: Component, user: User) -> None:
        super().__init__(component)
        self._user = user

    def delete_user(self) -> str:
        if self._user.role != "admin":
            raise PermissionError(f'Доступ запрещен! "{self._user.username}" не является администратором.')
        return f"{self._user.username} выполнил удаление. {self._component.delete.user()}"


def delete_user(user: User, user_id: int) -> None:
    component = DeleteUserComponent(user_id)
    protected = AdminDecorator(component, user)
    print(protected.delete_user())


if __name__ == "__main__":
    user1 = User('Sonya', 'admin')
    print(f"Текущий пользователь: {user1.username} его роль - '{user1.role}'")
    try:
        delete_user(user1, 1234)
    except PermissionError as e:
        print(f"Ошибка: {e}")
    print()