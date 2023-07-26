import requests
import random
import telegram
from telegram.ext import Updater, CommandHandler, JobQueue

# Define la función que enviará una curiosidad al azar al canal
def enviar_curiosidad(context):
    # Obtiene una curiosidad al azar de Curiosidades.com
    response = requests.get('https://www.curiosidades.com/')
    curiosidades = response.text.split('<h2 class="entry-title"><a href="')[1:]
    curiosidad = random.choice(curiosidades).split('</a>')[0].split('">')[1]

    # Envía la curiosidad al canal
    context.bot.send_message(chat_id='1825376552', text=curiosidad)

# Define la función que se ejecuta al recibir el comando /start
def start(update, context):
    # Envía una curiosidad al azar al canal
    enviar_curiosidad(context)

    # Envía un mensaje de bienvenida
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! Soy un bot que te enviará curiosidades al azar de Curiosidades.com cada 15 segundos. Utiliza el comando /stop para detener las curiosidades.")

# Crea el bot y registra los comandos
updater = Updater(token='6381156021:AAEi3G2a0WIJunnIsn6XoRdh110IK_5hMJg', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

# Crea el job queue y registra la función de enviar curiosidades
job_queue = JobQueue()
job_queue.run_repeating(enviar_curiosidad, interval=15, first=0)

# Inicia el bot
updater.start_polling()






