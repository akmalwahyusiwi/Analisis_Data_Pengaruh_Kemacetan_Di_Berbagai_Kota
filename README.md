# Analisis Faktor Kemacetan di Berbagai Kota di Indonesia

## Deskripsi

Proyek ini bertujuan untuk menganalisis faktor-faktor yang mempengaruhi tingkat kemacetan di beberapa kota di Indonesia. Data yang digunakan mencakup informasi demografi kota, infrastruktur jalan, dan transportasi publik.

## Struktur Proyek

1. `data/`: Direktori yang berisi file-file data CSV.
   - `faktor_infrasttruktu_transportasi.csv`: Data demografi kota.
   - `faktor_sosial_ekonomi.csv`: Data infrastruktur jalan.
   - `faktor_lingkungan_kepadatan.csv`: Data transportasi publik.

2. `analisis.ipynb`: Notebook Jupyter yang berisi analisis data menggunakan Python.

3. `README.md`: Dokumen ini, yang memberikan deskripsi proyek dan langkah-langkah untuk menjalankan analisis.

## Cara Menggunakan Data

Anda dapat menggunakan data yang disediakan dalam proyek ini untuk melakukan analisis sendiri atau menambahkan data tambahan untuk meningkatkan pemahaman tentang faktor-faktor yang mempengaruhi kemacetan di berbagai kota di Indonesia.

## Analisis Data

Notebook `analisis.ipynb` menyediakan langkah-langkah analisis data yang dilakukan menggunakan Python. Anda dapat menjalankan notebook tersebut untuk melihat hasil analisis lebih lanjut.

## Kontribusi

Kontribusi terhadap proyek ini sangat dipersilakan. Jika Anda ingin menambahkan data tambahan, memperbaiki kesalahan, atau menyumbangkan analisis tambahan, silakan lakukan langkah-langkah berikut:

1. Fork repositori ini.
2. Buat branch baru (`git checkout -b fitur-baru`).
3. Lakukan perubahan yang diinginkan.
4. Commit perubahan Anda (`git commit -am 'Menambahkan fitur baru'`).
5. Push ke branch (`git push origin fitur-baru`).
6. Buat pull request.

## Kontak

Jika Anda memiliki pertanyaan atau saran, jangan ragu untuk menghubungi kami melalui email: [contoh@email.com](mailto:contoh@email.com).

Terima kasih telah menggunakan data ini untuk analisis Anda!



FAKTOR INFRASTRUKTUR DAN TRANSPORTASI

Kota,Jumlah_Kendaraan (unit),Panjang_Jalan (km),Kualitas_Infrastruktur (skor),Penggunaan_Transportasi_Umum (%),Kemacetan (skor)
Jakarta,7500000,650,5,60,9
Surabaya,3000000,500,4,55,7
Bandung,2500000,400,3.5,50,8
Medan,2000000,300,4,45,6
Bekasi,1500000,200,3,40,7
Semarang,1200000,350,4,48,6
Palembang,1100000,250,3.5,42,5
Makassar,1000000,150,3,35,5
Denpasar,800000,100,4.5,55,4
Yogyakarta,600000,90,4,50,3
Tangerang,1300000,300,4.5,52,6
Bogor,800000,150,4,45,5
Depok,700000,120,3.8,47,6
Malang,950000,220,4,49,5
Balikpapan,500000,180,4.2,51,4
Pontianak,450000,140,3.9,40,4
Pekanbaru,600000,200,4.1,46,5
Batam,700000,250,3.7,44,6
Manado,350000,130,3.8,39,3
Padang,400000,150,4,42,4
Banjarmasin,500000,140,4,45,4
Solo,500000,140,4,53,4
Kediri,300000,80,3.7,39,3
Jambi,400000,120,4.1,44,4
Banda Aceh,350000,100,4,46,3
Palangkaraya,300000,80,3.8,40,3
Samarinda,500000,130,4,47,4
Kupang,250000,70,3.6,38,2
Jayapura,300000,90,3.9,41,3
Mataram,400000,110,4,44,4
Ambon,250000,80,3.7,39,3
Ternate,200000,60,3.5,37,2
Sorong,180000,50,3.6,36,2
Bengkulu,250000,80,3.8,40,3
Bandar Lampung,450000,140,4.1,48,5
Palu,300000,90,4,43,3
Kendari,250000,80,3.8,42,3
Tasikmalaya,350000,110,4,44,4
Cirebon,400000,130,4,46,4
Madiun,300000,90,3.8,40,3
Magelang,250000,70,3.7,38,3
Cimahi,600000,110,4.2,51,5
Pekalongan,300000,80,3.8,40,3
Tegal,300000,90,4,42,3
Blitar,250000,70,3.7,39,2
Probolinggo,300000,80,3.9,41,3
Pasuruan,350000,100,4,42,4
Banyuwangi,400000,120,4.1,44,4
Bontang,200000,60,3.7,38,2
Tanjung Pinang,180000,50,3.6,37,2
Pangkalan Bun,150000,40,3.5,36,2
Samarinda,500000,130,4,47,4
Manado,350000,130,3.8,39,3
Bitung,300000,100,4,43,3
Tomohon,250000,80,3.7,38,2
Gorontalo,300000,90,4,42,3
Toli-Toli,200000,60,3.5,37,2
Palu,300000,90,4,43,3
Bone,200000,60,3.6,37,2
Parepare,250000,80,3.8,40,3
Makassar,1000000,150,3,35,5
Sidenreng,180000,50,3.6,37,2
Kolaka,150000,40,3.5,36,2
Bau-Bau,200000,60,3.7,38,2
Tual,150000,40,3.5,36,2
Saumlaki,180000,50,3.6,37,2
Langgur,200000,60,3.7,38,2
Merauke,150000,40,3.5,36,2
Fakfak,180000,50,3.6,37,2
Manokwari,250000,70,3.8,40,3
Biak,200000,60,3.7,38,2
Sorong,180000,50,3.6,37,2
Raja Ampat,150000,40,3.5,36,2
Jayapura,300000,90,3.9,41,3

