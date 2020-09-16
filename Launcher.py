from tkinter import *
import os

# These function 3 function are just one simple and same command and work for MacOs Users
# Remember you can use multiple command in one function
def open_gitHub():
    # This command can be use for opening a website in a different web browser than your default one
    os.system("open -a /Your_Path_For/WebBrowser.app/ 'https://github.com'")
    # If you want to open the website in your default web browser you can delete the "-a" and the path part


def open_file():
    # With the same command you can open a file in a different application than the default one with this command
    os.system("open -a /Your_Path_For/Visual_Studio_Code.app '/Your_Path_for/Launcher.py'" )
    # If you want to open the file in the default application you can delete the "-a" and the FIRST path part ( second path is the file you want to open )

def open_vsCode():
    # With the same command ( without "-a" and the second path because you don't need to choose something else ) you can open an application
    os.system("open  /Your_Path_For/Visual_Studio_Code.app" )

# Your windows
window = Tk()

# Specifications of the windows
window.title("- - GitHub Python Launcher - -")  # Title of the windows
window.geometry("1080x720")                     # Default size of the window
window.minsize(1080, 720)                       # Minimum size of the window
window.maxsize(1080, 720)                       # Maximum size of the window
window.config(background="#21618C")             # Background of the window

# Adding a Frame
frame = Frame(window, bg="#21618C")             # Add a frame
frame.pack(expand=YES)                          # Place the frame and make it staying in the middle if user resizes the window

# Adding text
label_title = Label(frame, text="Welcome to App Py Launcher ", font=("Times", 60), bg="#21618C", fg="white")    # Add a label in the frame
label_title.pack()                                                                                              # Place the label


# Adding Button

# Button 1
gitHub_button = Button(frame, text="Go to GitHub.com", font=("Times", 30), fg="black", command=open_gitHub)                 # Make a button that use the "open_gitHub()" function without the parenthesis
gitHub_button.pack(pady=10,fill=X)                                                                                          # Place the button

# Button 2
file_button = Button(frame, text="Open Launcher.py with VS CODE", font=("Times", 30), fg="black", command=open_file)        # Make a button that use the "open_file()" function without the parenthesis
file_button.pack(pady=10,fill=X)                                                                                            # Place the button

# Button 3
file_button = Button(frame, text="Open VS CODE", font=("Times", 30), fg="black", command=open_vsCode)                       # Make a button that use the "open_vsCode()" function without the parenthesis
file_button.pack(pady=10,fill=X)                                                                                            # Place the button

# Afficher
window.mainloop()       # Display the window
