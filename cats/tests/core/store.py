class Store:

    instance = None
    __store = {}

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls,  *args, **kwargs)
        return cls.instance

    def set_item(self, name, elem):
        self.__store[name] = elem

    def get_item(self, name):
        return self.__store[name]
