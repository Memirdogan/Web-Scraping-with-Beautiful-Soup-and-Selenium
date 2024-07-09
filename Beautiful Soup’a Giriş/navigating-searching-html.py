#################################
# Navigating and Searching HTML
#################################

from bs4 import BeautifulSoup

html = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Example HTML</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
                <p id="paragraph" >A simple HTML page for testing web scraping with BeautifulSoup.</p>
                <a class='link' href='www.miuul.com' target='blank' aria-label='Miuul (Opens Miuul Page)'>Click</a>
                <li>Outsider</li>
                <ul>
                    <li class="list-item">Item 1</li>
                    <li class="list-item">Item 2</li>
                </ul>
                <li>Outsider 2</li>
            </body>
            </html>
"""

soup = BeautifulSoup(html, "html.parser")

# 1- bulmak istediğimiz elementin adı
# 2- attiribute ekliyoruz
soup.find("a", attrs={"class": "link", "target": "blank"})

# yukarıdaki bütün li'leri almak istersek
soup.find("li")  # ilk li'yi getirir
soup.find_all("li")  # liste içerisinde tüm li'leri getirir

# döküman içerisindeki attiributelerinde class'ı listitem olan bütün li'leri getir
li_elements = soup.find_all("li", attrs={"class": "list-item"})
print(li_elements)
print(li_elements[-1])  # li elementlerinin sonuncusu
