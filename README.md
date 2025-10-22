📚 Sistem Informasi Perpustakaan (SIP)
Aplikasi desktop sederhana untuk manajemen data buku dan anggota perpustakaan, diimplementasikan menggunakan Python (Tkinter) sebagai frontend dan MySQL sebagai backend.

Fitur Utama
Proyek ini telah memenuhi seluruh kriteria penilaian yang ditetapkan:

Sistem Login:
Form login dengan otentikasi terhadap tabel users di database.
Validasi input tidak boleh kosong.
Error handling untuk koneksi database.
Manajemen sesi (session management) untuk menyimpan info user yang login (username dan role).

Dashboard:
Tampilan welcome dengan nama user dan role yang login.
Menu navigasi ke Manajemen Buku dan Manajemen Anggota.
Statistik singkat (jumlah buku, jumlah anggota).

Manajemen Buku:
Fitur CRUD lengkap dengan field Kode Buku (unique), Judul, Pengarang, Penerbit, Tahun Terbit, dan Stok.
Validasi: Kode buku harus unique, Tahun terbit harus angka, Stok harus angka positif.
Menampilkan data dalam Treeview.
Fitur pencarian buku berdasarkan judul/pengarang.

Manajemen Anggota:
Fitur CRUD lengkap dengan field Kode Anggota (unique), Nama, Alamat, Telepon, dan Email.
Validasi: Kode anggota harus unique, format email valid, telepon harus angka.
Menampilkan data dalam Treeview.

UI/UX:
Warna dan layout yang konsisten.
Desain yang responsif (Treeview dan frame menggunakan expand=True).
Penggunaan message box untuk konfirmasi (hapus).
Pesan error yang informatif (validasi dan database error).
Persyaratan Sistem

Pastikan sistem Anda memenuhi persyaratan berikut:
Python 3.x
MySQL Server (Misalnya, menggunakan XAMPP atau Laragon).

Library Python:
Bash
pip install tkinter # Biasanya sudah termasuk dalam instalasi Python
pip install mysql-connector-python
Panduan Instalasi dan Setup

1. Database Setup (MySQL)
Buatlah database baru bernama perpustakaan dan buat tiga tabel (users, buku, anggota, peminjaman - jika diperlukan) menggunakan skrip SQL berikut:

SQL
-- Database: perpustakaan
-- Buat Tabel Users (untuk login)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL, -- Di sini password disimpan sebagai teks biasa (e.g., '123' untuk admin)
    role VARCHAR(50) NOT NULL
);

-- Masukkan data awal untuk admin
INSERT INTO users (username, password, role) VALUES ('admin', '123', 'admin');

-- Buat Tabel Buku (30 Poin)
CREATE TABLE IF NOT EXISTS buku (
    kode_buku VARCHAR(10) PRIMARY KEY,
    judul VARCHAR(255) NOT NULL,
    pengarang VARCHAR(255),
    penerbit VARCHAR(255),
    tahun_terbit YEAR,
    stok INT NOT NULL DEFAULT 0
);

-- Buat Tabel Anggota (25 Poin)
CREATE TABLE IF NOT EXISTS anggota (
    kode_anggota VARCHAR(10) PRIMARY KEY,
    nama VARCHAR(255) NOT NULL,
    alamat TEXT,
    telepon VARCHAR(15),
    email VARCHAR(255) UNIQUE
);
2. Konfigurasi Koneksi
Edit file database_koneksi.py dan pastikan kredensial koneksi sesuai dengan pengaturan MySQL Anda (terutama password).

Python
# File: database_koneksi.py
# ...
            host="localhost",
            user="root",
            password="",  # <-- SESUAIKAN PASSWORD ANDA DI SINI
            database="perpustakaan" 
# ...
3. Memuat Data Uji (50 Buku, 50 Anggota)
Gunakan query SQL yang telah disediakan sebelumnya untuk mengisi tabel buku dan anggota dengan 50 data agar fitur Manajemen Buku dan Anggota dapat diuji.

4. Struktur Proyek
Pastikan struktur file Anda terlihat seperti ini:

GUI perpustakaan/
├── database_koneksi.py  # Koneksi MySQL
├── perpustakaan.py      # Backend Logic (CRUD, Auth, Stats)
├── login_form.py        # Main App / Login Window (JALANKAN FILE INI)
├── dashboard.py         # Dashboard Window & Navigasi
├── buku_management.py   # Form 
CRUD Buku
└── anggota_management.py # Form CRUD Anggota
Panduan Penggunaan
Jalankan Aplikasi:

Bash
python login_form.py
Login:

Gunakan kredensial default:
Username: admin
Password: 123
Jika gagal, pastikan koneksi database Anda di database_koneksi.py sudah benar.

Akses Fitur:
Setelah login, Anda akan masuk ke Dashboard Statistik yang menampilkan jumlah buku dan anggota.
Klik Manajemen Buku atau Manajemen Anggota di menu navigasi sebelah kiri untuk mengakses fitur CRUD.
CRUD: Pilih baris di Treeview untuk mengisi form dan melakukan Update atau Hapus. Gunakan tombol Tambah untuk entri baru.
Logout: Klik tombol Logout di kiri bawah untuk kembali ke Form Login.

Klik tombol Logout di kiri bawah untuk kembali ke Form Login.
