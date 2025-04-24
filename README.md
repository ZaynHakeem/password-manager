Password Manager

This is my final CS2 project

A simple Tkinter-based GUI application for generating and storing secure passwords. Users can generate random passwords, validate website and email/username inputs, and save credentials to a text file.
Features

Password Generation: Creates random passwords of 8–32 characters, ensuring at least one lowercase letter, one uppercase letter, one digit, and one special character from: #$%‘^,()*+.:|=@?@/][_{}!;~`.
Input Validation:
Website: Must contain a . (e.g., example.com or user@domain.com).
Email/Username: Must contain both @ and . (e.g., user@domain.com).
Password: Must be 8–32 characters and include at least two of: letter (upper or lowercase), number, or special character.


Storage: Saves credentials (website, email/username, password) to passwords.txt in a pipe-separated format.
User Interface: Clean Tkinter GUI with input fields, error messages, and buttons for generating passwords and adding entries.
Error Handling: Displays clear error messages for invalid inputs in red, with success messages in green.

Requirements

Python: Version 3.x (tested with Python 3.8+).
Tkinter: Included with standard Python installations. If not available, install it:
On Ubuntu/Debian: sudo apt-get install python3-tk
On macOS (with Homebrew): brew install python-tk


Image File: An images.png file must be present in the project root for the GUI logo. Replace it with your own PNG image if desired.

Installation

Clone the repository:
git clone https://github.com/ZaynHakeem/password-manager.git
cd password-manager

Ensure images.png is in the project root. If you don’t have this file, create a placeholder PNG or update the code to remove the image dependency:
Comment out these lines in password_manager.py

photo = PhotoImage(file="images.png")
image_label = Label(image=photo)
image_label.grid(row=0, column=1, columnspan=2)



Verify Python and Tkinter are installed:
python3 --version
python3 -c "import tkinter"

If Tkinter is missing, install it as noted in Requirements.


Usage

Run the application:python3 password_manager.py


The GUI will open with fields for Website, Email/Username, and Password.
Generate a Password:
Click the "Generate Password" button to populate the Password field with a random password meeting all requirements.


Add Credentials:
Enter a website (e.g., example.com or user@domain.com).
Enter an email/username (e.g., user@domain.com).
Use the generated password or type your own (must meet validation criteria).
Click the "Add" button to save the credentials to passwords.txt.


View Saved Credentials:
Open passwords.txt in the project root to see saved entries in the format: website | email/username | password.



File Structure

password_manager.py: Main Python script containing the Tkinter GUI and logic.
images.png: Image file displayed in the GUI (must be provided by the user).
passwords.txt: Output file where credentials are saved (created automatically).
README.md: This documentation file.

Example
Input

Website: user@domain.com
Email/Username: john@doe.com
Password: Ab1@xyz123 (generated or manual)
Action: Click "Add"

Output (in passwords.txt)
user@domain.com | john@doe.com | Ab1@xyz123

Invalid Input

Website: example (missing .)
Email/Username: user (missing @ or .)
Password: abc (too short or doesn’t meet category requirements)
Result: Error message in red (e.g., "Invalid website name.")

Notes

Image Dependency: If images.png is missing, the application will fail to load. Ensure it’s present or modify the code to remove the image.
Security: Passwords are stored in plain text in passwords.txt. For production use, consider encryption or a secure storage solution.
Validation: The email/username field requires both @ and ., treating it like an email. Modify add_password in password_manager.py if you want different rules.

Contributing

Fork the repository.
Create a new branch: git checkout -b feature-name.
Make changes and commit: git commit -m "Add feature".
Push to your fork: git push origin feature-name.
Open a pull request on GitHub.

License
This project is unlicensed. Feel free to use or modify it as needed.
For questions or suggestions, open an issue on the GitHub repository or contact [ZaynHakeem] on GitHub.
