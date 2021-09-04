import yagmail as mail
from sys import argv

if len(argv) > 2:
    mailuser = argv[1]
    msg = argv[2]
    self = '{MAIL_HERE}@gmail.com'
    app_password = '{APP_PASSWORD_HERE}'
else:
    print("sassMailNotify.py [mail] [message]")

def start():
    subject = 'New command issued!'
    
    # Contains the body of the message sent to the mailbox.

    with mail.SMTP(self, app_password) as sendmail:
        try:
            sendmail.send(mailuser, subject, msg)
            print("Success")
        except:
            print("Error")

        
if __name__ == '__main__':
    start()
