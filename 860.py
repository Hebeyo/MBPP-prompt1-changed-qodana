def check_alphanumeric(string):
	import re
	regex = '[a-zA-z0-9]$'
	if(re.search(regex, string)):
		return ("Accept")
	else:
		return ("Discard")
