# Kaggle Veri Seti İncelemesi: Sephora Ürünleri

Bu veriseti tahminleme, sınıflandırma, kümeleme problemlerine örnek içindir

* **Veri Seti:** Sephora Products and Skincare Reviews
* **Link:** https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews
* **Seçtiğim Dosya:** `product_info.csv` (İçinde 8000'den fazla ürün ve 27 farklı sütun var)

Kaggle'daki tabloda ürünlerin markası (`brand_name`), kategorisi (`primary_category`), dolar cinsinden satış fiyatı (`price_usd`), kullanıcıların verdiği puanlar (`rating`), toplam yorum sayısı (`reviews`) ve favoriye ekleme sayıları (`loves_count`) yer alıyor.

---

### Bu Veri Seti 3 Temel Probleme Nasıl Uygulanır?

#### 1. Tahminleme 
* **Amaç:** Bir ürünün özelliklerine bakarak piyasa satış fiyatını tahmin etmek.
* **Nasıl Yaparız?:** Ürünün hangi markaya ait olduğu, hangi kategoride olduğu (parfüm mü, nemlendirici mi vb.), kaç kişinin favorilediği ve kaç yorum aldığı gibi bilgileri modele veririz.
* **Tahmin Edilecek Değer:** `price_usd` (Sayısal değer).

#### 2. Sınıflandırma
* **Amaç:** Bir ürünün piyasada sevilip sevilmeyeceğini, yani yüksek puanlı ("başarılı") bir ürün olup olmayacağını önceden anlamak.
* **Nasıl Yaparız?:** Tablodaki `rating` sütununu eşik değere göre iki sınıfa ayırırız. Örneğin 4.2 ve üzeri puan alan ürünlere "1" (Başarılı / Favori Ürün), 4.2'nin altındakilere "0" ( Düşük Puanlı Ürün) etiketi verip modeli buna göre eğitiriz.
* **Tahmin Edilecek Değer:** Oluşturduğumuz sınıf etiketi (0 veya 1).

#### 3. Kümeleme 
* **Amaç:** Veride hazır bir etiket olmadan ürünleri fiyat ve popülerlik alışkanlıklarına göre kendi içinde doğal gruplara ayırmak.
* **Nasıl Yaparız?:** `price_usd`, `rating`, `reviews` ve `loves_count` sütunlarını normalize edip K-Means algoritmasına veririz.
* **Beklenen Kümeler:**
  * Fiyatı ucuz ama puanı çok yüksek olan "Fiyat/Performans Ürünleri"
  * Fiyatı çok pahalı ama puanı standart kalan "Lüks/Pahalı Seri Ürünler"
  * Puanı düşük olsa da çok fazla favorilenmiş "Viral/Sosyal Medya Ürünleri"
* **Kullanılabilecek Yöntemler:** K-Means veya ???? (şu an bilmiyorum)
