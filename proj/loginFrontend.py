import PySimpleGUI as sg
import sqlite3
import subprocess  # Import the subprocess module

python_interpreter = r'C:\python_playground\project\proj\venv\Scripts\python.exe'
main_py_path = r'C:/python_playground/project/proj/main.py'

def login():
    # Define a default padding for elements in the form layout
    default_padding = (20, 30)  # Padding around each element (horizontal, vertical)

    # Application title definition
    appTitle = [
        # Row with the application title, centered
        [sg.Text(
            "SGLG Evaluation System",  # Title text
            font=("Times New Roman", 35),  # Font and size
            text_color='white',  # Text color
            justification='center',  # Center the text
            expand_x=True,  # Expand the width of the text element to fill the row
            pad=(0, 20)
        )]
    ]

    # Define the form layout with white background and black text
    form_layout = [
        # Row with username label and input field side by side
        [sg.Text("Username:", font=("Courier New", 12), text_color='black', background_color='white'),
         sg.InputText(key='-USERNAME-', font=("Courier New", 12), text_color='black', background_color='white')],
        # Row with password label and input field side by side
        [sg.Text("Password:", font=("Courier New", 12), text_color='black', background_color='white'),
         sg.InputText(key='-PASSWORD-', password_char='*', font=("Courier New", 12), text_color='black', background_color='white')],
        # Row with Login and Cancel buttons side by side
        [sg.Button("Login", font=("Courier New", 12), button_color=('white', '#546387'), pad=(0, 20)),
         sg.Button("Cancel", font=("Courier New", 12), button_color=('black', 'white'))]
    ]

    # Wrap the form layout in an sg.Column with default padding for each element
    column_layout = sg.Column(
        form_layout,
        element_justification='center',  # Align elements horizontally in the center
        vertical_alignment='center',  # Align elements vertically in the center
        background_color='#e8ad0c',
        pad=default_padding  # Apply default padding around each element
    )

    # Create a container (frame) with background color matching the form
    container = sg.Frame(
        title='',  # No title for the frame
        layout=[[column_layout]],  # Add the column layout inside the frame
        background_color='#e8ad0c',  # Background color of the container to match the form
        border_width=0  # Remove border for a cleaner look
    )

    # Define the main layout of the window
    layout = [
        [sg.VPush()],  # Vertical push for centering the container vertically in the window
        *appTitle,  # Include appTitle at the top of the layout
        [sg.Push(), container, sg.Push()],  # Center the container horizontally in the window
        [sg.VPush()]  # Vertical push for centering the container vertically in the window
    ]

    # Create the window with the specified layout
    window = sg.Window(
        "Login Form",
        layout,
        resizable=True,
        finalize=True
    )

    # Maximize the window to fill the entire screen
    window.maximize()

    # Event loop to process window events
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        if event == 'Login':
            username = values['-USERNAME-']
            password = values['-PASSWORD-']

            # Connect to SQLite database
            conn = sqlite3.connect('SGLG.db')  # Replace 'SGLG.db' with your database file
            cursor = conn.cursor()

            # Query the database for the username
            cursor.execute("SELECT Password, UId, provinceId, municipalityId FROM users WHERE UName=?", (username,))
            result = cursor.fetchone()

            # Close the database connection
            conn.close()

            if result is not None:
                # Retrieve password, pID, and mID from the query result
                password = result[0]
                UId = result[1]
                pID = result[2]
                mID = result[3]
                
                # Compare the entered password with the one from the database
                if password == values['-PASSWORD-']:
                    # Login successful, now you have pID and mID available for further use
                    print(f"UId: {UId}")
                    print(f"pID: {pID}")
                    print(f"mID: {mID}")
                    # Perform any necessary actions, such as launching `main.py` with these values
                    # For example:
                    command = f'"{python_interpreter}" "{main_py_path}" {UId} "{pID}" "{mID}"'
                    print()
                    subprocess.Popen(command, shell=True)
                    

                    sg.popup_auto_close("Successfully logged in!", auto_close_duration=5)
                    # Close the database connection
                    conn.close()
                    break
                else:
                    sg.popup("Invalid username or password!")
            else:
                sg.popup("Invalid username or password!")

    # Close the window
    window.close()

if __name__ == "__main__":
    login()
