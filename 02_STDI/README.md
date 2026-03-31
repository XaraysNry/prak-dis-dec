# Modul 2: Komunikasi Antar Proses pada Sistem Terdistribusi
Nama:Aditya Wisnu Naraya<br>
Nim :235410069<br>
Kelas: Informatika-2<br>
Mata_kuliah: Sistem Terdistribusi dan Terdesentralisasi<br>

1. Tampilan task manager di windows
![task_manager](img/Task_manager.png)

2. Buat workspace dengan nama workspace-01. dengan menggunakan python versi 3.14.3

3. Buat _environment_, aktifkan environment
4. Instalasi paket-paket yang di perlukan
5. jalanlan source code (schema.py)
   ```
   strawberry dev schema
   ```
lalu akses melalu browser ke http://0.0.0.0:8000/graphql dan akan muncul UI untuk request GraphQL data dari server<br>

bagian kiri untuk menuliskan query dan kanan untuk menampilkan hasil query, tombol run di gunakan untuk menjalankan query<br>

6. Pada tempat yang tersedia (di sisi kiri), tuliskan query nya
   ```
   {
     books  {
       title
       author
     }
   }
   ```
7. klik tombol run. hasil di sebelah kanan


