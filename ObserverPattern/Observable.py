

class Observable(object):
    """ Observable base class"""
    def __init__(self):
        self.__observers = []
    def add_observer(self, observer):
        """ Add new observer"""
        self.__observers.append(observer)
    def remove_observer(self, observer):
        """ Remove observer"""
        self.__observers.remove(observer)
    def notify_observers(self, object = 0):
        """ Notify all observers """
        for o in self.__observers:
            o.update(self, object)