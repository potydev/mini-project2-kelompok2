import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = "data/data-violent-sexual-crime.xlsx"

# 1. Baca file Excel
df = pd.read_excel(FILE_PATH, skiprows=2)

# 2. Bersihkan nama kolom dari spasi
df.columns = df.columns.str.strip()

# 3. Pastikan kolom VALUE berupa angka
df['VALUE'] = pd.to_numeric(df['VALUE'], errors='coerce')
df.dropna(subset=['VALUE'], inplace=True)

# 4. Ambil 10 negara dengan VALUE terbesar dan terkecil
top10 = df.groupby('Country')['VALUE'].sum().sort_values(ascending=False).head(10)
bottom10 = df.groupby('Country')['VALUE'].sum().sort_values(ascending=True).head(10)

# 5. Ubah VALUE menjadi jutaan
top10_million = (top10 / 1_000_000).round(2)
bottom10_million = (bottom10 / 1_000_000).round(2)

# 6. Buat figure dengan 2 subplot
fig, axs = plt.subplots(1, 2, figsize=(20, 9))  # 1 baris, 2 kolom

# --- Top 10 ---
bars_top = axs[0].bar(top10_million.index, top10_million.values, color='skyblue')
axs[0].set_title("Top 10 Negara Yang Tidak Aman", fontsize=16)
axs[0].set_xlabel("Negara")
axs[0].set_ylabel("VALUE (Juta)")
axs[0].grid(axis='y', linestyle='--', alpha=0.3)
axs[0].tick_params(axis='x', rotation=45)
for bar in bars_top:
    height = bar.get_height()
    axs[0].text(bar.get_x() + bar.get_width() / 2, height + 0.2, f"{height} Juta", ha='center', fontsize=10)

# --- Bottom 10 ---
bars_bottom = axs[1].bar(bottom10_million.index, bottom10_million.values, color='salmon')
axs[1].set_title("Top 10 Negara Yang Aman", fontsize=16)
axs[1].set_xlabel("Negara")
axs[1].set_ylabel("VALUE (Juta)")
axs[1].grid(axis='y', linestyle='--', alpha=0.3)
axs[1].tick_params(axis='x', rotation=45)
for bar in bars_bottom:
    height = bar.get_height()
    axs[1].text(bar.get_x() + bar.get_width() / 2, height + 0.05, f"{height} Juta", ha='center', fontsize=10)

plt.tight_layout()
plt.savefig("top10 aman dan tidak aman.png")
plt.show()
