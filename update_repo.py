from collections import OrderedDict
import editor
import re
import sys
from urllib.parse import urlencode, quote
import webbrowser

key = "D9NB4MSC6J"

def get_path():
	regex= r"\/Documents\/(.+)$"

	path = editor.get_path()
	matches = re.findall(regex, path)
	
	return matches[0]

def get_write_url():
	params = OrderedDict()
	
	params["key"]       = key
	params["x-success"] = "pythonista://"
	params["repo"]      = "Pythonista"
	params["path"]      = get_path()
	params["text"]      = editor.get_text()
	params["askcommit"] = 1

	return "working-copy://x-callback-url/write/?" + urlencode(params, quote_via=quote)
	
def get_read_url():
	params = OrderedDict()
	
	params["key"]       = key
	params["repo"]      = "Pythonista"
	params["path"]      = get_path()
	params["command"]   = "pull"
	params["command"]   = "read"
	params["x-success"] = "pythonista://update_script?action=run&argv={0}&argv=".format(get_path())

	return "working-copy://x-callback-url/chain/?" + urlencode(params, quote_via=quote)

def main():
	if key == "":
		print("You need to fill out key with value from Working Copy settings.")
		quit()
		
	url = get_write_url()
	if len(sys.argv) > 1 and sys.argv[1] == "read":
		url = get_read_url()
	
	webbrowser.open(url)

if __name__ == '__main__':
	main()

