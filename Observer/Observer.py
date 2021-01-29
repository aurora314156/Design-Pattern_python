from abc import ABCMeta, abstractmethod

class Observer(metaclass = ABCMeta):
    """ Observer base class""" 
    def update(self, observable, object):
        pass