FAKTOR SOSIAL DAN EKONOMI

Kota,Pendapatan_Perkapita (juta Rp),Tingkat_Pengangguran (%),Kepadatan_Penduduk (orang/km2),Tingkat_Pendidikan (skor),Kemacetan (skor)
Jakarta,250,8,15000,4.5,9
Surabaya,200,7,12000,4.2,7
Bandung,180,6,14000,4,8
Medan,150,5,10000,4,6
Bekasi,160,6,8000,3.8,7
Semarang,170,5,11000,4.1,6
Palembang,140,5.5,9000,3.9,5
Makassar,130,6,7000,3.8,5
Denpasar,200,4.5,6000,4.2,4
Yogyakarta,180,4,5000,4.1,3
Tangerang,190,6,9500,4.2,6
Bogor,150,5,7000,4,5
Depok,170,5.5,8000,3.9,6
Malang,160,4.5,7500,4,5
Balikpapan,140,6,6800,4,4
Pontianak,130,5,6400,3.8,4
Pekanbaru,160,5,7000,4,5
Batam,180,6.5,8000,3.9,6
Manado,120,5,6000,3.7,3
Padang,130,4.5,6200,3.8,4
Banjarmasin,140,5,6800,4,4
Solo,150,5,7500,4.1,4
Kediri,110,6,6000,3.6,3
Jambi,130,5.5,6600,4,4
Banda Aceh,120,4,5900,3.9,3
Palangkaraya,100,5,5500,3.8,3
Samarinda,140,6,7000,4,4
Kupang,90,5.5,5200,3.6,2
Jayapura,110,5,5600,3.7,3
Mataram,100,4.5,6300,4,4
Ambon,90,5,5200,3.7,3
Ternate,80,6,4900,3.5,2
Sorong,70,5.5,4500,3.6,2
Bengkulu,100,5,5000,3.7,3
Bandar Lampung,130,6,6700,4.1,5
Palu,90,5,5800,4,3
Kendari,80,5.5,5200,3.8,3
Tasikmalaya,110,5,6000,4,4
Cirebon,120,5.5,6200,4,4
Madiun,100,6,5800,3.8,3
Magelang,90,5,5200,3.7,3
Cimahi,140,6.5,7500,4.2,5
Pekalongan,100,5.5,5800,3.8,3
Tegal,110,5,6000,4,3
Blitar,90,6,5200,3.7,2
Probolinggo,100,5,5500,3.9,3
Pasuruan,110,5.5,5800,4,4
Banyuwangi,120,6,6000,4.1,4
Bontang,70,5,4900,3.7,2
Tanjung Pinang,60,5.5,4500,3.6,2
Pangkalan Bun,50,6,4200,3.5,2
Samarinda,140,6,7000,4,4
Manado,120,5,6000,3.7,3
Bitung,90,5.5,5700,4,3
Tomohon,70,6,5000,3.7,2
Gorontalo,100,5,6000,4,3
Toli-Toli,50,5.5,4900,3.5,2
Palu,90,5,5800,4,3
Bone,70,6,4900,3.6,2
Parepare,80,5,5200,3.8,3
Makassar,130,6,7000,3.8,5
Sidenreng,60,5.5,4500,3.6,2
Kolaka,50,6,4200,3.5,2
Bau-Bau,70,5,4900,3.7,2
Tual,50,6,4200,3.5,2
Saumlaki,60,5.5,4500,3.6,2
Langgur,70,5,4900,3.7,2
Merauke,50,6,4200,3.5,2
Fakfak,60,5.5,4500,3.6,2
Manokwari,80,5,5200,3.8,3
Biak,70,5.5,4900,3.7,2
Sorong,60,5,4500,3.6,2
Raja Ampat,50,6,4200,3.5,2
Jayapura,110,5,5600,3.7,3

