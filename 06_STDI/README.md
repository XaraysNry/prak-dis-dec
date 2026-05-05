### <center>  Modul 6   </center>
### <center>  Distributed File System - HDFS   </center>
### <center>  Nama: Aditya Wisnu Naraya   </center>
---
0. Persyaratan Software  
    Untuk mengerjakan materi pada petunjuk ini, beberapa distribusi software diperlukan:  
    - JDK: versi 17 dan/atau 21. Jika akan mengkompilasi Apache Hadoop, gunakan versi17. JDK versi 17 digunakan untuk server, sedangkan untuk client bisa menggunakan JDK 17 atau 21.  
    - Apache Hadoop. Versi ini menggunakan versi 3.5.0 (rilis 2 April 2026).  
    - pdsh  
    - ssh  
    - sshd telah dijalankan. Pada sistem Artix Linux + dinit sebagai init system, jalankan menggunakan sudo dinitctl start sshd. Jika menggunakan systemd: sudo systemctl start ssh.
1. Unduh Apache Hadoop
    Ambil distribusi Apache Hadoop di https://hadoop.apache.org/releases.html
    ![images/1](images/1.png)

2. Instalasi Apache Hadoop  
    Ekstraksi file hasil download , setelah itu konfigurasikan env var PATH:

    ![alt text](images/2.png)
    ![images/3](images/3.png)
    ![images/4](images/4.png)
    Catatan: lokasi instalasi Apache Hadoop selanjutnya akan disebut dengan $HADOOP_HOME. Dalam kasus ini, $HADOOP_HOME berarti merujuk pada direktori $HOME/software/storage/hadoop
    ![images/5](images/5.png)

    Setiap akan menggunakan Apache Hadoop di suatu shell/terminal, source file tersebut
    ![images/7](images/7.png)

3. Instalasi pdsh  
    Kebanyakan distro Linux sudah mempunyai paket untuk pdsh. Pada Artix Linux, pdsh harus dikompilasi dari AUR menggunakan trizen. Jika menggunakan distro lain, sesuaikan dengan distro yang digunakan.
    ![alt text](images/9.png)

    Setelah selesai instalasi pdsh, program bisa dijalankan menggunakan binary executable pdsh:
    ![images/10](images/10.png)

    Jika Rcmd type selain ssh, atur env variable dengan (misal di Bash):  
    ![06_STDI/11.png ](images/11.png)

    Atur supaya ssh ke localhost tidak perlu login  

        $ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
        $ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
        $ chmod 0600 ~/.ssh/authorized_keys  

    ![06_STDI/images/12.png](images/12.png)
    ![06_STDI/images/13.png](images/13.png)

4. Konfigurasi Apache Hadoop

        nano ~/software/storage/hadoop/etc/hadoop/hdfs-site.xml 
    ![14](images/14.png)
    
        nano ~/software/storage/hadoop/etc/hadoop/core-site.xml 
    ![15](images/15.png)

        nano ~/software/storage/hadoop/etc/hadoop/mapred-site.xml 
    ![16](images/16.png)

        nano ~/software/storage/hadoop/etc/hadoop/yarn-site.xml
    ![17](images/17.png)

5. Format NameNode
    Proses ini dilakukan sekali saja. Jika dilakukan lagi, akan menghapus berbagai file yang telah diproses di HDFS.
    ![18](images/18.png)
    ![19](images/19.png)

6. Atur konfigurasi JAVA_HOME
    Edit file $HADOOP_HOME/etc/hadoop/hadoop-env.sh dengan mengisikan env var untuk JAVA_HOME sesuai dengan lokasi di komputer / server / node
    ![images/6](images/6.png)

7. Jalankan daemon untuk HDFS
    ![20](images/20.png)
    Pemantauan bisa dilakukan menggunakan Web
    ![21](images/21.png)

8. Selesai
    Jika sudah berhasil sampai pada posisi ini, berarti Hadoop dan HDFS siap digunakan. Berikut adalah contoh operasi file pada HDFS. Daftar lengkap dari perintah-perintah HDFS bisa dilihat di https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html
    ![22](images/22.png)
    ![23](images/23.png)
    Untuk menghentikan HDFS:
    ![24](images/24.png)

Tugas:  
    1. Buat direktori /user/<nama-user>/datasets di HDFS anda  
    2. Cari 3 file .csv di Internet dan kemudian copykan 3 file tersebut ke direktori yang baru saja anda buat pada tugas 1 di atas.  

Jawaban:  
    0. Start hdfs
    ![t1](images/t1.png)   
    1. Membuat Direktori di HDFS  
    ![alt text](images/t1b.png)  
    2. Siapkan 3 link file dataset CSV publik (dari repositori Seaborn). Jalankan perintah wget ini :  
    wget https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv  
    wget https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv  
    wget https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv  
    Kembali ke folder software/storage, lalu jalankan ini  
    ![    t2  ](images/t2.png)
    3. Salin File ke HDFS  
    Setelah ketiga file tersebut terunduh di WSL, lalu pindahkan (copy) file-file lokal tersebut ke dalam folder /user/hp/datasets di HDFS menggunakan perintah -put :
    ![t3](images/t3.png)  
    4. Verifikasi Hasilnya  
    Untuk memastikan bahwa ketiga file tersebut sudah benar-benar masuk dan tersimpan dengan aman di dalam HDFS, gunakan perintah -ls untuk melihat daftar isinya:
    ![t4](images/t4.png) 
    terminal tersebut menampilkan daftar ketiga file .csv tersebut di dalam direktori HDFS  
    5. Cek hasil di http://localhost:9870/explorer.html#/user/hp/datasets
    ![t5](images/t5.png)