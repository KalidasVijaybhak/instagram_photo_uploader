from instabot import Bot
import os,glob
try:
	os.remove("linux_genius_uuid_and_cookie.json")
except :
	pass

user_name = str(input("Username: "))
pass_name = str(input("Password: "))


caption = str(input("Caption: "))
bot = Bot();
bot.login(username = user_name, password = pass_name)
os.chdir("images")
for file in glob.glob("*.jpg"): 
	bot.upload_photo(file,caption=caption+"\n ")

bot.logout()
