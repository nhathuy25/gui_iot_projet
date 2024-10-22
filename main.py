import tkinter as tk
import ttkbootstrap as tb

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

'''
    -- DATABASE TAB --
    Description: Tab for visualizing the database with the list of badges and its information.
    User can view, edit names or delete a badge from the database. The adding of a new badge is not possible by GUI.

    Author: Huy

    Last modified: 14/10/2024
'''
tk.Label(tab_database, text="Liste des badges:").grid(row=0, column=0, padx=10, pady=10)



root.mainloop()