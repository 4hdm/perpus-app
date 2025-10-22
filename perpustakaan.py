# File: perpustakaan.py (Backend Logic - NO GUI IMPORTS)

from database_koneksi import get_koneksi 
import mysql.connector 

# --- 1. SISTEM LOGIN (20 poin) ---
def otentikasi_user(username, password_input):
    if not username or not password_input:
        return {'sukses': False, 'pesan': 'Username dan password tidak boleh kosong.'}

    db = None
    try:
        db = get_koneksi()
        if db is None:
            return {'sukses': False, 'pesan': 'Gagal terhubung ke database. Cek server MySQL.'}

        cursor = db.cursor(dictionary=True) 
        query = "SELECT id, password, role FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user_data = cursor.fetchone() 
        
        if user_data:
            if user_data['password'] == password_input: 
                return {'sukses': True, 'user_id': user_data['id'], 'role': user_data['role']}
            else:
                return {'sukses': False, 'pesan': 'Password salah.'}
        else:
            return {'sukses': False, 'pesan': 'Username tidak ditemukan.'}

    except Exception as e:
        print(f"Error otentikasi: {e}")
        return {'sukses': False, 'pesan': 'Terjadi kesalahan internal.'}
    finally:
        if db and db.is_connected(): db.close()

# --- 2. DASHBOARD STATISTIK (15 poin) ---
def get_statistik():
    db = get_koneksi()
    stats = {"buku": "N/A", "anggota": "N/A"} 
    if db is None: return stats
    try:
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM buku")
        stats["buku"] = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM anggota")
        stats["anggota"] = cursor.fetchone()[0]
    except Exception as e:
        print(f"Error statistik: {e}")
    finally:
        if db and db.is_connected(): db.close()
    return stats

# --- 3. MANAJEMEN BUKU (30 poin) ---
def get_all_buku():
    db = get_koneksi()
    buku_list = []
    if db is None: return buku_list
    try:
        cursor = db.cursor()
        query = "SELECT kode_buku, judul, pengarang, penerbit, tahun_terbit, stok FROM buku ORDER BY judul"
        cursor.execute(query)
        buku_list = cursor.fetchall()
    except Exception as e: print(f"Error ambil buku: {e}")
    finally:
        if db and db.is_connected(): db.close()
    return buku_list

def search_buku(keyword):
    db = get_koneksi()
    buku_list = []
    if db is None: return buku_list
    try:
        cursor = db.cursor()
        keyword = f"%{keyword}%"
        query = "SELECT kode_buku, judul, pengarang, penerbit, tahun_terbit, stok FROM buku WHERE judul LIKE %s OR pengarang LIKE %s ORDER BY judul"
        cursor.execute(query, (keyword, keyword))
        buku_list = cursor.fetchall()
    except Exception as e: print(f"Error cari buku: {e}")
    finally:
        if db and db.is_connected(): db.close()
    return buku_list

def insert_buku(data):
    db = get_koneksi()
    if db is None: return False, "Koneksi database gagal."
    try:
        cursor = db.cursor()
        query = "INSERT INTO buku (kode_buku, judul, pengarang, penerbit, tahun_terbit, stok) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, data)
        db.commit()
        return True, "Buku berhasil ditambahkan."
    except mysql.connector.Error as err:
        if err.errno == 1062: 
             return False, "Kode Buku sudah ada (harus unique)."
        return False, f"Error: {err.msg}"
    except Exception as e:
        return False, f"Kesalahan internal: {e}"
    finally:
        if db and db.is_connected(): db.close()

def update_buku(data):
    db = get_koneksi()
    if db is None: return False, "Koneksi database gagal."
    try:
        cursor = db.cursor()
        query = "UPDATE buku SET judul=%s, pengarang=%s, penerbit=%s, tahun_terbit=%s, stok=%s WHERE kode_buku=%s"
        cursor.execute(query, data) 
        db.commit()
        if cursor.rowcount == 0:
            return False, "Kode Buku tidak ditemukan."
        return True, "Data buku berhasil diperbarui."
    except Exception as e:
        return False, f"Kesalahan internal: {e}"
    finally:
        if db and db.is_connected(): db.close()

