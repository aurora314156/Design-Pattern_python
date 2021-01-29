from time import strftime, gmtime

class User(object):
    """ User base class"""
    def __init__(self, name, IP, login_time):
        """
        @ param name: str 
        @ param IP: str
        @ param time: timestamp
        """
        self.__name = name
        self.__IP = IP
        self.__time = strftime("%Y-%m-%d %H:%M %S", gmtime(login_time))
    def getName(self):
        return self.__name
    def getIP(self):
        return self.__IP
    def getTime(self):
        return self.__time