import tkinter as tk
from tkinter import messagebox, simpledialog
from contact_logic import adding_cont, showing_cont, search_cont, delete_contact, update_cont

def add_contact_gui():
    adding_cont()

def show_contacts_gui():
    showing_cont()

def search_contact_gui():
    search_cont()

def delete_contact_gui():
    delete_contact()

def update_contact_gui():
    update_cont()

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("My Contact Book")
root.geometry("400x400")
root.config(bg="#e6f2ff")

label = tk.Label(root, text="📖 Contact Book", font=("Arial", 20, "bold"), bg="#e6f2ff")
label.pack(pady=20)

# Buttons
btn_add = tk.Button(root, text="➕ Add Contact", width=25, command=add_contact_gui)
btn_add.pack(pady=5)

btn_show = tk.Button(root, text="📋 Show Contacts", width=25, command=show_contacts_gui)
btn_show.pack(pady=5)

btn_search = tk.Button(root, text="🔍 Search Contact", width=25, command=search_contact_gui)
btn_search.pack(pady=5)

btn_delete = tk.Button(root, text="🗑️ Delete Contact", width=25, command=delete_contact_gui)
btn_delete.pack(pady=5)

btn_update = tk.Button(root, text="✏️ Update Contact", width=25, command=update_contact_gui)
btn_update.pack(pady=5)

btn_exit = tk.Button(root, text="❌ Exit", width=25, command=exit_app)
btn_exit.pack(pady=20)

root.mainloop()

