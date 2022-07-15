from .ObservableBase import ObservableBase

class ObservableList(ObservableBase):
    def __init__(self):
        super(ObservableList, self).__init__()
        self.list = []

    def append(self, item):
        self.change("append", [item], {})
        self.list.append(item)
