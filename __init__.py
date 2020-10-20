from instadm import InstaDM

if __name__ == '__main__':
    # Auto login
    insta = InstaDM(username='philipesko@yandex.ru', password='Zig44attack', headless=False)

    # Send message
    insta.sendMessage(user='sineokovamarina3', message='Hey !')