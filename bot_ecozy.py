from time import sleep

from instapy import InstaPy
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CM


session = InstaPy(username="philipesko8", password="Zig55attack", bypass_security_challenge_using='email')
session.login()
popeye_followers = session.grab_followers(username="philipesko8", amount="300", live_match=True, store_locally=True)
sleep(60)
print(popeye_followers)