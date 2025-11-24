import pandas as pd

# Load file dengan header di baris ke-2
file_path = "data-violent-sexual-crime.xlsx"
data = pd.read_excel(file_path, header=2)

# Bersihkan nama kolom dari spasi
data.columns = data.columns.str.strip()

kolom_nilai = 'VALUE'
kolom_negara = 'Country'

# Pastikan kolom VALUE ada
if "VALUE" not in data.columns:
    raise Exception("❌ Kolom VALUE tidak ditemukan setelah pemrosesan!")

# Fungsi klasifikasi
def calculate_klasifikasi(x):
    if x >= 100000:
        return "Sangat Tinggi"
    elif x >= 50000:
        return "Tinggi"
    elif x >= 10000:
        return "Sedang"
    elif x >= 1000:
        return "Rendah"
    else:
        return "Sangat Rendah"

# Buat kolom klasifikasi baru
data["Klasifikasi"] = data["VALUE"].astype(float).apply(calculate_klasifikasi)

top5_aman = data.sort_values(by=kolom_nilai, ascending=False).head(5)
top5_tidak_aman = data.sort_values(by=kolom_nilai, ascending=True).head(5)

print(data)


with pd.ExcelWriter('Rekap Kasus.xlsx', engine='openpyxl') as writer:
    data.to_excel(writer, sheet_name = 'Semua Data', index=False)
    top5_aman.to_excel(writer, sheet_name= 'Top 5 Negara Paling Aman', index=False)
    top5_tidak_aman.to_excel(writer, sheet_name= 'Top 5 Negara Paling Tidak Aman', index=False)
