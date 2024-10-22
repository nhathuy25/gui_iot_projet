import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import PhotoImage
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Dữ liệu mẫu cho danh sách badge
badges = [
    {"Nom": "Badge A", "ID": 1},
    {"Nom": "Badge B", "ID": 2},
    {"Nom": "Badge C", "ID": 3},
]

# Dữ liệu mẫu cho lịch sử truy cập
access_history = [
    {"ID": 1, "User": "Nguyễn Văn A", "Time": "2024-10-22 08:30", "Image": "image1.png"},
    {"ID": 2, "User": "Trần Thị B", "Time": "2024-10-22 09:00", "Image": "image2.png"},
    {"ID": 3, "User": "Lê Văn C", "Time": "2024-10-22 09:30", "Image": "image3.png"},
]

def delete_badge():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
        messagebox.showinfo("Suppression", "Badge supprimé avec succès.")
    else:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner un badge à supprimer.")

def edit_badge():
    selected_item = tree.selection()
    if selected_item:
        new_name = simpledialog.askstring("Édition", "Entrez le nouveau nom du badge:")
        if new_name:
            tree.item(selected_item, values=(new_name, tree.item(selected_item)["values"][1]))
            messagebox.showinfo("Édition", "Badge mis à jour avec succès.")
    else:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner un badge à éditer.")

root = tb.Window()
root.title("Gestion des badges")
root.geometry("800x600")
tabs = tb.Notebook(root)

# Tab for the database
tab_database = tb.Frame(tabs)
tabs.add(tab_database, text="Database")

# Tab for the history of access
tab_history = tb.Frame(tabs)
tabs.add(tab_history, text="Histoire d'accès")

# Packing 2 tabs
tabs.pack(expand=True, fill='both')

# Title label for badges
tk.Label(tab_database, text="Liste des badges:").grid(row=0, column=0, padx=10, pady=10)

# Create Treeview for displaying badges
tree = tb.Treeview(tab_database, columns=("Nom", "ID"), show="headings")
tree.heading("Nom", text="Nom")
tree.heading("ID", text="ID")

# Insert data into the Treeview for badges
for badge in badges:
    tree.insert("", "end", values=(badge["Nom"], badge["ID"]))

tree.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

# Create buttons for editing and deleting badges
button_frame = tb.Frame(tab_database)
button_frame.grid(row=2, column=0, padx=10, pady=10)

edit_button = tb.Button(button_frame, text="Modifier", command=edit_badge)
edit_button.pack(side=LEFT, padx=5)

delete_button = tb.Button(button_frame, text="Supprimer", command=delete_badge)
delete_button.pack(side=LEFT, padx=5)

# Configure grid weights
tab_database.grid_rowconfigure(1, weight=1)
tab_database.grid_columnconfigure(0, weight=1)

# -- Histoire d'accès Tab --
tk.Label(tab_history, text="Historique des accès:").grid(row=0, column=0, padx=10, pady=10)

# Create Treeview for displaying access history
access_tree = tb.Treeview(tab_history, columns=("ID", "User", "Time", "Image"), show="headings")
access_tree.heading("ID", text="ID")
access_tree.heading("User", text="Nom d'utilisateur")
access_tree.heading("Time", text="Temps d'accès")
access_tree.heading("Image", text="Image")

# Insert data into the Treeview for access history
for access in access_history:
    access_tree.insert("", "end", values=(access["ID"], access["User"], access["Time"], access["Image"]))

access_tree.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

# Configure grid weights for access history
tab_history.grid_rowconfigure(1, weight=1)
tab_history.grid_columnconfigure(0, weight=1)

root.mainloop()
