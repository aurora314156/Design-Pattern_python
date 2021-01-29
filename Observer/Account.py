from Observable import Observable

class Account(Observable):
    """ User account"""
    def __init__(self):
        """
        @ param lastestIP: dict 
        @ param lastestRegion: dict
        """
        super().__init__()
        self.__lastestIP = {}
        self.__lastestRegion = {}

    def login(self, user):
        """
        Get current login location.
        If current login location is far away last time logion region, then trigger notify_observers().
        Otherwise, record region and IP information.
        """
        currentLoginRegion = self.__get_region(user.getIP())
        if self.__is_different_login_location(user.getName(), currentLoginRegion):
            self.notify_observers({"name": user.getName(), "IP": user.getIP(), "region": currentLoginRegion, "time": user.getTime()})

        self.__lastestRegion[user.getName()] = currentLoginRegion
        self.__lastestIP[user.getName()] = user.getIP()
        
    def __get_region(self, ip):
        """
        Get current login region.

        @ param ipRegions: record login location and ip address
        """
        ipRegions = {
            "8.8.8.5252": "Taiwan",
            "8.9.1.17": "My home"
        }
        currentLoginRegion = ipRegions.get(ip)
        return "" if currentLoginRegion is None else currentLoginRegion
        
    def __is_different_login_location(self, name, currentLoginRegion):
        """
        check current login region and last time login region. 
        """
        lastestRegion = self.__lastestRegion.get(name)
        return lastestRegion is not None and lastestRegion != currentLoginRegion