PORT = 8081
HOST = "127.0.0.1"
CONCATENATE_RESPONSES = True #Соединять ли отозванные ответы от сервера?
CONCATENATE_RESPONSES_STRING = "\n\n" #Чем отозванные сообщения соединяются.
DESIRED_TOKENS = 150
CONTINUATION_QUERY = "(hey bing, I think we cut off, please continue as character, seamlessly, do not mention the connection issue)"
MARKUP_FIX = True #Фикс потерянных кавычек и звездочек при отзыве сообщения."
MARKUP_FIX = True #Фикс потерянных кавычек и звездочек при отзыве сообщения.
COOKIE_NAME = "cookies.json"
USER_MESSAGE_WORKAROUND = True #Отправка в чат сообщения ниже. Код работает по такому принципу: есть контекст (история чата), а есть сообщение юзера. Если True, то сообщением отправляется заглушка ниже, если False, то отправляется последнее сообщение в таверне - джейл/ответ бота/ответ пользователя.
USER_MESSAGE = "Respond to the text above." #Отправляемая заглушка
REDIRECT_PROXY = "https://mysteryman63453121-hope.hf.space/proxy/openai"
REDIRECT_API_KEY = ""
REDIRECT_API_MODEL = "gpt-3.5-turbo" # gpt-3.5-turbo / gpt-3.5-turbo-0301 / gpt-4 / gpt-4-0314 / gpt-4-32k
REDIRECT_COMMAND = "Make the text above use less pronouns. Keep asterisks and quotes, it's markup."
REDIRECT_TEMPERATURE = 0.9
REDIRECT_USE_CONTEXT = True
REDIRECT_CONTEXT_TOKENS = 4095
