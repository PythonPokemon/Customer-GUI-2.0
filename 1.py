import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class VocabApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vokabel-App")
        self.root.geometry("800x600")

        self.vocab_label = ctk.CTkLabel(master=self.root, text="Vokabeln")
        self.vocab_label.pack()

        self.vocab_textbox = ctk.CTkTextbox(master=self.root)
        self.vocab_textbox.pack()

        self.add_button = ctk.CTkButton(master=self.root, text="Vokabel hinzufügen", command=self.add_vocab)
        self.add_button.pack()

    def add_vocab(self):
        # Öffnet ein neues Fenster, um Vokabeln hinzuzufügen
        add_window = ctk.CTk()
        add_window.title("Vokabel hinzufügen")
        add_window.geometry("400x200")

        word_label = ctk.CTkLabel(master=add_window, text="Vokabel:")
        word_label.pack()

        word_entry = ctk.CTkEntry(master=add_window)
        word_entry.pack()

        translation_label = ctk.CTkLabel(master=add_window, text="Übersetzung:")
        translation_label.pack()

        translation_entry = ctk.CTkEntry(master=add_window)
        translation_entry.pack()

        save_button = ctk.CTkButton(master=add_window, text="Speichern", command=lambda: self.save_vocab(add_window, word_entry.get(), translation_entry.get()))
        save_button.pack()

    def save_vocab(self, add_window, word, translation):
        # Speichert die Vokabel und schließt das Fenster
        self.vocab_textbox.insert(ctk.END, f"{word} - {translation}\n")
        add_window.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = VocabApp(root)
    root.mainloop()
