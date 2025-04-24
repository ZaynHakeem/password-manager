from tkinter import *   
import random

root = Tk()

#Window title
root.title("Password Manager")

photo = PhotoImage(file="images.png")
image_label = Label(image=photo)
image_label.grid(row=0, column=1, columnspan=2)

error_label = Label(text="", fg="red")
error_label.grid(row=6, column=0, columnspan=6)

def generate_password():

    length = random.randint(8, 32)

    if length < 8 or length > 32:
        raise ValueError("Password length must be between 8 and 32 characters.")
    
    # Define the character sets to use
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "#$%‘^,()*+.:|=@?@/][_`{}\!;~"
    
    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password length with random choices from all sets
    all_characters = lower + upper + digits + symbols
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)
    
    output = ''.join(password)

    entry3.delete(0, END)  # Clear previous content
    entry3.insert(0, output)  # Insert new result
    error_label.config(text="")  # Clear error message
    

def add_password():
    website = entry1.get()
    username = entry2.get()
    password = entry3.get()

    if not website or not username or not password:
        error_label.config(text="Please fill in all fields.", fg="red")
        return
    
    if '.' not in website.lower():
        error_label.config(text="Invalid website name.", fg="red")
        return
    
    if '@' not in username or '.' not in username:
        error_label.config(text="Invalid email/username.", fg="red")
        return

    if len(password) < 8 or len(password) > 32:
        error_label.config(text="Password length must be between 8 and 32 characters.", fg="red")
        return
    
     # Define character sets for validation
    letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digits = set("0123456789")
    symbols = set("#$%‘^,()*+.:|=@?@/][_`{}\!;~")

    # Count which categories are present
    has_letter = any(c in letters for c in password)
    has_digit = any(c in digits for c in password)
    has_symbol = any(c in symbols for c in password)

    # Check if at least two categories are satisfied
    categories_met = sum([has_letter, has_digit, has_symbol])
    if categories_met < 2:
        error_label.config(text="Password must include at least two of the following:\nAt least one letter(upper or lower)\nAt least one number\nAt least one special character from: #$%‘^,()*+.:|=@?@/][_`{}\!;~.", fg="red")
        return

    with open('passwords.txt', 'a') as file:
        file.write(f"{website} | {username} | {password}\n")
    
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    error_label.config(text="Details added successfully!", fg="green")

Label1 = Label(text="Website:") 
Label2 = Label(text="Email/Username:")
Label3 = Label(text="Password:")
entry1 = Entry(width=35)
entry2 = Entry(width=35)
entry3 = Entry(width=21)
button1 = Button(text="Generate Password", command=generate_password)
button2 = Button(text="Add", width=30, command=add_password)

Label1.grid(row=2, column=0)
Label2.grid(row=3, column=0)
Label3.grid(row=4, column=0)
entry1.grid(row=2, column=2, columnspan=2)
entry2.grid(row=3, column=2, columnspan=2)
entry3.grid(row=4, column=2, columnspan=2)
button1.grid(row=4, column=4)
button2.grid(row=5, column=1, columnspan=2)

mainloop()