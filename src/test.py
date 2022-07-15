from observable import ObservableList

l = ObservableList()

l.add_change_listener(lambda action, item: print(action, item))

l.append(1)

l.append("two")

l.append(500)
