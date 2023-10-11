1] Install PyInstaller:
	pip install pyinstaller
	
2] Navigate to Your Python Script
	Open your command prompt or terminal and navigate to the directory where your Python script is located.

3] Generate the .exe File
	Run the following command to generate the .exe file:
	pyinstaller --onefile hello_name.py  (for testing)
	pyinstaller --onefile main.py        (for actual program)

4] Locate the .exe File
	After PyInstaller finishes its process, you can find the .exe file in the dist directory within your project folder.

5] Note: I got some comments/warnings about adding a line to "main.spec" and subsequently running "pyinstaller --onefile main.spec". That eventually resulted in a .exe :-)
