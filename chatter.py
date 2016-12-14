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
admin_server = ChatBot("KenM",
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
    database="./admin.json",
    silence_performance_warning=True,
    filters="chatterbot.filters.RepetitiveResponseFilter"
)
bots.append(admin_server)

def talk_to_the_dead(message):
    bot_input = candybot.get_response(message)
    return bot_input

def may_i_speak_to_the_wumpus(message):
    bot_input = api_memer.get_response(message)
    return bot_input
def fname(arg):
    bot_input = admin_server.get_response(arg)
    return bot_input