def delete_buku(kode_buku):
    db = get_koneksi()
    if db is None: return False, "Koneksi database gagal."
    try:
        cursor = db.cursor()
        query = "DELETE FROM buku WHERE kode_buku = %s"
        cursor.execute(query, (kode_buku,))
        db.commit()
        if cursor.rowcount == 0:
            return False, "Kode Buku tidak ditemukan."
        return True, "Buku berhasil dihapus."
    except Exception as e:
        return False, f"Kesalahan internal: {e}"
    finally:
        if db and db.is_connected(): db.close()

# --- 4. MANAJEMEN ANGGOTA (25 poin) ---
def get_all_anggota():
    db = get_koneksi()
    anggota_list = []
    if db is None: return anggota_list
    
    try:
        cursor = db.cursor()
        query = "SELECT kode_anggota, nama, alamat, telepon, email FROM anggota ORDER BY nama"
        cursor.execute(query)
        anggota_list = cursor.fetchall()
    except Exception as e: print(f"Error mengambil data anggota: {e}")
    finally:
        if db and db.is_connected(): db.close()
    return anggota_list

def search_anggota(keyword):
    db = get_koneksi()
    anggota_list = []
    if db is None: return anggota_list
    
    try:
        cursor = db.cursor()
        keyword = f"%{keyword}%"
        query = "SELECT kode_anggota, nama, alamat, telepon, email FROM anggota WHERE nama LIKE %s OR kode_anggota LIKE %s ORDER BY nama"
        cursor.execute(query, (keyword, keyword))
        anggota_list = cursor.fetchall()
    except Exception as e: print(f"Error mencari anggota: {e}")
    finally:
        if db and db.is_connected(): db.close()
    return anggota_list

def insert_anggota(data):
    db = get_koneksi()
    if db is None: return False, "Koneksi database gagal."
    try:
        cursor = db.cursor()
        query = "INSERT INTO anggota (kode_anggota, nama, alamat, telepon, email) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, data)
        db.commit()
        return True, "Anggota berhasil ditambahkan."
    except mysql.connector.Error as err:
        if err.errno == 1062: 
             return False, "Kode Anggota atau Email sudah terdaftar (harus unique)."
        return False, f"Error: {err.msg}"
    except Exception as e:
        return False, f"Kesalahan internal: {e}"
    finally:
        if db and db.is_connected(): db.close()

def update_anggota(data):
    db = get_koneksi()
    if db is None: return False, "Koneksi database gagal."
    try:
        cursor = db.cursor()
        query = "UPDATE anggota SET nama=%s, alamat=%s, telepon=%s, email=%s WHERE kode_anggota=%s"
        cursor.execute(query, data)
        db.commit()
        if cursor.rowcount == 0:
            return False, "Kode Anggota tidak ditemukan."
        return True, "Data anggota berhasil diperbarui."
    except mysql.connector.Error as err:
        if err.errno == 1062: 
             return False, "Email sudah terdaftar untuk anggota lain."
        return False, f"Error: {err.msg}"
    except Exception as e:
        return False, f"Kesalahan internal: {e}"
    finally:
        if db and db.is_connected(): db.close()

def delete_anggota(kode_anggota):
    db = get_koneksi()
    if db is None: return False, "Koneksi database gagal."
    try:
        cursor = db.cursor()
        query = "DELETE FROM anggota WHERE kode_anggota = %s"
        cursor.execute(query, (kode_anggota,))
        db.commit()
        if cursor.rowcount == 0:
            return False, "Kode Anggota tidak ditemukan."
        return True, "Anggota berhasil dihapus."
    except Exception as e:
        return False, f"Kesalahan internal: {e}"
    finally:
        if db and db.is_connected(): db.close()