from instabot import Bot

bot = Bot()
bot.login(username="whoasuman", password="IamVinaya@13")
bot.follow('name_of_follow_person')

# Upload image withOut opening insta
bot.upload_photo("name/path of photu", caption="i love Pyhton")

# unfollowing a person
bot.unfollow("name_of_unfollow_person")

# send multiple people message
bot.send_message(", o.fc qhi,bq", ["username_1", "username_2"])

# View Details of instaAccount
followers = bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(follower))

# following list
following = bot.get_user_following("username")
for follow in following:
    print(bot.get_user_info(following))