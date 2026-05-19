Modul 8 Arsitektur Microservices untuk Sistem Terdistribusi
Nama: Aditya Wisnu Naraya  
NIM : 235410069  
=====
0. Pengantar
Microservices adalah salah satu arsitektur yang banyak digunakan pada sistem
terdistribusi. Dengan menggunakan arsitektur ini, software terdiri atas frontend yang berisi
UI/UX dan merupakan titik interaksi antara pengguna dengan aplikasi. Sisi frontend tersebut
kemudian meminta layanan / services dari backend yang berupa service. Untuk saat ini,
kebanyakan service tersebut bisa dibuat menggunakan REST API, GraphQL, dan gRPC.
Praktik pada mata kuliah ini akan menggunakan REST API dengan pustaka FastAPI dan
SQLModel untuk ORM dari Python.
1. Prasyarat
Untuk mengerjakan materi pada pertemuan ini, berikut adalah beberapa prasyarat:
1. Software uv telah terinstall dan penggunaannya telah dipahami. Lihat ke
https://github.com/NEO-X-School/notes/blob/main/uv/00.md untuk panduan praktis.
2. Instalasi Python menggunakan uv - Python 3.14.4
![alt text](images/1.png)
![alt text](images/1a.png)
![alt text](images/1b.png)
![alt text](images/1c.png)
3. Install paket FastAPI dan SQLModel:
![alt text](images/2.png)
4. Install SQLite jika belum ada di OS yang digunakan:
wget https://www.sqlite.org/2026/sqlite-autoconf-3530100.tar.gz
5. Buat database:
![alt text](images/3.png)
2. Source Code
![alt text](images/4.png)
3. Menjalankan Source Code
![alt text](images/connect.png)
Untuk memeriksa, akses dari browser atau dari headless tool (curl atau wget):
![alt text](images/akhir.png)
4. Tugas
1. Buat satu tabel baru menggunakan SQLite, tabel berbeda dari yang ada pada
contoh. Tabel tersebut mempunyai 1 primary key dan setidaknya berisi data dengan
tipe INT, CHAR, VARCHAR, BOOLEAN, dan FLOAT.
![alt text](images/t1.png)
2. Isikan 5 data menggunakan script Python
![alt text](images/t2.png)
3. Buat RESTful API endpoint untuk menampilkan semua data yang telah diisikan.
![alt text](images/t3.png)
4. Tampilkan hasil RESTful API endpoint tersebut menggunakan curl.
![alt text](images/t4.png)