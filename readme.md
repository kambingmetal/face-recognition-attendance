# Sistem Absensi Wajah

Sistem ini menggunakan teknologi pengenalan wajah untuk melakukan absensi secara otomatis. Dibangun menggunakan Python dan pustaka seperti `OpenCV`, `face_recognition`, dan `Tkinter` untuk antarmuka pengguna.

## Persyaratan
Pastikan Anda telah menginstal dependensi yang diperlukan sebelum menjalankan sistem ini.

```sh
pip install opencv-python face-recognition numpy pandas openpyxl
```

## Struktur File
```
project-folder/
│── menu.py              # Antarmuka utama untuk memulai sistem
│── register.py          # Pendaftaran wajah pengguna
│── classification.py    # Pengenalan wajah untuk absensi
│── faces/               # Folder penyimpanan gambar wajah
│── faces_list.csv       # Data wajah pengguna
│── absensi.xlsx         # Catatan absensi dalam format Excel
```

## Cara Menggunakan

### 1. Menjalankan Sistem
Untuk memulai sistem, jalankan `menu.py`:
```sh
python menu.py
```
Akan muncul tampilan GUI dengan opsi:
- **Daftar**: Mendaftarkan wajah baru
- **Mulai Absen**: Melakukan absensi dengan pengenalan wajah
- **Keluar**: Menutup aplikasi

### 2. Pendaftaran Wajah
1. Klik tombol **Daftar** pada antarmuka.
2. Masukkan nama saat diminta.
3. Tekan **Spasi** untuk menangkap gambar wajah atau **Q** untuk membatalkan.
4. Wajah akan disimpan dan dicatat di `faces_list.csv`.

### 3. Melakukan Absensi
1. Klik tombol **Mulai Absen**.
2. Hadapkan wajah ke kamera.
3. Jika wajah dikenali, sistem akan mencatat waktu kehadiran ke `absensi.xlsx`.
4. Notifikasi akan muncul setelah absensi berhasil.

### 4. Keluar dari Sistem
- Tekan tombol **Keluar** pada menu utama atau tekan `Q` saat absensi berlangsung.

## Catatan Tambahan
- Gambar wajah disimpan di folder `faces/`.
- Data absensi disimpan dalam file `absensi.xlsx`.
- Sistem menggunakan `face_recognition` dengan tingkat kesesuaian 0.6.

## Kontributor
- **M. Yusuf Abdillah** - Pengembang
- **Kukuh Cito Angga Brilliant** - Pengembang
- **Muhammad Yunus Anshari** - Pengembang

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).

