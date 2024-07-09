"""
XPath (XML Path Language):
XPath, XML veya HTML belgelerinde belirli Öğeleri bulmak ve seçmek için kullanılan bir dil ve yol belirleme tekniğidir.
* starts-with, contains gibi komutları içinde barındırdığı için elemnt bulma alanı çok kuvvetlidir
* elementlere node ve tag de denilir
* attiribute = elementlerin özellikleri (id, class, href)
* text = element içerisindeki asıl içerik
* child = bir elementin içerisindeki element
* parent = elementi kapsayan element, yani içerisinde bulunduğumuz element
* ancestor = tüm atalarımız, yani elementi içerisine alıp kapsayan tüm elementler
* sibling = parent elementinin altında aunı seviyede duran kardeş elementler

// belgenin herhangi bir yerindeki elementleri aramak için kullanılır
/ sadece child elementleri aradığımızı ifade eder
elementname bu element adına sahip olan elementleri seçer (div, p ne arıyorsak)
@attiributename bir attiribute seçer (class, id ne arıyorsak)
text() bir elementin içerisindeki metni/içeriği seçer



################################################################################
CSS Selectors:
CSS Seçiciler, web sayfalarındaki HTML öğelerini seçmek ve stil uygulamak için kullanılan bir yöntemdir.

Web kazımada kullanılan CSS Seçiciler
• Simple Selectors: Öğeleri adlarına, id'lerine veya class'larına göre seçmek için kullanılırlar.

p.text-red => class'ı text-red olan p elementi
div#main => id'si main olan divi bul
i için #
class için .
sadece element adına göre seçmek istersek => dümdüz elementname

• Combinator Selectors: Elementleri diğer elementlerle olan Özel İçerisindeki p" gibi) göre seçmek İçin kullanılırlar.

div p => div içerisindeki p

• Attribute Selectors: Elementleri attribute'u olup olmamasına göre veya attribute değerine göre seçmek İçin kullanılırlar.

@class='text-red' => class'ı text-red olanı getir
@class~='text-red' => class'ında text-red geçeni getir

"""