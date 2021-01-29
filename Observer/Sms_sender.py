from Observer import Observer

class Sms_sender(Observer):
    """ Sms sender"""
    def update(self, observable, object):
        print("[Sending message] \nHello {}, detected your account might be has login exception.\n \
              Last login information:\n \
              Login region: {}\n \
              Logion IP: {}\n \
              Login time: {}\n".format(object['name'], object['region'], object['IP'], object['time']))