FAKTOR LINGKUNGAN DAN KEPADATAN PENDUDUK

Kota,Kepadatan_Penduduk (orang/km2),Luas_Lahan_Hijau (%),Tingkat_Polusi (skor),Kualitas_Air (skor),Kemacetan (skor)
Jakarta,15000,10,8,6,9
Surabaya,12000,15,7,6,7
Bandung,14000,12,7,5,8
Medan,10000,18,6,6,6
Bekasi,8000,20,5,5,7
Semarang,11000,16,6,5,6
Palembang,9000,22,5,6,5
Makassar,7000,25,4,5,5
Denpasar,6000,30,3,7,4
Yogyakarta,5000,28,3,7,3
Tangerang,9500,20,5,5,6
Bogor,7000,35,3,7,5
Depok,8000,25,4,5,6
Malang,7500,30,4,6,5
Balikpapan,6800,32,4,6,4
Pontianak,6400,28,3,5,4
Pekanbaru,7000,25,4,5,5
Batam,8000,20,5,6,6
Manado,6000,30,3,7,3
Padang,6200,28,3,6,4
Banjarmasin,6800,25,4,5,4
Solo,7500,30,4,5,4
Kediri,6000,32,3,5,3
Jambi,6600,28,4,6,4
Banda Aceh,5900,35,3,6,3
Palangkaraya,5500,40,2,7,3
Samarinda,7000,22,5,5,4
Kupang,5200,35,3,7,2
Jayapura,5600,32,3,6,3
Mataram,6300,28,4,6,4
Ambon,5200,40,2,7,3
Ternate,4900,45,2,7,2
Sorong,4500,50,1,7,2
Bengkulu,5000,35,3,7,3
Bandar Lampung,6700,28,4,6,5
Palu,5800,32,3,6,3
Kendari,5200,40,2,7,3
Tasikmalaya,6000,35,3,7,4
Cirebon,6200,28,4,6,4
Madiun,5800,32,3,6,3
Magelang,5200,40,2,7,3
Cimahi,7500,30,4,5,5
Pekalongan,5800,32,3,6,3
Tegal,6000,35,3,7,3
Blitar,5200,40,2,7,2
Probolinggo,5500,35,3,7,3
Pasuruan,5800,32,3,6,4
Banyuwangi,6000,35,3,7,4
Bontang,4900,45,2,7,2
Tanjung Pinang,4500,50,1,7,2
Pangkalan Bun,4200,55,1,7,2
Samarinda,7000,22,5,5,4
Manado,6000,30,3,7,3
Bitung,5700,32,3,6,3
Tomohon,5000,40,2,7,2
Gorontalo,6000,35,3,7,3
Toli-Toli,4900,45,2,7,2
Palu,5800,32,3,6,3
Bone,4900,45,2,7,2
Parepare,5200,40,2,7,3
Makassar,7000,25,4,5,5
Sidenreng,4500,50,1,7,2
Kolaka,4200,55,1,7,2
Bau-Bau,4900,45,2,7,2
Tual,4200,55,1,7,2
Saumlaki,4500,50,1,7,2
Langgur,4900,45,2,7,2
Merauke,4200,55,1,7,2
Fakfak,4500,50,1,7,2
Manokwari,5200,40,2,7,3
Biak,4900,45,2,7,2
Sorong,4500,50,1,7,2
Raja Ampat,4200,55,1,7,2
Jayapura,5600,32,3,6,3

![Figure_1](https://github.com/akmalwahyusiwi/Analisis_Data_Pengaruh_Kemacetan_Di_Berbagai_Kota/assets/167242922/1dbab723-a0d4-4edd-bfaa-61286e4534dc)

![Figure_2](https://github.com/akmalwahyusiwi/Analisis_Data_Pengaruh_Kemacetan_Di_Berbagai_Kota/assets/167242922/ba9c2dbb-29b3-4b77-983f-db9cc58cfbec)









