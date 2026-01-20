import json
from pathlib import Path

presetFolder = Path(__file__).resolve().parent / "Presets"
preset = None

def GetFiles(folder: Path):
    """Returns files within a given folder."""
    files = [f for f in folder.iterdir() if f.is_file()]
    return files

def CheckFolder():
    if not presetFolder.exists():
        print("No folder found. Please check if you downloaded the presets along with this code.")
        return False
    
    files = GetFiles(presetFolder)
    if not files:
        print("No files were found in the folder. Please check if you downloaded the files along with the folder.")
        return False
    
    return True

def ChoosePreset():
    """Placeholder for when I'll let the user select the preset."""
    return

def Main():
    if CheckFolder():
        print("Preset files were found.")
    return

if __name__ == "__main__":
    Main()