import requests
from bs4 import BeautifulSoup

x = 1
while x <= 3:
    url = requests.get("https://www.trendyol.com/cep-telefonu-x-c103498?pi="+str(x)+"")
    html = url.content

    soup = BeautifulSoup(html, "lxml")

    product = soup.find_all("div", attrs={"class": "p-card-wrppr with-campaign-view"})
    print("#########################################")
    for urun in product:
        linkbasi = "https://www.trendyol.com"
        linksonu = urun.a.get("href")
        link = linkbasi+linksonu

        r1 = requests.get(link)
        html1 = r1.content
        soup1 = BeautifulSoup(html1, "lxml")
        info = soup1.find("div", attrs={"class": "pr-in-cn"})

        info_title_folder = soup1.find("h1", attrs={"class": "pr-new-br"})
        info_name = info_title_folder.find("span").text.strip()

        info_brand = info_title_folder.find("a", attrs={"class": "product-brand-name-with-link"})
        brand_text = info_brand.text.strip() if info_brand else "Null"

        info_attiribute = soup1.find("div", attrs={"class": "attributes"})

        price = soup1.find("div", attrs={"class": "pr-bx-nm with-org-prc"})
        price_text = price.text.strip() if price else "Null"

        print(f"Ürün adı: {info_name}")
        print("#########################################################")
        print(f"Marka: {brand_text}")
        print(f"Fiyat: {price_text}")

        if info_attiribute:
            attrs_info = info_attiribute.find_all("li")
            for attr in attrs_info:
                try:
                    attribute_name = attr.find("span", class_="attribute-label attr-name").text.strip()
                    attribute_value_div = attr.find("span", class_="attribute-value")
                    attribute_value = attribute_value_div.find("div", class_="attr-name attr-name-w").text.strip()
                    print(f"{attribute_name} ----> {attribute_value}")
                except:
                    print("ürünün bu özelliği bulunamadı")
        else:
            print("Özellikler Bulunamadı")

        print("\n")
    x = x + 1
    print("#########################################################################################")
    print("#########################################################################################")
    print("#########################################################################################")
    print("#########################################################################################")