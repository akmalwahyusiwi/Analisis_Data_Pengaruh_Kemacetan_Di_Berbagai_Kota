import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari tabel-tabel
transportasi_df = pd.read_csv("faktor_infrastruktur_transportasi.csv")
ekonomi_df = pd.read_csv("faktor_sosial_ekonomi.csv")
lingkungan_df = pd.read_csv("faktor_lingkungan_kepadatan.csv")

# Analisis sederhana
# Contoh: Rata-rata jumlah kendaraan berdasarkan pendapatan per kapita
avg_kendaraan_perkota = ekonomi_df.merge(transportasi_df, on="Kota")
avg_kendaraan_perkota["Rata-rata Kendaraan"] = avg_kendaraan_perkota["Jumlah_Kendaraan (unit)"] / avg_kendaraan_perkota["Pendapatan_Perkapita (juta Rp)"]

# Set style
sns.set_style("whitegrid")

# Set color palette
sns.set_palette("pastel")

# Visualisasi data
plt.figure(figsize=(15, 18))

# Subplot 1: Histogram Kepadatan Penduduk
plt.subplot(3, 2, 1)
sns.histplot(ekonomi_df["Kepadatan_Penduduk (orang/km2)"], bins=10, kde=True, color='skyblue', edgecolor='black', linewidth=1.2)
plt.title("Histogram Kepadatan Penduduk")
plt.xlabel("Kepadatan Penduduk (orang/km2)")
plt.ylabel("Frekuensi")

# Subplot 2: Sebaran Pendapatan Perkapita vs. Tingkat Pengangguran
plt.subplot(3, 2, 2)
sns.scatterplot(x="Pendapatan_Perkapita (juta Rp)", y="Tingkat_Pengangguran (%)", data=ekonomi_df, color='salmon')
plt.title("Sebaran Pendapatan Perkapita vs. Tingkat Pengangguran")
plt.xlabel("Pendapatan Perkapita (juta Rp)")
plt.ylabel("Tingkat Pengangguran (%)")

plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 18))

# Subplot 3: Diagram Batang Kualitas Infrastruktur Tiap Kota
plt.subplot(3, 2, 1)
sns.barplot(x="Kota", y="Kualitas_Infrastruktur (skor)", data=transportasi_df, palette='Set2')
plt.title("Kualitas Infrastruktur Tiap Kota")
plt.xlabel("Kota")
plt.ylabel("Kualitas Infrastruktur (skor)")
plt.xticks(rotation=45, ha='right')

# Subplot 4: Diagram Pie Persentase Luas Lahan Hijau di Beberapa Kota
plt.subplot(3, 2, 2)
explode = (0.1, 0, 0, 0, 0)  # Untuk menyorot Kota pertama
plt.pie(lingkungan_df["Luas_Lahan_Hijau (%)"][:5], labels=lingkungan_df["Kota"][:5], explode=explode, autopct='%1.1f%%', startangle=140)
plt.title("Persentase Luas Lahan Hijau di Beberapa Kota")

# Subplot 5: Diagram Garis Kemacetan Tiap Kota Berdasarkan Tingkat Pendidikan
plt.subplot(3, 2, 3)
sns.lineplot(x="Tingkat_Pendidikan (skor)", y="Kemacetan (skor)", data=ekonomi_df, color='green')
plt.title("Kemacetan Tiap Kota Berdasarkan Tingkat Pendidikan")
plt.xlabel("Tingkat Pendidikan (skor)")
plt.ylabel("Kemacetan (skor)")

plt.tight_layout()
plt.show()
