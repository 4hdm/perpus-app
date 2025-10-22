# File: database_koneksi.py
import mysql.connector

def get_koneksi():
    """Membuat dan mengembalikan objek koneksi ke database 'perpustakaan'."""
    try:
        # Konfigurasi koneksi HARUS ADA DI DALAM FUNGSI INI
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Ganti jika user 'root' Anda memiliki password
            database="perpustakaan" # Sesuai dengan phpMyAdmin Anda
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error koneksi database: {err}")
        return None