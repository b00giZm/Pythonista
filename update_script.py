import editor
import sys

def main():
	print(sys.argv)
	if len(sys.argv) <= 1:
		print("No changes detected.")
		quit()
	
	editor.open_file(sys.argv[1])
	text_length = len(editor.get_text())
	editor.replace_text(0, text_length, sys.argv[2])
	
if __name__ == '__main__':
	main()
