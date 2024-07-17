import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
# Veriyi Excel dosyasından oku
df = pd.read_excel(r"C:\Users\musae\Desktop\Web Scraping with Beautiful Soup and Selenium\TrendyolPhoneData\cleaned_excel_file.xlsx")

print("############################ Shape ############################")
print(df.shape)
print("############################ Types ############################")
print(df.dtypes)
print("############################ Head ############################")
print(df.head())
print("############################ tail ############################")
print(df.tail())
print("############################ Na ############################")
print(df.isnull().sum())

total_brands = df['Marka'].nunique()
print(f"Farklı Marka Sayısı: {total_brands}")

# Eksik veri miktarlarını gösteren bir grafik
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Eksik Veri Görselleştirmesi')
plt.show()

plt.figure(figsize=(12, 6))
df['Marka'].value_counts().plot(kind='bar')
plt.title('Marka Dağılımı')
plt.xlabel('Marka')
plt.ylabel('Adet')
plt.show()



