import discord 
import os
import random 
import requests
import json 
import emoji
from deep_translator import GoogleTranslator
from sauvegarde import keep_alive
client = discord.Client()

#variable et constantes
sdb = "\n1) Pour avoir une citation qui  boost votre confiance:\ntapez\t"+emoji.emojize(':backhand_index_pointing_right:') +" \tinspire\n2) Sinon pour obtenir le rapport des reunions précédantes:\nEntrez\t " +emoji.emojize(':backhand_index_pointing_right:') + " \treunion "


sollicitations1 =  ["Salut", "Bonjour", "salut", "bonjour","Bonsoir", 
"slt", "bonsoir", "Coucou", "coucou", "Salut!", "salut!", "Bonjour!",
"Coucou!", "coucou!", "Bonsoir!", "bonsoir!" ]
reponses_possible = ["Bienvenue ! je m'appelle Elliot\nComment allez-Vous?",
"Je me nomme Elliot assistant au service de la team \nOn dit quoi? ", "Coucou! ici Elliot à votre service "+emoji.emojize(':smile:')]

sollicitations2 = ["Bien et", "super", "hamdoulilah", 
"oui", "Oui je vais", "oui", "Super", "bien", "bien et","çava", "Çava"
, "porte bien", "merveille", "pas mal", "pas mal ", "et toi", "rien", "Rien"]

reponses_admissible = ["C'est bien \t"+emoji.emojize(':thumbs_up:')+" \tde voir la bonne humeur!"+sdb, "Je suis ravis\t"+emoji.emojize(':smile:')+" \tde votre situation"+sdb, "J'aspire votre belle énérgie positive!"+sdb]

sollicitations3 = ["Comment", "comment", "allez"]
reponses_valables = ["je suis plein d'énérgie et vous ?", "j'admire votre enthousiasme!\n quoi de neuf?" ]

inspirations = ["inpire", "Inspire", "Inspire moi" ]

my_secret = os.environ['TOKEN']

#FONCTIONS   
def obtenir_citation():
  response = requests.get('https://zenquotes.io/api/random')
  data =  json.loads (response.text)
  quote = data[0]['q']
  traduction = GoogleTranslator(source='auto', target='fr').translate(quote)  
  quote = "\" "+traduction+" \" \n\t"+data[0]['a']
  return (quote)




@client.event 
async  def on_ready():
  print("Nous sommes connectes à {0.user}"
  .format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  
  msg = message.content
 

  if any( word in msg for word in sollicitations1):
    await message.channel.send(random.choice(reponses_possible))

  if any(word in msg for word in sollicitations2 ):
    await message.channel.send(random.choice(reponses_admissible))

  if any(word in msg for word in sollicitations3 ):
    await message.channel.send(random.choice(reponses_valables))

  
  if msg.startswith('inspire' ):
    quote = obtenir_citation()
    await message.channel.send(quote)

  
  
  if msg.startswith('reunion'):
    value = "\n\n**HISTORIQUE DE REUNION**\n"
    r1 = "reunion 1\n"
    await message.channel.send(value+r1+'https://drive.google.com/file/d/1QQdt-Xeo4MH_lHALlP6_zOlaFA4vikDd/view?usp=sharing')
keep_alive()
client.run(my_secret)

