import pandas as pd

# Fungsi untuk menghitung bunga sederhana
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Membaca data dari file CSV
df = pd.read_csv('loans.csv')

# Menghitung bunga sederhana dan total pembayaran
df['Simple Interest'] = df.apply(lambda row: calculate_simple_interest(row['Principal'], row['Rate'], row['Time']), axis=1)
df['Total Payment'] = df['Principal'] + df['Simple Interest']

# Menampilkan hasil
print("Hasil Perhitungan Bunga Sederhana:")
print(df)

# Menyimpan hasil ke file CSV baru
df.to_csv('simple_interest_results.csv', index=False)
print("\nHasil telah disimpan ke 'simple_interest_results.csv'")