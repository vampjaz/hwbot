VERBOSE = True   ## prints out extra status messages

GATEWAY_VERSION = 6 ## api stuff

LIBRARY_VERSION = 0.1
LIBRARY_NAME = 'Dogecord'
LIBRARY_AUTHOR = '@LGA#1151'

ACTIVE_TOKEN = ''

USER_AGENT = "{} {} by {}".format(LIBRARY_NAME, LIBRARY_VERSION, LIBRARY_AUTHOR)

DEFAULT_RP = 'with DogeCord.py'

# all the long URLs are stored here
GATEWAY_REQ_URL = "https://discordapp.com/api/v{}/gateway?encoding=json".format(GATEWAY_VERSION)
GATEWAY_MESSAGE_SEND = "https://discordapp.com/api/v{}/channels/{{}}/messages?encoding=json".format(GATEWAY_VERSION)