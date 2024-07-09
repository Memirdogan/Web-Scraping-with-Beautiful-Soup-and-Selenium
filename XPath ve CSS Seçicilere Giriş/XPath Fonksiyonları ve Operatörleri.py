#XPath Fonksiyonları ve Operatörleri
###########################################################
"""

"|" (pipe) operatörü - birden fazla elementi aynı anda seçmek için kullanılır (//p | //h2)
and operatörü - ve şartı eklememizi sağlar (//input[@type="text" and @name="username"]
or operatörü - veya şartı eklememizi sağlar (//a[@class="external" or @target="_blank"])

######################################################################################
XPath Fonksiyonları, diğer dillerde olduğu gibi built-in(gömülü) fonksiyonlardandır.
######################################################################################

* contains() - bir elementin x kısmında y kelimesi geçiyor mu
* starts-with() - elementin adı x ile başlıyorsa getir
* not() - içinde bulunmayan olumsuz koşul
* li[x] - listelerde indekse erişmek için x yerine 1,2,3 gibi indeksler yazabiliriz
* last() - örneğin bir listedeki sonuncu li yi getirmek için kullanılabilir



contains(@aradığımızKısım,'AradığımızMetninKendisi')
contains(@class,'products')

starts-with(@aradığımızKısım,'AradığımızMetninKendisi')
starts-with(@class,'products')

//p[not(b)] - içinde b etiketi olmayan p leri getir













"""