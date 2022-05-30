# DjangoLibraryApp

Veri tabanı olarak MongoDB kullandığım bu projede, Django kütüphanesinin base engine i yerine mongoengine kütüphanesini kullandım. 
Bu sayede NoSQL yapısındaki MongoDB'yi Django'nun ORM syntax ını kullanabildim.


Uygulamayı temelde 2 ana app e böldüm. Bunlar **user** ve **library** appleri. 
User app i içerisinde kullanıcı bilgilerini tuttuğumuz User document'ı bulunmakta. 
Bu aşamada django engine kullanmadığımız için Django ile gelen User tablosunu kullanamamış olduk.
Library app i içerisinde kütüphanedeki kitapları tutan Book documentı ve ödünç alınan kitapları tutan BookBorrow documentı bulunmaktadır.
BookBorrow documentı hem ödünç alınan kitabın object id sini hemde ödünç alan kullanıcının object idsini tutmaktadır.
Ayrıca is_delivered alanı ile kitabın geri teslim edilip edilmediği bilgisini tutuyoruz. 
Böylece aynı kitabı 2 kişinin kiralayamamasını kontrol edebilmiş oluyoruz.
