import json
from pathlib import Path

language = "en"

stringPath = (
    Path(__file__).resolve().parent
    / "Strings"
    / f"{language}.json"
)

with stringPath.open(encoding="utf-8") as file:
    text = json.load(file)

presetFolder = Path(__file__).resolve().parent / "Presets"
preset = None

def GetFiles(folder: Path):
    """Returns files within a given folder."""
    files = [f for f in folder.iterdir() if f.is_file()]
    return files

def CheckFolder(folder):
    if not folder.exists():
        print(text["noFolder"])
        return None
    
    files = GetFiles(folder)
    if not files:
        print(text["noFiles"])
        return None
    
    return files

def ChoosePreset(presets: list[Path]):
    """Placeholder for when I'll let the user select the preset."""
    print(text["availablePresets"])

    for index, preset_file in enumerate(presets, start = 1):
        print(f"{index}. {preset_file.stem}")

    print(text["choice"])

    choice = input("Choice: ").strip()

    return choice

def HandleChoice(choice, presets: list[Path]):
    if not choice.isdigit():
        print(text["invalidChoice"])
        return None

    index = int(choice) - 1

    if index < 0 or index >= len(presets):
        print(text["invalidChoice"])
        return None

    return presets[index]

def CreateSheet():
    pass

def CalculateModifier(score: int) -> int:
    return (score - 10) // 2

def Main():
    print(text["welcome"])

    presets = CheckFolder(presetFolder)
    if not presets:
        return

    preset = HandleChoice(ChoosePreset(presets), presets)
    if not preset:
        return

    print(preset.stem)
    return

if __name__ == "__main__":
    Main()