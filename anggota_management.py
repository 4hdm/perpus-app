# File: anggota_management.py

import tkinter as tk
from tkinter import ttk, messagebox
import re 
from perpustakaan import insert_anggota, get_all_anggota, update_anggota, delete_anggota, search_anggota

class AnggotaManagementFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        tk.Label(self, text="MANAJEMEN ANGGOTA (25 poin)", font=("Arial", 16, "bold")).pack(pady=10)
        self.create_input_form()
        self.create_search_area()
        self.create_treeview()
        self.refresh_treeview() # Memuat data saat frame dibuat

    def create_input_form(self):
        form_frame = tk.Frame(self); form_frame.pack(fill='x', padx=10, pady=10)
        fields = ["Kode Anggota", "Nama", "Alamat", "Telepon", "Email"]
        self.entries = {}
        for field in fields:
            row = tk.Frame(form_frame); row.pack(side="top", fill="x", padx=5, pady=2)
            tk.Label(row, text=field.ljust(15)).pack(side="left")
            entry = tk.Entry(row); entry.pack(side="right", expand=True, fill="x")
            self.entries[field] = entry
            
        btn_frame = tk.Frame(self); btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Tambah", command=self.add_anggota).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_anggota_data).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Hapus", command=self.delete_anggota_data).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear Form", command=self.clear_form).pack(side="left", padx=5)

    def create_search_area(self):
        search_frame = tk.Frame(self); search_frame.pack(fill='x', padx=10, pady=5)
        tk.Label(search_frame, text="Cari Nama/Kode:").pack(side="left")
        self.search_entry = tk.Entry(search_frame); self.search_entry.pack(side="left", expand=True, fill="x", padx=5)
        ttk.Button(search_frame, text="Cari", command=self.search_anggota_data).pack(side="left")
        ttk.Button(search_frame, text="Reset", command=self.refresh_treeview).pack(side="left", padx=5)

    def create_treeview(self):
        tree_frame = tk.Frame(self); 
        # Menggunakan expand=True agar Treeview mengisi sisa ruang
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        columns = ("Kode Anggota", "Nama", "Alamat", "Telepon", "Email")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
        
        # Penyesuaian lebar kolom
        self.tree.column("Kode Anggota", width=100, anchor='center')
        self.tree.column("Nama", width=150, anchor='w')
        self.tree.column("Alamat", width=180, anchor='w')
        self.tree.column("Telepon", width=100, anchor='center')
        self.tree.column("Email", width=180, anchor='w')
        
        for col in columns:
            self.tree.heading(col, text=col)
            
        self.tree.pack(side="left", fill="both", expand=True) # expand=True untuk responsif
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview); vsb.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.bind('<<TreeviewSelect>>', self.load_selected_anggota)

    def validate_input(self, data):
        kode, nama, alamat, telepon_str, email = data
        if any(not val for val in data): return False, "Semua field harus diisi."
        try: int(telepon_str)
        except ValueError: return False, "Telepon harus angka."
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.fullmatch(email_regex, email): return False, "Format Email tidak valid."
        return True, ""

    def get_form_data(self):
        return (self.entries["Kode Anggota"].get(), self.entries["Nama"].get(), self.entries["Alamat"].get(), 
                self.entries["Telepon"].get(), self.entries["Email"].get())

    def clear_form(self):
        for entry in self.entries.values(): entry.delete(0, tk.END)
        self.entries["Kode Anggota"].config(state='normal'); self.tree.selection_remove(self.tree.selection())

    def add_anggota(self):
        data = self.get_form_data(); valid, msg = self.validate_input(data)
        if not valid: messagebox.showerror("Validasi Gagal", msg); return
        success, result_msg = insert_anggota(data)
        if success:
            messagebox.showinfo("Sukses", result_msg); self.clear_form(); self.refresh_treeview()
        else: messagebox.showerror("Gagal", result_msg)

    def load_selected_anggota(self, event):
        selected_item = self.tree.focus();
        if not selected_item: return
        values = self.tree.item(selected_item, 'values');
        if not values: return
        self.clear_form()
        fields = ["Kode Anggota", "Nama", "Alamat", "Telepon", "Email"]
        for i, field in enumerate(fields): self.entries[field].insert(0, values[i])
        self.entries["Kode Anggota"].config(state='disabled') 

    def update_anggota_data(self):
        # Format data: (nama, alamat, telepon, email)
        data_list = list(self.get_form_data()); valid, msg = self.validate_input(data_list)
        if not valid: messagebox.showerror("Validasi Gagal", msg); return
        kode_anggota = data_list.pop(0); data_list.append(kode_anggota) # Memindahkan kode_anggota ke akhir
        success, result_msg = update_anggota(tuple(data_list))
        if success:
            messagebox.showinfo("Sukses", result_msg); self.clear_form(); self.refresh_treeview()
        else: messagebox.showerror("Gagal", result_msg)

    def delete_anggota_data(self):
        kode_anggota = self.entries["Kode Anggota"].get()
        if not kode_anggota: messagebox.showerror("Error", "Pilih anggota dari tabel untuk dihapus."); return
        confirm = messagebox.askyesno("Konfirmasi", f"Yakin ingin menghapus anggota dengan kode {kode_anggota}?")
        if confirm:
            success, result_msg = delete_anggota(kode_anggota)
            if success:
                messagebox.showinfo("Sukses", result_msg); self.clear_form(); self.refresh_treeview()
            else: messagebox.showerror("Gagal", result_msg)

    def refresh_treeview(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        data = get_all_anggota()
        for row in data: self.tree.insert('', tk.END, values=row)

    def search_anggota_data(self):
        keyword = self.search_entry.get()
        if not keyword: self.refresh_treeview(); return
        data = search_anggota(keyword)
        for item in self.tree.get_children(): self.tree.delete(item)
        for row in data: self.tree.insert('', tk.END, values=row)