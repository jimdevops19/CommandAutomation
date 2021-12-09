# CommandAutomation
This is a project that creates executables written with python in a directory that should be in PATH env variable

Libraries that you use needs to be installed on the System Interpreter that is used on your CLI (see the requirements.txt)


# Steps to get started (Use Terminal):

 - git clone this project
 - cd CommandAutomation
 - pip install -r requirements.txt
 - Put the dist directory in the PATH:
   - Use the `Windows Key + Pause` shortcut to open System Window
   - Click on Advanced System Settings
   - Find the Environment Variables
   - In System Section, add the full path of the dist directory
   - Save Changes
 - run `python run.py` to generate the executable files into the dist file.
 - Once done, close the terminal, and open it back again
 - Test if works by writing the command (hworld)
 - Now you can follow the pattern of [commands/hworld.py](commands/hworld.py) file
   - Simply copy and paste this file and create your own shortcuts
   - After each python file you write with this specific design, run `python run.py` to generate the executable file
 