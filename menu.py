import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

def start_absen():
    try:
        python_path = sys.executable
        subprocess.Popen([python_path, 'classification.py'])
        messagebox.showinfo("Info", "Absensi dimulai, silakan hadapkan wajah ke kamera.")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menjalankan skrip: {e}")

def register_face():
    try:
        python_path = sys.executable
        subprocess.Popen([python_path, 'register.py'])
        messagebox.showinfo("Info", "Silakan masukkan nama dan capture wajah Anda.")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menjalankan skrip: {e}")

def close_app():
    exit()

# Inisialisasi UI
tk_root = tk.Tk()
tk_root.title("Sistem Absensi Wajah")
tk_root.geometry("300x200")

tk.Label(tk_root, text="Sistem Absensi Berbasis Wajah", font=("Arial", 12)).pack(pady=10)

# Tombol untuk mulai absensi
btn_absen = tk.Button(tk_root, text="Daftar", font=("Arial", 10), command=register_face)
btn_absen.pack(pady=10)

# Tombol untuk mulai absensi
btn_absen = tk.Button(tk_root, text="Mulai Absen", font=("Arial", 10), command=start_absen)
btn_absen.pack(pady=10)

# Tombol keluar
btn_keluar = tk.Button(tk_root, text="Keluar", font=("Arial", 10), command=close_app)
btn_keluar.pack(pady=10)

# Jalankan UI
tk_root.mainloop()
