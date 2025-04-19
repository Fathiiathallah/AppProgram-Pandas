import pandas as pd

# Fungsi untuk menghitung bunga sederhana
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Mengambil input dari pengguna
principal = float(input("Masukkan jumlah pinjaman (Principal): "))
rate = float(input("Masukkan suku bunga tahunan (Rate) dalam persen: "))
time = float(input("Masukkan waktu (Time) dalam tahun: "))

# Menghitung bunga sederhana
interest = calculate_simple_interest(principal, rate, time)
total_payment = principal + interest

# Menyimpan hasil dalam DataFrame
data = {
    'Principal': [principal],
    'Rate (%)': [rate],
    'Time (years)': [time],
    'Simple Interest': [interest],
    'Total Payment': [total_payment]
}

df = pd.DataFrame(data)

# Menampilkan hasil
print("\nHasil Perhitungan Bunga Sederhana:")
print(df)