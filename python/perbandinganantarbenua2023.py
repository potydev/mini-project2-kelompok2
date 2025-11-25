import pandas as pd
import matplotlib.pyplot as plt

# Baca file
file_path = "../data/data-violent-sexual-crime.xlsx"
df = pd.read_excel(file_path, skiprows=2)

# Bersihkan nama kolom
df.columns = df.columns.str.strip()
df.columns = ['Iso3_code', 'Country', 'Region', 'Category', 'Sex', 'Year', 'VALUE']

# Filter data untuk tahun 2023
df_2023 = df[df['Year'] == 2023]

# Hitung total VALUE per Region (Benua)
region_totals = df_2023.groupby('Region')['VALUE'].sum().sort_values(ascending=False)

# Opsional: ubah ke jutaan
region_totals_million = (region_totals / 1_000_000).round(2)

# Pie chart
plt.figure(figsize=(12, 10))
plt.pie(
    region_totals_million.values,
    labels=region_totals_million.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.Set3.colors  # variasi warna
)

plt.title("Proporsi Kasus Kekerasan Seksual per Benua (2023) dalam Jutaan", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('../perbandingan antar benua.png')
plt.show()
