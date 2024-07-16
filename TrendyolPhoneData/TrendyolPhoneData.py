import requests
from bs4 import BeautifulSoup


def scrape_trendyol_data(pages):
    global attribute_name, attribute_value
    data = []
    x = 1

    while x <= pages:
        url = requests.get("https://www.trendyol.com/cep-telefonu-x-c103498?pi=" + str(x) + "")
        html = url.content
        soup = BeautifulSoup(html, "lxml")
        product = soup.find_all("div", attrs={"class": "p-card-wrppr with-campaign-view"})

        for urun in product:
            try:
                linkbasi = "https://www.trendyol.com"
                linksonu = urun.a.get("href")
                link = linkbasi + linksonu

                r1 = requests.get(link)
                html1 = r1.content
                soup1 = BeautifulSoup(html1, "lxml")

                info_title_folder = soup1.find("h1", attrs={"class": "pr-new-br"})
                info_name = info_title_folder.find("span").text.strip()

                info_brand = info_title_folder.find("a", attrs={"class": "product-brand-name-with-link"})
                brand_text = info_brand.text.strip() if info_brand else "Null"

                info_attiribute = soup1.find("div", attrs={"class": "attributes"})

                price = soup1.find("div", attrs={"class": "pr-bx-nm with-org-prc"})
                price_text = price.text.strip() if price else "Null"

                attributes_dict = {}

                if info_attiribute:
                    attrs_info = info_attiribute.find_all("li")
                    for attr in attrs_info:
                        try:
                            attribute_name = attr.find("span", class_="attribute-label attr-name").text.strip()
                            attribute_value_div = attr.find("span", class_="attribute-value")
                            attribute_value = attribute_value_div.find("div",
                                                                       class_="attr-name attr-name-w").text.strip()
                            attributes_dict[attribute_name] = attribute_value
                        except Exception as e:
                            print(f"Hata: {e}")
                            attributes_dict[attribute_name] = "Null"
                else:
                    print("Özellikler Bulunamadı")
                data.append({
                    "Ürün adı": info_name,
                    "Marka": brand_text,
                    "Fiyat": price_text,
                    **attributes_dict
                })
            except Exception as e:
                print(f"Error processing product: {e}")
        x = x + 1
    return data
