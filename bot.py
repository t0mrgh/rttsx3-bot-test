from telegram.ext import Updater, CommandHandler, commandhandler, updater


def start(update, context):
    
    update.message.reply_text('fuck you!')
    

if __name__ == '__main__':
    
    updater = Updater(token='YOUR TOKEN', use_context=True) 
    dp = updater.dispatcher
    
    
    dp.add_handler(CommandHandler('start', start))
    
    updater.start_polling()
    updater.idle()    
    