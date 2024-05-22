import csv
import os
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox
from tkinter import messagebox


class App:
    def __init__(self):
        self.csv_file = None
        self.mode = None
        self.app = ctk.CTk()
        ctk.set_default_color_theme("blue")
        ctk.set_appearance_mode("System")
        self.app.title("Invitation App")
        self.app.geometry("720x500+200+200")
        ctk.CTkLabel(self.app, text="").pack(pady=10)
        self.new_file_button = ctk.CTkButton(self.app, text="New File", command=self.new_file)
        self.new_file_button.pack(padx=10, pady=10)
        self.existing_file_button = ctk.CTkButton(self.app, text="Select File", command=self.existing_file)
        self.existing_file_button.pack(padx=10, pady=10)

    def new_file(self):
        self.csv_file = filedialog.asksaveasfilename(initialfile="Lista de Invitados", defaultextension=".csv", filetypes=(("CSV files", "*.csv"),("All files", "*.*")), title="Enter the file path or location to save the new CSV file")
        if self.csv_file:
            self.mode = 'w'
            # Disable buttons
            self.new_file_button.configure(state='disabled')
            self.existing_file_button.configure(state='disabled')
            
            ctk.CTkLabel(self.app, text="").pack(pady=10)

            self.next_button = ctk.CTkButton(self.app, text="Next", command=self.add_invitation, text_color="white", border_color="green", border_width=2)
            self.next_button.pack(padx=10, pady=10)

    def existing_file(self):
        self.csv_file = filedialog.askopenfilename(title="Select the existing CSV file")
        if self.csv_file:
            self.mode = 'a'
            # Disable buttons
            self.new_file_button.configure(state='disabled')
            self.existing_file_button.configure(state='disabled')

            ctk.CTkLabel(self.app, text="").pack(pady=10)

            self.next_button = ctk.CTkButton(self.app, text="Next", command=self.add_invitation, text_color="white", border_color="green", border_width=2)
            self.next_button.pack(padx=10, pady=10)

    def add_invitation(self):
        if self.csv_file:
            # Create a new window
            self.input_window = ctk.CTk()
            self.input_window.geometry("720x500+200+200")
            self.input_window.title("Input Invitation Information")


            # Create labels and text boxes
            name_label = ctk.CTkLabel(self.input_window, text="Name")
            self.name_entry = ctk.CTkEntry(self.input_window)
            people_per_invite_label = ctk.CTkLabel(self.input_window, text="People Per Invite")
            self.people_per_invite_entry = ctk.CTkEntry(self.input_window)
            number_of_invitations_label = ctk.CTkLabel(self.input_window, text="Number of Invitations")
            self.number_of_invitations_entry = ctk.CTkEntry(self.input_window)
            invite_name_label = ctk.CTkLabel(self.input_window, text="Invite Name")
            self.invite_name_entry = ctk.CTkEntry(self.input_window)
            location_to_send_label = ctk.CTkLabel(self.input_window, text="Location to Send")
            self.location_to_send_entry = ctk.CTkEntry(self.input_window)

            # Create a label for the notes textbox
            notes_label = ctk.CTkLabel(self.input_window, text="Notes")

            # Create a large textbox for notes
            self.notes_textbox = ctk.CTkTextbox(self.input_window, width=300, height=100, corner_radius=1)

            # Pack labels and text boxes
            name_label.pack()
            self.name_entry.pack()
            people_per_invite_label.pack()
            self.people_per_invite_entry.pack()
            number_of_invitations_label.pack()
            self.number_of_invitations_entry.pack()
            invite_name_label.pack()
            self.invite_name_entry.pack()
            location_to_send_label.pack()
            self.location_to_send_entry.pack()
            # Pack the label and textbox
            notes_label.pack()
            self.notes_textbox.pack()

            ctk.CTkLabel(self.input_window, text="").pack(pady=1)

            # Create a submit button
            submit_button = ctk.CTkButton(self.input_window, text="Submit", command=lambda: self.write_to_file(self.name_entry.get(), self.people_per_invite_entry.get(), self.number_of_invitations_entry.get(), self.invite_name_entry.get(), self.location_to_send_entry.get(),self.notes_textbox.get("1.0", "end-1c")))
            submit_button.pack()

            # Start the input window's main loop
            self.input_window.mainloop()
        else:
            messagebox.showerror("Error", "No file selected")

    def write_to_file(self, name, people_per_invite, number_of_invitations, invite_name, location_to_send,notes):
        
        try:
            with open(self.csv_file, self.mode, newline='') as file:
                writer = csv.writer(file)
                if self.mode == 'w':
                    writer.writerow(["Name", "People Per Invite", "Number of Invitations", "Invite Name", "Location to Send", "Notes"])
                    self.mode = 'a'
                writer.writerow([name, people_per_invite, number_of_invitations, invite_name, location_to_send, notes])

            # Clear the entries
            self.name_entry.delete(0, 'end')
            self.people_per_invite_entry.delete(0, 'end')
            self.number_of_invitations_entry.delete(0, 'end')
            self.invite_name_entry.delete(0, 'end')
            self.location_to_send_entry.delete(0, 'end')
            self.notes_textbox.delete("1.0", "end")

        except PermissionError:
            messagebox.showerror("Error", "Permission denied. Please make sure the file is not open in another program and try again.")

        # Create a label with the submission message on input_window
        submission_message = ctk.CTkLabel(self.input_window, text="Info has been submitted.")
        submission_message.pack()

        # Schedule the label to be destroyed after 3 seconds
        self.input_window.after(2000, submission_message.destroy)


# Create an instance of the App class
app_instance = App()
app_instance.app.mainloop()
