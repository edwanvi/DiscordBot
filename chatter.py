# import chatterbot modules
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# List of chatbot objects
# This is a good idea, right guys?
# Right?
bots = []
# Create the bot, may CandyToast live on
candybot = ChatBot("CandyToast",
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
    # output_adapter="chatterbot.adapters.output.TerminalAdapter",
    database="./candy_toast.json",
    silence_performance_warning=True,
    filters="chatterbot.filters.RepetitiveResponseFilter"
)
bots.append(candybot)
# Discord API server bot
api_memer = ChatBot("Wumpus",
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
    # output_adapter="chatterbot.adapters.output.TerminalAdapter",
    database="./ratelimit.json",
    silence_performance_warning=True,
    filters="chatterbot.filters.RepetitiveResponseFilter"
)
bots.append(api_memer)
# TIIIIINY amount of training on english and spanish corpus
for bot in bots:
    # f = open(bot.database)
    # if f.read == "" or f.read == None:
    bot.set_trainer(ChatterBotCorpusTrainer)
    bot.train("chatterbot.corpus.english")
    print(bot.name + " was trained on the english corpus.")
    bot.train("chatterbot.corpus.spanish")
    print(bot.name + " was trained on the spanish corpus.")
        # f.close()
    # else:
        # f.close()

def talk_to_the_dead(message):
    try:
        bot_input = candybot.get_response(message)
        return bot_input
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        pass

def may_i_speak_to_the_wumpus(message):
    try:
        bot_input = api_memer.get_response(message)
        return bot_input
    except (KeyboardInterrupt, EOFError, SystemExit):
        pass
