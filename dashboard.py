# File: dashboard.py

import tkinter as tk
from perpustakaan import get_statistik
from buku_management import BukuManagementFrame 
from anggota_management import AnggotaManagementFrame 

class DashboardApp:
    def __init__(self, master, session_data):
        self.master = master
        self.session = session_data 
        self.master.geometry("800x600")
        self.master.title(f"Dashboard Perpustakaan - {self.session['username']}")
        self.create_widgets()
        
    def create_widgets(self):
        # Menu Navigasi (Kiri)
        menu_frame = tk.Frame(self.master, bg="#333", width=200); menu_frame.pack(side="left", fill="y")
        welcome_text = f"Welcome, {self.session['username']}\nRole: {self.session['role'].upper()}"
        tk.Label(menu_frame, text=welcome_text, bg="#333", fg="white", wraplength=180).pack(pady=20, padx=5)

        # Tombol Navigasi
        # Navigasi ke Dashboard
        tk.Button(menu_frame, text="Dashboard Statistik", command=lambda: self.show_content("Statistik")).pack(fill='x', padx=10, pady=5)
        # Navigasi ke Manajemen Buku
        tk.Button(menu_frame, text="Manajemen Buku", command=lambda: self.show_content("Buku")).pack(fill='x', padx=10, pady=5)
        # Navigasi ke Manajemen Anggota
        tk.Button(menu_frame, text="Manajemen Anggota", command=lambda: self.show_content("Anggota")).pack(fill='x', padx=10, pady=5)
        # Tombol Logout
        tk.Button(menu_frame, text="Logout", command=self.logout).pack(fill='x', padx=10, pady=20, side='bottom')

        # Frame Konten Utama (Kanan)
        self.content_frame = tk.Frame(self.master, bg="#f0f0f0"); self.content_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        self.show_content("Statistik")
        
    def show_content(self, section):
        for widget in self.content_frame.winfo_children(): widget.destroy()
        
        if section == "Statistik":
            tk.Label(self.content_frame, text="Halaman: Dashboard Statistik", font=("Arial", 14)).pack(pady=20)
            self.display_stats()
        elif section == "Buku":
            tk.Label(self.content_frame, text="Halaman: Manajemen Buku", font=("Arial", 14)).pack(pady=5)
            BukuManagementFrame(self.content_frame).pack(fill="both", expand=True) 
        elif section == "Anggota":
            tk.Label(self.content_frame, text="Halaman: Manajemen Anggota", font=("Arial", 14)).pack(pady=5)
            AnggotaManagementFrame(self.content_frame).pack(fill="both", expand=True) 
            
    def display_stats(self):
        # Statistik singkat
        stats = get_statistik()
        tk.Label(self.content_frame, text="STATISTIK PERPUSTAKAAN", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(self.content_frame, text=f"Jumlah Buku: {stats['buku']}", font=("Arial", 10)).pack(anchor='w', padx=20)
        tk.Label(self.content_frame, text=f"Jumlah Anggota: {stats['anggota']}", font=("Arial", 10)).pack(anchor='w', padx=20)

    def logout(self):
        # Menghancurkan jendela dashboard dan memanggil form login baru
        self.master.destroy()
        import tkinter as tk
        from login_form import LoginForm # Late Import untuk mencegah circular import
        root_login = tk.Tk()
        root_login.title("Login Sistem Perpustakaan")
        LoginForm(root_login)
        root_login.mainloop()