# Türkiye 81 İl K-Means Analizi ve Makine Öğrenmesi Veri Seti İncelemesi

Bu repo, denetimsiz öğrenme yöntemlerinden **K-Means Kümeleme** algoritmasının Türkiye'nin 81 ilinin coğrafi koordinatları üzerindeki aşamalı uygulamasını ve makine öğrenmesi problemlerine (sınıflandırma, tahminleme, kümeleme) uygun bir Kaggle veri seti analizini içermektedir.

---

## 1. K-Means Aşamaları ve Coğrafi Bölge Karşılaştırması

Projede algoritma 3 aşamada ele alınmıştır:
1. **Aşama 1 (`kmeans_asama1.py`):** İlk 7 il seçilerek $k=2$ küme merkezi ile Öklid mesafesi ve ağırlık merkezi güncelleme mantığı saf matematiksel adımlarla uygulanmıştır.
2. **Aşama 2 (`kmeans_asama2.py`):** Türkiye'nin 81 ili dahil edilmiş, elle seçilen 7 merkez üzerinden iller en yakın merkeze atanıp merkezler döngüyle güncellenmiştir.
3. **Aşama 3 (`kmeans_asama3.py`):** Başlangıç merkezlerini 81 il arasından rastgele seçen, mesafe kareleri üzerinden hesaplama maliyetini düşüren ve atamalar sabitlendiğinde (yakınsama/convergence) otomatik duran optimize algoritma kurgulanmıştır.

### "İller Gerçekten Bu Mantıkla mı Bölgelere Ayrılmış?"
* **K-Means:** Noktalar arasındaki doğrusal (Öklid) kuş uçuşu mesafeyi baz alır ve dairesel/küresel kümeler üretme eğilimindedir.
* **Resmi 7 Coğrafi Bölge:** 1941 Birinci Coğrafya Kongresi'nde yalnızca koordinatlara göre değil; sıradağların uzanışı, denizellik/karasallık etkisi, yağış rejimi, iklim tipleri ve bitki örtüsü esas alınarak çizilmiştir.
* **Sonuç:** K-Means şerit halinde doğu-batı ekseninde uzanan Karadeniz veya Akdeniz gibi bölgeleri tek kümede tutamaz; kıyı illerini dairesel yakınlıktan dolayı İç Anadolu veya Doğu Anadolu merkezlerine bağlar. Dolayısıyla Türkiye'nin coğrafi bölgeleri salt koordinat mesafesiyle açıklanamaz.

---

## 2. Kaggle Veri Seti İncelemesi

Ödev kapsamında hem denetimli (regresyon ve sınıflandırma) hem de denetimsiz (kümeleme) makine öğrenmesi problemlerine uygun bir veri seti seçilmiştir.

* **Veri Seti:** Customer Personality Analysis
* **Kaggle Linki:** [https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)
* **Özet:** Müşterilerin yaş, gelir, eğitim durumu, çocuk sayısı, web sitesi ziyaretleri ve çeşitli kategorilerdeki (şarap, et, tatlı vb.) harcama miktarlarını içeren çok boyutlu bir veri tablosudur.

### Bu Veri Seti Hangi ML Problemlerine Uygundur?

1. **Tahminleme (Regression):**
   * **Problem:** Müşterinin demografik özelliklerine (yaş, eğitim, gelir, evdeki çocuk sayısı) bakılarak yıllık toplam harcama tutarının (`Total Spending`) sayısal olarak tahmin edilmesi.
   * **Hedef Değişken:** Sürekli sayısal değer (`MntWines + MntFruits + ...`).

2. **Sınıflandırma (Classification):**
   * **Problem:** Bir müşterinin son pazarlama kampanyasına olumlu yanıt verip vermeyeceğinin (`0: Red`, `1: Kabul`) tahmin edilmesi.
   * **Hedef Değişken:** İkili kategorik etiket (`Response`).

3. **Kümeleme (Clustering):**
   * **Problem:** Etiketsiz veride müşterilerin `Income` (Gelir) ve harcama alışkanlıkları özelliklerinin K-Means / Hiyerarşik Kümeleme ile gruplanarak "Tasarruflu Müşteri", "Premium Müşteri", "Fırsatçı Alışverişçi" gibi alt hedef kitle segmentlerine ayrılması.
