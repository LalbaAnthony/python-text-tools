import tkinter as tk
from tkinter import ttk, messagebox


class pttView:
    def __init__(self, root):
        self.root = root
        self.root.title("Python text tools")
        self.root.geometry("600x700")

        # Case butons container
        case_buttons_row = tk.Frame(root, padx=10, pady=10)
        case_buttons_row.pack(fill=tk.X)

        # Case buttons
        self.sentence_case_button = tk.Button(case_buttons_row, text="Sentence case")
        self.sentence_case_button.pack(side=tk.LEFT, padx=5)
        self.lower_case_button = tk.Button(case_buttons_row, text="lower case")
        self.lower_case_button.pack(side=tk.LEFT, padx=5)
        self.upper_case_button = tk.Button(case_buttons_row, text="UPPER CASE")
        self.upper_case_button.pack(side=tk.LEFT, padx=5)
        self.alternating_case_button = tk.Button(case_buttons_row, text="aLtErNaTiNg CaSe")
        self.alternating_case_button.pack(side=tk.LEFT, padx=5)
        self.title_case_button = tk.Button(case_buttons_row, text="Title Case")
        self.title_case_button.pack(side=tk.LEFT, padx=5)
        self.inverse_case_button = tk.Button(case_buttons_row, text="InVeRsE CaSe")
        self.inverse_case_button.pack(side=tk.LEFT, padx=5)

        # Separator
        ttk.Separator(root, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10, pady=10)

        # Deduplicate buttons container
        deplucate_buttons_row = tk.Frame(root, padx=10, pady=10)
        deplucate_buttons_row.pack(fill=tk.X)

        # Deduplicate buttons
        self.deduplicate_button = tk.Button(deplucate_buttons_row, text="Deduplicate Words")
        self.deduplicate_button.pack(side=tk.LEFT, padx=5)
        self.deduplicate_lines_button = tk.Button(deplucate_buttons_row, text="Deduplicate Lines")
        self.deduplicate_lines_button.pack(side=tk.LEFT, padx=5)
        self.deduplicate_case_insensitive_button = tk.Button(deplucate_buttons_row, text="Deduplicate Words Case Insensitive")
        self.deduplicate_case_insensitive_button.pack(side=tk.LEFT, padx=5)
        self.deduplicate_lines_case_insensitive_button = tk.Button(deplucate_buttons_row, text="Deduplicate Lines Case Insensitive")
        self.deduplicate_lines_case_insensitive_button.pack(side=tk.LEFT, padx=5)

        # Separator
        ttk.Separator(root, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10, pady=10)

        # Order buttons container
        order_buttons_row = tk.Frame(root, padx=10, pady=10)
        order_buttons_row.pack(fill=tk.X)

        # Order buttons
        self.order_alphabetically_button = tk.Button(order_buttons_row, text="A, B, C")
        self.order_alphabetically_button.pack(side=tk.LEFT, padx=5)
        self.order_alphabetically_descending_button = tk.Button(order_buttons_row, text="C, B, A")
        self.order_alphabetically_descending_button.pack(side=tk.LEFT, padx=5)
        self.order_numerically_button = tk.Button(order_buttons_row, text="1, 2, 3")
        self.order_numerically_button.pack(side=tk.LEFT, padx=5)
        self.order_numerically_descending_button = tk.Button(order_buttons_row, text="3, 2, 1")
        self.order_numerically_descending_button.pack(side=tk.LEFT, padx=5)
        
        # Textarea Section
        tk.Label(root, text="", font=("Arial", 12)).pack(pady=5)
        self.textarea = tk.Text(root, height=25, width=60)
        self.textarea.pack(pady=5)

        # Clear button
        self.clear_button = tk.Button(root, text="Clear")
        self.clear_button.pack(pady=10)

    def get_textarea_value(self):
        return self.textarea.get("1.0", tk.END).strip()

    def set_textarea_value(self, text):
        self.textarea.delete("1.0", tk.END)
        self.textarea.insert(tk.END, text)

    def clear_textarea(self):
        self.textarea.delete("1.0", tk.END)

    def show_warning(self, message):
        messagebox.showwarning("Warning", message)
