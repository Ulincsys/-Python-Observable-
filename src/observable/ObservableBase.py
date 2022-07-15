
class ObservableBase:
    def __init__(self):
        self.observers = []

    def add_change_listener(self, observer):
        self.observers.append(observer)

    def change(self, action, args, kwargs):
        for observer in self.observers:
            observer(action, *args, **kwargs)
