class Signleton:
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]


class ConfigCache(Signleton):
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._config = {}
            self._initialized = True

    def set(self, key, value):
        self._config[key] = value

    def get(self, key):
        return self._config.get(key)

    def get_all(self):
        return self._config


if __name__ == "__main__":
    cache = ConfigCache()
    cache.set('theme', 'dark')
    cache.set('volume', '0.8')
    cache.set('sensivity', '2.0')

    cache2 = ConfigCache()
    cache2.set('size', 'large')
    print(cache2.get('theme'))
    print(cache2.get('sensivity'))

    cache3 = ConfigCache()
    print(cache3.get('size'))

    print(cache is cache2 is cache3)
    print(id(cache))
    print(id(cache2))
    print(id(cache3))
