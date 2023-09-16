from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = "6412441114:AAF5nri-Vw1kcwvMn4JT4KzXH2Fjpxv3HHA"

# Create an Updater instance
updater = Updater(token=bot_token, use_context=True)

# Create a dispatcher to handle commands and messages
dispatcher = updater.dispatcher

# Function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Group Management Bot!")

# Function to handle the /add command (add user to group)
def add_member(update, context):
    user_id = update.message.reply_to_message.from_user.id
    context.bot.add_chat_member(update.effective_chat.id, user_id, can_send_messages=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Added {update.message.reply_to_message.from_user.first_name} to the group!")

# Function to handle the /remove command (remove user from group)
def remove_member(update, context):
    user_id = update.message.reply_to_message.from_user.id
    context.bot.kick_chat_member(update.effective_chat.id, user_id)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Removed {update.message.reply_to_message.from_user.first_name} from the group!")

# Function to handle the /promote command (promote user to admin)
def promote_admin(update, context):
    user_id = update.message.reply_to_message.from_user.id
    context.bot.promote_chat_member(update.effective_chat.id, user_id, can_change_info=True, can_delete_messages=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Promoted {update.message.reply_to_message.from_user.first_name} to admin!")

# Function to handle the /demote command (demote admin to user)
def demote_admin(update, context):
    user_id = update.message.reply_to_message.from_user.id
    context.bot.promote_chat_member(update.effective_chat.id, user_id, can_change_info=False, can_delete_messages=False)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Demoted {update.message.reply_to_message.from_user.first_name} to user!")

# Handlers for commands
start_handler = CommandHandler('start', start)
add_member_handler = CommandHandler('add', add_member)
remove_member_handler = CommandHandler('remove', remove_member)
promote_admin_handler = CommandHandler('promote', promote_admin)
demote_admin_handler = CommandHandler('demote', demote_admin)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(add_member_handler)
dispatcher.add_handler(remove_member_handler)
dispatcher.add_handler(promote_admin_handler)
dispatcher.add_handler(demote_admin_handler)

# Start the bot
updater.start_polling()

# Run the bot until you manually stop it (e.g., with Ctrl+C)
updater.idle()
