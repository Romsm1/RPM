class GuardSystem:
    def __init__(self):
        self._enable = False

    def activate(self) -> str:
        self._enable = True
        return 'Охранная система активирована!'

    def deactivated(self) -> str:
        self._enable = False
        return 'Охранная система деактивирована!'

    def check(self) -> str:
        return 'Охранная система активна!' if self._enable else 'Охранная система неактивна!'


class CameraSystem:
    def __init__(self):
        self._enable = False
        self._recording = False

    def activate(self) -> str:
        self._enable = True
        return 'Система видеонаблюдения включена!'

    def recording(self) -> str:
        if self._enable:
            self._recording = True
            return 'Камера начала запись.'
        return 'Камера выключена. Невозможно начать запись!'

    def stop_recording(self) -> str:
        if self._recording:
            self._recording = False
            return 'Камера завершила запись.'
        return 'Камера уже завершила запись.'

    def deactivated(self) -> str:
        self._enable = False
        return 'Система видеонаблюдения выключена!'

    def check(self) -> str:
        if self._enable:
            return f'Камера включена. Запись: {"идет." if self._recording else "не идет."}'
        return 'Камера выключена.'


class AccesControl:
    def __init__(self):
        self._enable = False

    def activate(self) -> str:
        self._enable = True
        return 'Система контроля доступа включена!'

    def deactivated(self) -> str:
        self._enable = False
        return 'Система контроля доступа выключена!'

    def check(self) -> str:
        return 'Система контроля доступа активна!' if self._enable else 'Система контроля доступа неактивна!'


class AlarmSystem:
    def __init__(self):
        self._active = False

    def activate(self) -> str:
        self._active = True
        return 'Сигнализация активна!'

    def deactivated(self) -> str:
        self._active = False
        return 'Сигнализация неактивна!'

    def check(self) -> str:
        if self._active:
            return f'Сигнализация работает.'
        return 'Сигнализация не работает.'


class SecuritySystemFacade:
    def __init__(self) -> None:
        self._guard = GuardSystem()
        self._camera = CameraSystem()
        self._acces = AccesControl()
        self._alarm = AlarmSystem()

    def active_all(self) -> str:
        results = ['Происходит полная активация системы безопасности...',
                   self._guard.activate(),
                   self._camera.activate(),
                   self._camera.recording(),
                   self._acces.activate(),
                   self._alarm.activate(),
                   'Все системы безопасности активны!']
        return "\n".join(results)

    def deactivate_all(self) -> str:
        results = ['Происходит полная деактивация системы безопасности...',
                   self._guard.deactivated(),
                   self._camera.deactivated(),
                   self._camera.stop_recording(),
                   self._acces.deactivated(),
                   self._alarm.deactivated(),
                   'Все системы безопасности неактивны!']
        return "\n".join(results)

    def check_status(self) -> str:
        results = ['Происходит проверка состояния системы безопасности...',
                   self._guard.check(),
                   self._camera.check(),
                   self._acces.check(),
                   self._alarm.check(),
                   'Проверка состояния системы безопасности окончена!']
        return "\n".join(results)


if __name__ == "__main__":
    facade = SecuritySystemFacade()
    print(facade.check_status())
    print(facade.active_all())
    print(facade.check_status())
    print(facade.deactivate_all())

    print(facade.check_status())
