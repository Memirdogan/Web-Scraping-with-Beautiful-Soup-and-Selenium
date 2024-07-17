import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = pd.read_excel(
    r"C:\Users\musae\Desktop\Web Scraping with Beautiful Soup and Selenium\TrendyolPhoneData\trendyol_data.xlsx")


def clean_price(price):
    if pd.isna(price):
        return np.nan
    try:
        # Replace non-numeric characters and convert to float
        return float(price.replace(' TL', '').replace('.', '').replace('Null', ''))
    except ValueError:
        return np.nan


def clean_ram(ram):
    if isinstance(ram, float) and np.isnan(ram):
        return np.nan
    try:
        return int(ram.replace(' GB', '').replace('+', ''))
    except ValueError:
        return np.nan


def clean_camera(camera):
    try:
        # MP'yi kaldır ve fazladan boşlukları sil
        camera = camera.replace(' MP', '').replace('ve üstü', '').strip()

        if '-' in camera:
            # Aralıktaki değerlerin ortalamasını al
            values = [int(x) for x in camera.split(' - ')]
            return sum(values) / len(values)
        else:
            return int(camera)
    except:
        return np.nan


df['Kamera Çözünürlüğü'] = df['Kamera Çözünürlüğü'].apply(clean_camera)
df['Kamera Çözünürlüğü'] = df['Kamera Çözünürlüğü'].fillna(df['Kamera Çözünürlüğü'].mean())

def clean_storage(storage):
    if pd.isna(storage) or storage.lower() == 'yok':
        return np.nan
    try:
        return int(storage.replace(' GB', '').replace('TB', '000').strip())
    except ValueError:
        return np.nan


def clean_speed(speed):
    if pd.isna(speed):
        return '4G'
    if speed == '4.5G':
        return '4G'
    return speed


def clean_screen_size(size):
    if pd.isna(size) or not isinstance(size, str):
        return np.nan
    try:
        if 've üstü' in size:
            return float(size.split()[0])
        elif '-' in size:
            values = [float(x.replace(',', '.')) for x in size.split(' - ')]
            return sum(values) / len(values)
        else:
            return float(size.replace(',', '.'))
    except ValueError:
        return np.nan


def clean_battery(battery):
    if pd.isna(battery) or not isinstance(battery, str):
        return np.nan
    try:
        if '-' in battery:
            values = [int(x.replace(' ve altı', '').strip()) for x in battery.split('-')]
            return sum(values) / len(values)
        else:
            return int(battery.replace(' ve altı', '').strip())
    except ValueError:
        return np.nan


def clean_color(color):
    if pd.isna(color):
        return 'Bilinmiyor'
    return color


def clean_front_camera_resolution(resolution):
    if pd.isna(resolution) or not isinstance(resolution, str):
        return np.nan
    try:
        if 've üstü' in resolution:
            return int(resolution.split()[0])
        elif '-' in resolution:
            values = [float(x.split()[0].replace(',', '.')) for x in resolution.split(' - ')]
            return sum(values) / len(values)
        else:
            return float(resolution.split()[0].replace(',', '.'))
    except ValueError:
        return np.nan


def fill_na_with_unknown(column):
    return column.fillna('Bilinmiyor')


def clean_warranty_duration(duration):
    if pd.isna(duration):
        return 'Bilinmiyor'
    return duration


def clean_camera_range(range):
    if pd.isna(range):
        return 'Bilinmiyor'
    return range


def clean_front_camera_count(count):
    try:
        return int(count)
    except (ValueError, TypeError):
        return np.nan


df['Fiyat'] = df['Fiyat'].apply(clean_price)
df['RAM Kapasitesi'] = df['RAM Kapasitesi'].apply(clean_ram)
df['Dahili Hafıza'] = df['Dahili Hafıza'].apply(clean_storage)
df['Mobil Bağlantı Hızı'] = df['Mobil Bağlantı Hızı'].apply(clean_speed)
df['Cep Telefonu Modeli'] = df['Cep Telefonu Modeli'].fillna('Bilinmiyor')
df['Ekran Boyutu'] = df['Ekran Boyutu'].apply(clean_screen_size)
df['Pil Gücü (mAh)'] = df['Pil Gücü (mAh)'].apply(clean_battery)
df['Renk'] = df['Renk'].apply(clean_color)
df['Ön Kamera Çözünürlüğü'] = df['Ön Kamera Çözünürlüğü'].apply(clean_front_camera_resolution)
df['Görüntü Teknolojisi'] = fill_na_with_unknown(df['Görüntü Teknolojisi'])
df['Ekran Çözünürlüğü'] = fill_na_with_unknown(df['Ekran Çözünürlüğü'])
df['Kozmetik Durum'] = fill_na_with_unknown(df['Kozmetik Durum'])
df['Garanti Süresi'] = df['Garanti Süresi'].apply(clean_warranty_duration)
df['Ana Kamera Çözünürlük Aralığı'] = df['Ana Kamera Çözünürlük Aralığı'].apply(clean_camera_range)
df['Ön Kamera Sayısı'] = df['Ön Kamera Sayısı'].apply(clean_front_camera_count)

# Kontrol
print(df.head())
print(df.info())
df.to_excel('cleaned_excel_file.xlsx', index=False)