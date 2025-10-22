# File: buku_management.py

import tkinter as tk
from tkinter import ttk, messagebox
from perpustakaan import insert_buku, get_all_buku, update_buku, delete_buku, search_buku

class BukuManagementFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        tk.Label(self, text="MANAJEMEN BUKU (30 poin)", font=("Arial", 16, "bold")).pack(pady=10)
        self.create_input_form()
        self.create_search_area()
        self.create_treeview()
        self.refresh_treeview() # Memuat data saat frame dibuat

    def create_input_form(self):
        form_frame = tk.Frame(self); form_frame.pack(fill='x', padx=10, pady=10)
        fields = ["Kode Buku", "Judul", "Pengarang", "Penerbit", "Tahun Terbit", "Stok"]
        self.entries = {}
        for field in fields:
            row = tk.Frame(form_frame); row.pack(side="top", fill="x", padx=5, pady=2)
            tk.Label(row, text=field.ljust(15)).pack(side="left")
            entry = tk.Entry(row); entry.pack(side="right", expand=True, fill="x")
            self.entries[field] = entry
            
        btn_frame = tk.Frame(self); btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Tambah", command=self.add_buku).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_buku_data).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Hapus", command=self.delete_buku_data).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear Form", command=self.clear_form).pack(side="left", padx=5)

    def create_search_area(self):
        search_frame = tk.Frame(self); search_frame.pack(fill='x', padx=10, pady=5)
        tk.Label(search_frame, text="Cari Judul/Pengarang:").pack(side="left")
        self.search_entry = tk.Entry(search_frame); self.search_entry.pack(side="left", expand=True, fill="x", padx=5)
        ttk.Button(search_frame, text="Cari", command=self.search_buku_data).pack(side="left") 
        ttk.Button(search_frame, text="Reset", command=self.refresh_treeview).pack(side="left", padx=5)

    def create_treeview(self):
        tree_frame = tk.Frame(self); 
        # Menggunakan expand=True agar Treeview mengisi sisa ruang
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10) 
        
        columns = ("Kode Buku", "Judul", "Pengarang", "Penerbit", "Tahun Terbit", "Stok")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings')
        
        # Penyesuaian lebar kolom
        self.tree.column("Kode Buku", width=80, anchor='center')
        self.tree.column("Judul", width=180, anchor='w')
        self.tree.column("Pengarang", width=120, anchor='w')
        self.tree.column("Penerbit", width=120, anchor='w')
        self.tree.column("Tahun Terbit", width=90, anchor='center')
        self.tree.column("Stok", width=60, anchor='center')
        
        for col in columns:
            self.tree.heading(col, text=col)
            
        self.tree.pack(side="left", fill="both", expand=True) # expand=True untuk responsif
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview); vsb.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.bind('<<TreeviewSelect>>', self.load_selected_buku)

    def validate_input(self, data):
        kode, judul, pengarang, penerbit, tahun_str, stok_str = data
        if any(not val for val in data): return False, "Semua field harus diisi."
        try: int(tahun_str)
        except ValueError: return False, "Tahun Terbit harus angka."
        try:
            stok = int(stok_str)
            if stok < 0: return False, "Stok tidak boleh negatif."
        except ValueError: return False, "Stok harus angka."
        return True, ""

    def get_form_data(self):
        return (self.entries["Kode Buku"].get(), self.entries["Judul"].get(), self.entries["Pengarang"].get(), 
                self.entries["Penerbit"].get(), self.entries["Tahun Terbit"].get(), self.entries["Stok"].get())

    def clear_form(self):
        for entry in self.entries.values(): entry.delete(0, tk.END)
        self.entries["Kode Buku"].config(state='normal'); self.tree.selection_remove(self.tree.selection())

    def add_buku(self):
        data = self.get_form_data(); valid, msg = self.validate_input(data)
        if not valid: messagebox.showerror("Validasi Gagal", msg); return
        success, result_msg = insert_buku(data)
        if success:
            messagebox.showinfo("Sukses", result_msg); self.clear_form(); self.refresh_treeview()
        else: messagebox.showerror("Gagal", result_msg)

    def load_selected_buku(self, event):
        selected_item = self.tree.focus();
        if not selected_item: return
        values = self.tree.item(selected_item, 'values');
        if not values: return
        self.clear_form()
        fields = ["Kode Buku", "Judul", "Pengarang", "Penerbit", "Tahun Terbit", "Stok"]
        for i, field in enumerate(fields): self.entries[field].insert(0, values[i])
        self.entries["Kode Buku"].config(state='disabled') 

    def update_buku_data(self):
        # Format data: (judul, pengarang, penerbit, tahun, stok)
        data_list = list(self.get_form_data()); valid, msg = self.validate_input(data_list)
        if not valid: messagebox.showerror("Validasi Gagal", msg); return
        kode_buku = data_list.pop(0); data_list.append(kode_buku) # Memindahkan kode_buku ke akhir
        success, result_msg = update_buku(tuple(data_list))
        if success:
            messagebox.showinfo("Sukses", result_msg); self.clear_form(); self.refresh_treeview()
        else: messagebox.showerror("Gagal", result_msg)

    def delete_buku_data(self):
        kode_buku = self.entries["Kode Buku"].get()
        if not kode_buku: messagebox.showerror("Error", "Pilih buku dari tabel untuk dihapus."); return
        confirm = messagebox.askyesno("Konfirmasi", f"Yakin ingin menghapus buku dengan kode {kode_buku}?")
        if confirm:
            success, result_msg = delete_buku(kode_buku)
            if success:
                messagebox.showinfo("Sukses", result_msg); self.clear_form(); self.refresh_treeview()
            else: messagebox.showerror("Gagal", result_msg)

    def refresh_treeview(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        data = get_all_buku()
        for row in data: self.tree.insert('', tk.END, values=row)

    def search_buku_data(self):
        keyword = self.search_entry.get()
        if not keyword: self.refresh_treeview(); return
        data = search_buku(keyword)
        for item in self.tree.get_children(): self.tree.delete(item)
        for row in data: self.tree.insert('', tk.END, values=row)