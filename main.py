## main file for HWbot


''' stuff to look up:
	- SMBios definitions and related info for each one (including mobile?)
		- everymac.com maybe
	- intel cpu info (uses image embed with the cpu logo)
		- main command - basic stuff
		- graphics command - more on the iGPU
		- package command - physical package size, socket, lithography, temperatures
		- search command for finding multiple results
	- nvidia web driver versions
		- can search by mac os version, build number, webdriver version, or latest
	- syd's macos archive
		- we'll see about web scraping to auto-populate
		- will show sha1 as well

'''


import dogecord
import config

dogecord.setup(config.BOT_TOKEN_SECRET)
dogecord.run()