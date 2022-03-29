from instabot import Bot

COOKIE_FNAME = 'cookie.txt'

bot = Bot()
bot.login(username="wirexia66@gmail.com", password="reNcDjEgWp4X7Gt", use_cookie = False)
user_id = bot.get_user_id_from_username("lego")
user_info = bot.get_user_info(user_id)
print(user_info['biography'])