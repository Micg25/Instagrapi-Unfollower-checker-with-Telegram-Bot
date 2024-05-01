This bot has been realized with the "pyTelegramBotAPI" api and the "Instagrami" api. In order to make it work with your bot you must create a bot;
you can follow this tutorial to realize it: https://core.telegram.org/bots/tutorial

Once you made it you must create a telegram group and set it to PUBLIC, add your bot to this group but before doing it: 1. go to BotFather  2. write the "/setprivacy" command 3. choose your bot 4. set to DISABLE.
After adding the bot to your PUBLIC group give it administrator permission. 
(The program I wrote can't work on the bot chat itself because this can't interact with the pinned message of the chat which we will need to store our followers and compare them)

Now you have your bot, your public group where the bot is added and it will run, the next step is to open the "instagrapi_login.py" and "Unfollower checker with telebot.py" codes and change the variables I pinned with comments with your own datas (for example you will need to change the: Username,passowrd strings with your owns, the bot token id with your own)
And you did it! Now just start the "Unfollower checker with telebot.py" code and it will work on your telegram.

NOTICE that this code only work with profiles that have limited followers, like less than a thousand I think, this happens because telegram messages have a characters limitation, BUT if you want to have a program like this that works with large amounts of followers, refers to my other repository
where I realized this same code but working with FILES, so there is no limitation in the amount of followers you can store. Here is the repository: https://github.com/Micg25/Instagrapi_unfollowers_checker 
Of course this is a starting point, this was a project I made for fun, you can refer to this and upgrade it! Hope this can be helpful to someone!  <3
