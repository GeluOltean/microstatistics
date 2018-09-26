A package for micropalaeontological statisics with a Qt5 gui. Also available on pip; launched with microstatistics-start.

# microStatistics

A Python 3 package for ecological, paleoecological and micropaleontological statistical indices with a Qt5 GUI. Available through pip, as [the package "microstatistics"]{https://pypi.org/project/microstatistics/}. For further information, please consult the following article: 

## Dependencies

The software has a number of dependencies, namely `PyQt5`, used for the interface, `xlrd` used to process the input files, as well as `pandas`, `scipy`, and `sklearn`.

## Installing

Installation is done through pip and launched using a script, `microstatistics-start`. See below for OS specific instructions. 

### GNU/Linux

Odds are your specific GNU/Linux distribution already has Python 3 installed, but does not include pip. Install Python 3 pip using your specific package manager, and then install microStatistics. On Ubuntu, this would be:

```
sudo apt install python3-pip
pip3 install microstatistics
```

Once installed, `microstatistics-start` will launch the software. An easy way to keep the program handy is to make a bash file, such as `microstatistics.sh`, containing just the launch command as one line, `microstatistics-start`, and making the file executable. 


### macOS

Please make sure you have Python 3  and pip installed from the official website, [https://www.python.org/downloads/mac-osx/]{https://www.python.org/downloads/mac-osx/}. Afterwards, using a terminal window, the install command is simply:

```
pip install microstatistics
```

Once installed, the terminal command `microstatistics-start` will launch the software. An easy way to keep the program handy is to make a bash file, such as `microstatistics.sh` containing just the launch command as one line, `microstatistics-start`, and making the file executable. 

### Windows

Please make sure you have Python 3 and pip installed from the official website, [https://www.python.org/downloads/windows/]{https://www.python.org/downloads/windows/}. Afterwards, open a powershell window and install the program using the following command:

```
pip install microstatistics
```

During installation, in the powershell window, a prompt will appear telling the user that scripts will not be available in powershell, as they are not included in the PATH, and provide a path string to where the `microstatistics-start` script is stored. 

Using said script, it is possible to create a shortcut to the script by creating a shortcut to powershell.exe and modifying the target to include the path to the startup script: 

```
powershell.exe -File "[REPLACE WITH YOUR PATH]\microstatistics-start.py"
```

Afterwards, the shortcut should launch the program. 

## License

This project is licensed under the GNU GPL3. See LICENSE.md file for additional details. 
