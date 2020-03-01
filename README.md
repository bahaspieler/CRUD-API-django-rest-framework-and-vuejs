# CRUD API with Django Rest Framework & vue.js

Its a simple inventory app built with django rest framework and vue.js. The django api is hosted 
in Heroku and the vue app is hosted in the firebase. The links are given below.

[Django api](https://productstoreapi.herokuapp.com/api/products/)

[vuejs app](https://vuejsproduct.firebaseapp.com/) 

## Dependencies

`python3`

## Telegram-bot

Before running the telegrambot, do the below steps,

`pip install -r requirements.txt`

Now need to create a bot and get the api token. So do the below steps.

`open telegram`

`search for '@BotFather'`

`/start`

`/newbot`

`give a name`

`get the API token`

Now open the `telegrambot.py` file and edit the below line

`bot = telebot.TeleBot('token goes here')`

Finally run the bot.

`python telegrambot.py`

Search the bot in the telegram by the givenb name and type `/start`. Now 
you are good to go.
