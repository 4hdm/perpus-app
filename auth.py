# auth.py
import sqlite3

def otentikasi_user(username, password):
    # Validasi input kosong
    if not username or not password:
        return {'sukses': False, 'pesan': "Username dan Password tidak boleh kosong!"}

    try:
        # Koneksi ke database
        conn = sqlite3.connect('perpustakaan.db')
        cursor = conn.cursor()

        # Query untuk cek user
        cursor.execute("""
            SELECT id, username, role 
            FROM users 
            WHERE username=? AND password=?
        """, (username, password))
        
        user = cursor.fetchone()

        if user:
            return {
                'sukses': True,
                'user_id': user[0],
                'role': user[2],
                'pesan': "Login berhasil!"
            }
        else:
            return {'sukses': False, 'pesan': "Username atau Password salah!"}

    except Exception as e:
        # Error handling koneksi database
        return {'sukses': False, 'pesan': f"Error database: {e}"}

    finally:
        try:
            conn.close()
        except:
            pass
