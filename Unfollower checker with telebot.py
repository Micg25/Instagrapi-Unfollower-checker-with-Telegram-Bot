from instagrapi import Client
import time
import Instagrapi_login as pl
import telebot

ACCOUNT_USERNAME=""
ACCOUNT_PASSWORD=""
cl = Client()
logger = pl.logging.getLogger()
pl.login_user(ACCOUNT_USERNAME, ACCOUNT_PASSWORD,cl,logger)

user_id=cl.user_id_from_username(ACCOUNT_USERNAME)  #Instead of ACCOUNT_USERNAME you can put any public profile username and check their follower/unfollower.
                                                    #If you want to track your own instagram account's unfollowers I suggest you to log in with a fake account 
                                                    #then put your own profile to public and run the code but change ACCOUNT_USERNAME to your own username
key="" #Put the key of your bot, given by BotFather
bot=telebot.TeleBot(key)
id=0   #Instead of Zero put the id of the chat you want the bot to work in
idme=0 #Instead of Zero put your own telegram ID, we will need it later so the bot will know that YOU are writing 
time.sleep(1)


unf=telebot.types.BotCommand("/unfollowers","It will print the list of your unfollowers on instagram")
bot.set_my_commands([unf])
infos=bot.get_chat(id)          #It gets the infos of our chat where the bot is working in, 
                                #we need it in order to get the info of the pinned message, wich is where we store the current follower list
bot.send_message(id,"STARTING...")

def unfollowers() :
 if infos.pinned_message is not None:  #check if there is a stored list of our followers
    users_id1=[]
    users_id2=[]
    strunf2=""
    fw=cl.user_followers(user_id, amount = 0)
    for user in fw:
        users_id2.append(user)
        strunf2=strunf2+user+"\n" #string that will store the newest follower in the pinned message

    
    users_id1=infos.pinned_message.text.split("\n") #it gets the ids of current follower by the pinned message and it stores them in the users_id1 list

    set1=set(users_id1) 
    set2=set(users_id2)   
    unfollowers= set1 - set2
    strunf="" 
    
    i=1
    if len(unfollowers) >0:
        bot.send_message(id, "Unfollowers were found...")
        for x in unfollowers:
            strunf= strunf + ("Unfollower Number "+ str(i)+" "+cl.username_from_user_id(x)+"\n")
            time.sleep(1)
            i+=1 
        bot.send_message(id, "Unfollowers list: \n" + strunf)
        messaget=bot.send_message(id,strunf2)
        bot.unpin_all_chat_messages(id)
        bot.pin_chat_message(id,messaget.id)
    elif set2!=set1: #if the set2 is not equal to set1 it means that there are new followers, so even in this case we update the follower list in the pinned message 
        bot.send_message(id,"New followers were found, Updating the list...")
        messaget=bot.send_message(id,strunf2)
        bot.unpin_all_chat_messages(id)
        bot.pin_chat_message(id,messaget.id)
 else: #if the pinned message is empty we calculate for the first time the list of the followers
    fw=cl.user_followers(user_id, amount = 0)
    users_id1=[]
    for user in fw:
        users_id1.append(user) 
    set1=set(users_id1)
    ris=""
    for x in set1:
        ris = ris + (str(x) + "\n")
    messagep=bot.send_message(id,ris)
    bot.pin_chat_message(id,messagep.id)
    bot.send_message(id,"Actual followers have been calculated, restart the bot in order to check if there are any new Unfollowers")

@bot.message_handler(commands=['unfollowers'])
def handle_test_command(message):
    sender_id = message.from_user.id
    if sender_id == idme:
        unfollowers()


bot.polling()