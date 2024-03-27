from time import sleep
from instagram import InstagramBot as igb

INSTAGRAM_EMAIL = ''
INSTAGRAM_PASSWORD = ''
USERNAME = ''
ACCOUNT = f'https://www.instagram.com/{USERNAME}/'

def main():
    ig_bot = igb()
    ig_bot.follow(INSTAGRAM_EMAIL,INSTAGRAM_PASSWORD,ACCOUNT,20)


if __name__ == "__main__":
    main()