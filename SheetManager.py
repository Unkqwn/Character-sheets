import json
from pathlib import Path

presetFolder = Path(__file__).resolve().parent / "Presets"
preset = None

def CheckFolder():
    if presetFolder == None:
        print("No folder found, please check if you downloaded the presets along with this code.")
    else:
        if CheckForFiles(presetFolder):
            return True
        else:
            print("No files were found, please check if you downloaded the files in the folder.")
    return False

def CheckForFiles(folder):
    files = [f for f in folder.iterdir() if f.is_file()]
    return files

def ChoosePreset():
    return

def Main():
    if CheckFolder():
        print("Preset files were found.")
    return

if __name__ == "__main__":
    Main()