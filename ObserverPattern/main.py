import time
from Account import Account
from User import User
from Sms_sender import Sms_sender
from Mail_sender import Mail_sender

def main():
    Rick = User("Rick", "8.8.2.5252", time.time())
    Rick2 = User("Rick", "8.9.1.17", time.time())
    account = Account()
    account.add_observer(Sms_sender())
    account.add_observer(Mail_sender())
    account.login(Rick)
    account.login(Rick2)

if __name__ == '__main__':
    main()