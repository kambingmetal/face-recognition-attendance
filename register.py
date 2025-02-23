import os
import cv2
import face_recognition
import csv
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

# Direktori penyimpanan wajah
faces_folder = "faces/"
csv_file = "faces_list.csv"
excel_file = "absensi.xlsx"

# Pastikan folder "faces" ada
os.makedirs(faces_folder, exist_ok=True)

def capture_face():
    # Buka kamera
    camera = cv2.VideoCapture(0)

    # Minta input nama melalui UI
    user_name = simpledialog.askstring("Input Nama", "Masukkan nama Anda:")
    if not user_name:
        messagebox.showerror("Error", "Nama tidak boleh kosong!")
        return

    # Hitung jumlah file agar nama file unik
    file_count = len(os.listdir(faces_folder))
    file_name = f"person{file_count + 1}.jpg"
    file_path = os.path.join(faces_folder, file_name)

    messagebox.showinfo("Instruksi", "Tekan 'Space' untuk capture, 'Q' untuk keluar.")

    while True:
        ret, frame = camera.read()
        cv2.imshow("Capture Wajah", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):  # Tekan Space untuk capture
            cv2.imwrite(file_path, frame)
            messagebox.showinfo("Berhasil", f"Wajah disimpan sebagai {file_name}")
            break
        elif key == ord('q'):  # Tekan Q untuk keluar
            messagebox.showwarning("Batal", "Proses dibatalkan")
            camera.release()
            cv2.destroyAllWindows()
            return

    # Tutup kamera
    camera.release()
    cv2.destroyAllWindows()

    # Simpan data ke CSV
    file_exists = os.path.exists(csv_file)
    with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["gambar", "nama"])  # Tulis header jika file belum ada
        writer.writerow([file_name, user_name])

    # Simpan ke Excel (absensi)
    tanggal = datetime.now().strftime("%Y-%m-%d")
    waktu = datetime.now().strftime("%H:%M:%S")

    if os.path.exists(excel_file):
        df = pd.read_excel(excel_file)
    else:
        df = pd.DataFrame(columns=["Nama", "Tanggal", "Waktu"])

    # Tambahkan data baru
    new_data = pd.DataFrame([[user_name, tanggal, waktu]], columns=["Nama", "Tanggal", "Waktu"])
    df = pd.concat([df, new_data], ignore_index=True)

    # Simpan kembali ke Excel
    df.to_excel(excel_file, index=False)
    messagebox.showinfo("Sukses", "Data berhasil dicatat di absensi.xlsx")

# Buat UI dengan Tkinter
root = tk.Tk()
root.title("Face Registration")
root.geometry("300x200")

label = tk.Label(root, text="Face Recognition System", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Capture Wajah", command=capture_face, font=("Arial", 12))
button.pack(pady=10)

root.mainloop()
