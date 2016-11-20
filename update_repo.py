import editor
import re
from urllib.parse import urlencode, quote
import webbrowser

key = "D9NB4MSC6J"

def main():
	if key == "":
		print("You need to fill out key with value from Working Copy settings.")
		quit()
		
	regex = r"\/Documents\/(.+)$"

	path = editor.get_path()
	matches = re.findall(regex, path)

	params = {
		"key"       : key,
		"x-success" : "pythonista://",
		"repo"      : "Pythonista",
		"command"   : "write",
		"path"      : matches[0],
		"text"      : editor.get_text()
	}

	url = "working-copy://x-callback-url/chain/?" + urlencode(params, quote_via=quote) + "&command=commit"
	print(url)
	webbrowser.open(url)

if __name__ == '__main__':
	main()

