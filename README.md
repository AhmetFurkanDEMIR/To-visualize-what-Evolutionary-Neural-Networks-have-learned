# To visualize what Evolutionary Neural Networks have learned.

* Bu projemizde Evrişimli sinir ağlarının öğrendiklerini, filtreleri ve ısı haritasını görselleştireceğiz.

* Test Resmimiz : 

![dog](https://user-images.githubusercontent.com/54184905/78069651-1d7fce00-73a3-11ea-95f8-2b86aa279b2b.jpg)

* Modelimiz katmanlarımız parametrelerimiz :

![Screenshot_2020-03-31_22-59-47](https://user-images.githubusercontent.com/54184905/78069826-68014a80-73a3-11ea-8f0e-c90e07200bed.png)

* Şimdi katmanlarımızdaki kanallardan geçen resimlere göz atalım :

![Screenshot_2020-03-31_22-39-25](https://user-images.githubusercontent.com/54184905/78069973-ac8ce600-73a3-11ea-9eac-c5a96f32d5b1.png)

![Screenshot_2020-03-31_22-41-04](https://user-images.githubusercontent.com/54184905/78069975-ad257c80-73a3-11ea-8c78-15b828a1c440.png)

    Katmanlardaki resimleri gördünüz. ilk katmanın beşinci kanalından çıkan resimde kenar ayrıntıları tanınmış,
    Ama hayla canlı hakkında pek bir bilgi edinememiş.
    
    İkinci katmanda ise köpeğin burnu ve kuyruğu tanımlanmış yani modelimiz yavaştan canlının köpek olduğunu anlıyor.
    
* Şimdi ise Tüm kanalların tüm aktivasyonlarını görselleştirme işlemini yapalım : 
