# -*- coding: utf-8 -*-
from wxpy import *

api_key = "40ac7efefb6c44a79a682d3210122dcb"
bot = Bot()
tuling = Tuling(api_key=api_key)

my_group = ensure_one(bot.groups().search("学习交流群"))
my_friend = ensure_one(bot.friends().search("微信好友名"))

@bot.register(my_group)
def auto_replay_group(msg):
　　tuling.do_reply(msg)

@bot.register(my_friend)
def auto_replay_person(msg):
　　tuling.do_reply(msg)

bot.join()
