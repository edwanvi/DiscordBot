# import chatterbot modules
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# Create the bot, may CandyToast live on
bot = ChatBot("CandyToast",
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.adapters.output.TerminalAdapter",
    database="./database.json"
)
# TIIIIINY amount of training on english corpus
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")

print("Bot CandyToast is now ready for use.")

def talk_to_the_dead(message):
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(message)
        # print(bot_input)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        pass
