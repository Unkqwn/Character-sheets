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

characterFolder = Path(__file__).resolve().parent / "Characters"

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

def LoadFile(file: Path):
    """Load a JSON file and return its contents."""
    with file.open(encoding="utf-8") as f:
        return json.load(f)

def ChoosePreset(presets: list[Path]):
    """Display available presets and get user selection."""
    print(text["availablePresets"])

    for index, preset_file in enumerate(presets, start = 1):
        print(f"{index}. {preset_file.stem}")

    choice = input(text["choose"]).strip()

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

def ModifyAbilityScores(sheet_data: dict) -> dict:
    """Allow user to modify ability scores and automatically calculate modifiers."""
    abilities = sheet_data["Ability"]
    
    print(text["modifyAbilityScores"])
    
    for ability_name in abilities:
        current_score = abilities[ability_name]["score"]
        print(f"{ability_name} ({text['currentScore']}{current_score})")
        
        while True:
            prompt = text["enterNewScore"].format(current=current_score)
            new_score = input(prompt).strip()
             
            if not new_score:
                break
                
            score = int(new_score)
            if 1 <= score <= 20:
                abilities[ability_name]["score"] = score
                modifier = CalculateModifier(score)
                abilities[ability_name]["modifier"] = modifier
                output = text["scoreSet"].format(
                    ability = ability_name,
                    score = score,
                    modifier = modifier
                )
                print(output)
                break
            else:
                print(text["invalidScoreRange"])
    
    return sheet_data

def SaveNewSheet(sheet_data: dict, filename: str) -> bool:
    """Save the modified sheet as a new file."""
    try:
        file_path = characterFolder / f"{filename}.json"
        
        if file_path.exists():
            overwrite = input(f"\n'{filename}.json' already exists. Overwrite? (yes/no): ").strip().lower()
            if overwrite != "yes":
                print("File not saved.")
                return False
        
        with file_path.open("w", encoding="utf-8") as f:
            json.dump(sheet_data, f, indent=4)
        
        print(f"\n Character sheet saved as '{filename}.json'")
        return True
    except Exception as e:
        output = text["errorSaving"].format(error = e)
        print(output)
        return False

def CreateSheet(preset_file: Path):
    """Create a new character sheet based on a preset template."""
    sheet_data = LoadFile(preset_file)
    
    print(f"\nLoaded preset: {preset_file.stem}")
    
    sheet_data = ModifyAbilityScores(sheet_data)
    
    filename = input(text["characterSheetName"]).strip()
    
    if not filename:
        print(text["noFilename"]).strip()
    
    if not filename:
        print("No filename provided. Character sheet not created.")
        return
    
    SaveNewSheet(sheet_data, filename)

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

    CreateSheet(preset)
    return

if __name__ == "__main__":
    Main()