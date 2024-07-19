############################################
# Headers ve Proxy
############################################
"""
-- Headers
Headers, bir web tarayıcısı ile iletişimde bulunurken gönderilen bilgilerdir, bu bilgilerde kullanıcının tarayıcı türü,
isteğin tipi gibi bilgiler bulunabilir. Web sitesinden veri çekerken tarayıcı gibi bir iz bırakabiliriz.

-- Proxy
Proxy, bir ağdaki istemcinin (kullanıcının), sunucuyla iletişimini sağlayan araçtır. Proxy gizliliği arttırabilir,
iletişimi kolaylaştırır ve farklı bir IP adresinden bağlanıyormuş gibi görünmemizi sağlayabilir.


---
headers = {
    "User-Agent": "Mozi11a/5.O (Windows NT 10,0; Win64; x64).......",
    "Accept-Language": "en-US,en;q=0.5"

** UserAgent ile tarayıcımızın mozilla olduğu belirtildi
** sitenin defoult dilinin de ingilizce olması belirtildi
---
proxy = {"http": "http://192.0.0.0:0000", "https":
    "http://192.0.0.10:0000"}

** Coğrafi sınırları kaldırmak için avrupa sunucusunda bulunan proxy kullanıldı
---
"""
