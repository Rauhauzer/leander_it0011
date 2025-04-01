import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

FILE_PATH = "records.csv"

def save_record(first, middle, last, birthday, gender):
    if not all([first, last, birthday, gender]):
        messagebox.showerror("Error", "All fields except Middle Name are required.")
        return
    
    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([first, middle, last, birthday, gender])
    messagebox.showinfo("Success", "Record saved successfully!")

def view_records():
    records_window = tk.Toplevel()
    records_window.title("View All Records")
    
    tree = ttk.Treeview(records_window, columns=("First Name", "Middle Name", "Last Name", "Birthday", "Gender"), show="headings")
    for col in tree['columns']:
        tree.heading(col, text=col)
    tree.pack(expand=True, fill="both")
    
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                tree.insert("", "end", values=row)

def search_record():
    def perform_search():
        query = search_entry.get().strip()
        if not query:
            messagebox.showerror("Error", "Please enter a name to search.")
            return
        
        results_window = tk.Toplevel()
        results_window.title("Search Results")
        tree = ttk.Treeview(results_window, columns=("First Name", "Middle Name", "Last Name", "Birthday", "Gender"), show="headings")
        for col in tree['columns']:
            tree.heading(col, text=col)
        tree.pack(expand=True, fill="both")
        
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if query.lower() in [field.lower() for field in row]:
                        tree.insert("", "end", values=row)
    
    search_window = tk.Toplevel()
    search_window.title("Search Record")
    tk.Label(search_window, text="Enter name to search:").pack()
    search_entry = tk.Entry(search_window)
    search_entry.pack()
    tk.Button(search_window, text="Search", command=perform_search).pack()

def signup_form():
    form_window = tk.Toplevel()
    form_window.title("Sign-up Form")
    
    labels = ["First Name:", "Middle Name:", "Last Name:", "Birthday (YYYY-MM-DD):", "Gender:"]
    entries = []
    for label in labels:
        tk.Label(form_window, text=label).pack()
        entry = tk.Entry(form_window)
        entry.pack()
        entries.append(entry)
    
    tk.Button(form_window, text="Submit", command=lambda: save_record(*[e.get() for e in entries])).pack()

def main():
    root = tk.Tk()
    root.title("User Management System")
    
    menu = tk.Menu(root)
    root.config(menu=menu)
    
    menu.add_command(label="Sign-up", command=signup_form)
    menu.add_command(label="View All Records", command=view_records)
    menu.add_command(label="Search a Record", command=search_record)
    menu.add_command(label="Exit", command=root.quit)
    
    root.mainloop()

if __name__ == "__main__":
    main()
