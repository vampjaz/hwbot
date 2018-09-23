## parses the messages from Discord and makes channel, guild, user lists and changes them if they are edited


class Server: #holds info about the server (singular, discord as a whole); holds guilds, channels, 
	my_id = None
	channels = {}
	guilds = {}

##TODO:
class Guild:
	pass

class Channel:
	pass

class User:
	pass

class Role:
	pass


def handle_mesg(mesg): # looks for messages from Discord about updates in guild/user status, updates the lists
	pass

def get_my_mention():
	return '<@{}>'.format(Server.my_id)  # maybe?