# To visualize what Evolutionary Neural Networks have learned.

* Bu projemizde Evrişimli sinir ağlarının öğrendiklerini, filtreleri ve ısı haritasını görselleştireceğiz.

* Test Resmimiz : 

![dog](https://user-images.githubusercontent.com/54184905/78069651-1d7fce00-73a3-11ea-95f8-2b86aa279b2b.jpg)

* Modelimiz, katmanlarımız, parametrelerimiz :

![Screenshot_2020-03-31_22-59-47](https://user-images.githubusercontent.com/54184905/78069826-68014a80-73a3-11ea-8f0e-c90e07200bed.png)

* Şimdi katmanlarımızdaki kanallardan geçen resimlere göz atalım :

![Screenshot_2020-03-31_22-39-25](https://user-images.githubusercontent.com/54184905/78069973-ac8ce600-73a3-11ea-9eac-c5a96f32d5b1.png)

![Screenshot_2020-03-31_22-41-04](https://user-images.githubusercontent.com/54184905/78069975-ad257c80-73a3-11ea-8c78-15b828a1c440.png)

    Katmanlardaki resimleri gördünüz. ilk katmanın beşinci kanalından çıkan resimde kenar ayrıntıları tanınmış,
    Ama hayla canlı hakkında pek bir bilgi edinememiş.
    
    İkinci katmanda ise köpeğin burnu ve kuyruğu tanımlanmış yani modelimiz yavaştan canlının köpek olduğunu anlıyor.
    
* Şimdi ise Tüm kanalların tüm aktivasyonlarını görselleştirme işlemini yapalım : 

![Screenshot_2020-03-31_22-41-24](https://user-images.githubusercontent.com/54184905/78070495-8f0c4c00-73a4-11ea-8b2a-21581c06e456.png)

![Screenshot_2020-03-31_22-41-35](https://user-images.githubusercontent.com/54184905/78070499-90d60f80-73a4-11ea-8dea-d5c339237d23.png)

![Screenshot_2020-03-31_22-41-45](https://user-images.githubusercontent.com/54184905/78070501-929fd300-73a4-11ea-8bbb-a28b0185168f.png)

![Screenshot_2020-03-31_22-41-54](https://user-images.githubusercontent.com/54184905/78070532-a0edef00-73a4-11ea-997e-8142076815f0.png)

![Screenshot_2020-03-31_22-42-04](https://user-images.githubusercontent.com/54184905/78070535-a2b7b280-73a4-11ea-965e-886020bd91d7.png)

![Screenshot_2020-03-31_22-42-10](https://user-images.githubusercontent.com/54184905/78070543-a51a0c80-73a4-11ea-9f17-7de4222e22ca.png)

![Screenshot_2020-03-31_22-42-15](https://user-images.githubusercontent.com/54184905/78070559-ae0ade00-73a4-11ea-80ed-ae0c4206ee10.png)

![Screenshot_2020-03-31_22-42-21](https://user-images.githubusercontent.com/54184905/78070560-aea37480-73a4-11ea-9339-1fbc7ef4738a.png)

    Büyük resimde de gördüğünüz gibi modelimiz adım adım köpeği tanımakta.
    
* Artık resim üzerinde gezen filtreleri görselleştirme zamanı : 

![Screenshot_2020-03-31_22-42-57](https://user-images.githubusercontent.com/54184905/78071091-8a946300-73a5-11ea-8c9c-e1b26fb99018.png)

![Screenshot_2020-03-31_22-44-21](https://user-images.githubusercontent.com/54184905/78071095-8bc59000-73a5-11ea-9acd-4111f5ce64a7.png)

![Screenshot_2020-03-31_22-44-46](https://user-images.githubusercontent.com/54184905/78071097-8cf6bd00-73a5-11ea-988d-c54d80783ed7.png)

![Screenshot_2020-03-31_22-44-34](https://user-images.githubusercontent.com/54184905/78071105-8ff1ad80-73a5-11ea-9960-947d6cd7969d.png)

    Bu gördüğünüz resimler rastgele katmanlardan çektiğim filtreler.
    Bu filtreler resimlerin üzerinde gezinerek köpeğin gözü burnu vb. yerlerini tespit eder.
    Ve son katmanlara doğruda köpek olarak sınıflandırılır.

