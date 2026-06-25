import SheetMaker as SM
import customtkinter as ctk

app = ""

def CreateWindow(resizable: bool = True):
    '''Creates the window to show the characters'''
    global app
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()
    app.title("Character Sheet")
    app.geometry(f"1200x700")
    app.resizable(resizable, resizable)
    ShowFiles()
    app.mainloop()
    return

def ShowFiles():
    '''Gets the files and makes them visiable'''
    file_frame = ctk.CTkScrollableFrame(app, label_text="My Characters")
    file_frame.pack(fill="both", expand=True, padx=20, pady=20)

    character_files = SM.CheckFolder(SM.characterFolder)
    if not character_files:
        return

    columns = 3

    for index, character_file in enumerate(character_files):
        row = index // columns
        column = index % columns

        characterbtn = ctk.CTkButton(
            file_frame,
            text=character_file.stem,
            command=lambda file=character_file: OpenSheet(file),
            width=160,
            height=220
        )
        characterbtn.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    for column in range(columns):
        file_frame.grid_columnconfigure(column, weight=1)
    return
        
def OpenSheet(characterSheet):
    return

if __name__ == "__main__":
    CreateWindow()