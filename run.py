import dist
import os

commands_dir = os.path.join(os.curdir, 'commands')
ignored_modules = ['base.py', '__init__.py']
for file in os.listdir(commands_dir):
    is_python_file = file.endswith('.py')
    if is_python_file and file not in ignored_modules:
        file_path = os.path.join(commands_dir, file)
        os.system(
            f'pyinstaller --onefile {file_path}'
        )
