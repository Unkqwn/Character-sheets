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

    characterbtn = ctk.CTkButton(
        file_frame,
        width=160,
        height=220
    )
    characterbtn.pack(padx=10, pady=10)
    return
        

if __name__ == "__main__":
    CreateWindow()