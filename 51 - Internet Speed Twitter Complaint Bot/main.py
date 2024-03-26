
from time import sleep
from internetspeed import InternetSpeedTwitterBot as istb

PROMISED_DOWN = 3000
PROMISED_UP = 500
TWITTER_EMAIL = ''
TWITTER_PASSWORD = ''
TWITTER_INTERNET_PROVIDER = ''

def main():

    internet_bot = istb()
    real_down, real_up = internet_bot.get_internet_speed()

    if real_up < (PROMISED_UP * 0.50) or real_down < (PROMISED_DOWN * 0.50):
        message = f'Hey {TWITTER_INTERNET_PROVIDER}, why is my internet speed {real_down}down/{real_up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up'
        internet_bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD,message)


if __name__ == "__main__":
    main()
