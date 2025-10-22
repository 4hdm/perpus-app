# File: login_form.py

import tkinter as tk
from perpustakaan import otentikasi_user
from dashboard import DashboardApp # Impor DashboardApp di sini (hanya butuh 1 arah impor)

class LoginForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        tk.Label(self, text="SISTEM LOGIN PERPUSTAKAAN", font=("Arial", 16, "bold")).pack(pady=15)
        
        # Input Username
        tk.Label(self, text="Username:").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)
        
        # Input Password
        tk.Label(self, text="Password:").pack()
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=5)
        
        # Feedback Label
        self.feedback_label = tk.Label(self, text="", fg="black")
        self.feedback_label.pack(pady=10)
        
        # Tombol Login
        self.login_button = tk.Button(self, text="Login", command=self.handle_login)
        self.login_button.pack(pady=10)
        
        self.pack(padx=40, pady=40)

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Panggil fungsi otentikasi (meliputi validasi input dan koneksi database)
        hasil = otentikasi_user(username, password)
        
        if hasil['sukses']:
            self.feedback_label.config(text="Login Berhasil! Loading Dashboard...", fg="green")
            
            # Session Management Data
            user_session = {
                'id': hasil['user_id'],
                'username': username,
                'role': hasil['role']
            }
            
            # Navigasi ke Dashboard
            self.master.destroy() 
            root_dashboard = tk.Tk()
            from dashboard import DashboardApp # Pastikan import ini ada
            DashboardApp(root_dashboard, user_session)
            root_dashboard.mainloop()

        else:
            # Tampilkan pesan error otentikasi atau koneksi
            self.feedback_label.config(text=hasil['pesan'], fg="red")
            
# --- Main Execution ---
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Login Sistem Perpustakaan")
    LoginForm(root)
    root.mainloop()