from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import re

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the callback function for the /start command
def start(update, context):
    update.message.reply_text('Welcome to the Calculator Bot! Send me expressions like 3+2, 3*4, etc., and I will calculate the result for you.')

# Define the callback function for normal messages
def calculate(update, context):
    expression = update.message.text
    result = evaluate_expression(expression)
    update.message.reply_text(result)

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        # Using regular expression to extract numbers and operators
        numbers = re.findall(r'\d+', expression)
        operators = re.findall(r'[\+\-\*\/]', expression)

        result = float(numbers[0])
        for i in range(len(operators)):
            if operators[i] == '+':
                result += float(numbers[i+1])
            elif operators[i] == '-':
                result -= float(numbers[i+1])
            elif operators[i] == '*':
                result *= float(numbers[i+1])
            elif operators[i] == '/':
                result /= float(numbers[i+1])
        
        return str(result)
    except Exception as e:
        return "Error: {}".format(str(e))

# Define main function
def main():
    # Create the Updater and pass it your bot's token
    updater = Updater("7150044305:AAHwaCBBP798BwlEMoyZiXHKc0r6SqZLgqU", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Register the message handler to handle normal messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, calculate))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
