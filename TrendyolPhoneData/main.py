import pandas as pd
from TrendyolPhoneData  import scrape_trendyol_data

number_of_pages = int(input("Kaç sayfa taransın?"))

data = scrape_trendyol_data(pages=number_of_pages)

df = pd.DataFrame(data)
df.to_excel("trendyol_data.xlsx", index=False)
print("Veriler Excel dosyasına başarıyla kaydedildi.")
