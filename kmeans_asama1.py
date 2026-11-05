import math
import matplotlib.pyplot as plt

# ==============================================================================
# AŞAMA 1: İLK 7 İL İLE TEMEL DÜZEYDE (ACEMİ USULÜ) K-MEANS MANTIĞI (k = 2)
# ==============================================================================

# 1. ADIM: Veri Hazırlığı
# ilk 7 ilimizi ve onların enlem/boylam koordinatlarını
# en basit haliyle ayrı ayrı listelerde tutuyoruz.
il_isimleri = ["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya"]

# Enlemler (Kuzey-Güney ekseni -> Y ekseni gibi düşünebiliriz)
enlemler = [37.0000, 37.7648, 38.7507, 39.7191, 40.6501, 39.9334, 36.8969]

# Boylamlar (Doğu-Batı ekseni -> X ekseni gibi düşünebiliriz)
boylamlar = [35.3213, 38.2786, 30.5567, 43.0503, 35.8353, 32.8597, 30.7133]

print("Kümelenecek ilk 7 ilimiz:")
for i in range(len(il_isimleri)):
    print(il_isimleri[i], "-> Enlem:", enlemler[i], "Boylam:", boylamlar[i])

print("-" * 50)


# 2. ADIM: Başlangıç Merkezlerinin (Centroid) Belirlenmesi
# K = 2 olduğu için başlangıçta 2 tane merkez noktasına ihtiyacımız var.
# Şimdilik rastgele seçim fonksiyonları kullanmak yerine, elimizdeki 7 ilden
# gözümüze kestirdiğimiz 2 tanesini doğrudan başlangıç merkezi seçiyoruz.
# Örneğin: 0. sıradaki Adana (Merkez 1) ve 3. sıradaki Ağrı (Merkez 2) olsun.

merkez1_enlem = enlemler[0]   
merkez1_boylam = boylamlar[0] 

merkez2_enlem = enlemler[3]   
merkez2_boylam = boylamlar[3] 

print("Başlangıçta seçilen 1. Merkez (Adana):", merkez1_enlem, merkez1_boylam)
print("Başlangıçta seçilen 2. Merkez (Ağrı):", merkez2_enlem, merkez2_boylam)
print("-" * 50)


# 3. ADIM: İlleri En Yakın Merkeze Atama ve Merkezleri Güncelleme Döngüsü
# Algoritmanın birkaç adımda noktaları merkezlere çekip merkezleri kaydırmasını
# izlemek için basitçe 4 kere dönen bir 'for' döngüsü kuruyoruz.

for adim in range(4):
    print(f"\n--- {adim + 1}. ADIM / İTERASYON BAŞLADI ---")
    
    # Her ilin hangi merkeze ait olduğunu tutacağımız liste
    # Örneğin [1, 2, 1, 2, ...] gibi 1. ya da 2. kümeyi belirtecek
    hangi_kume = []
    
    # 7 ilin her biri için tek tek mesafeleri hesaplıyoruz
    for i in range(7):
        su_anki_enlem = enlemler[i]
        su_anki_boylam = boylamlar[i]
        
        # Pisagor (Öklid) bağıntısı ile 1. merkeze olan uzaklığı buluyoruz:
        # Uzaklık = Karekök( (x1 - x2)^2 + (y1 - y2)^2 )
        fark_enlem_1 = su_anki_enlem - merkez1_enlem
        fark_boylam_1 = su_anki_boylam - merkez1_boylam
        mesafe_merkez1 = math.sqrt((fark_enlem_1 ** 2) + (fark_boylam_1 ** 2))
        
        # Aynı şekilde 2. merkeze olan uzaklığı buluyoruz:
        fark_enlem_2 = su_anki_enlem - merkez2_enlem
        fark_boylam_2 = su_anki_boylam - merkez2_boylam
        mesafe_merkez2 = math.sqrt((fark_enlem_2 ** 2) + (fark_boylam_2 ** 2))
        
        # Hangisi daha yakınsa ili o kümeye dahil ediyoruz
        if mesafe_merkez1 < mesafe_merkez2:
            hangi_kume.append(1)  # 1. merkeze daha yakın
            print(f"{il_isimleri[i]} -> 1. Kümeye atandı (Mesafe 1: {mesafe_merkez1:.2f}, Mesafe 2: {mesafe_merkez2:.2f})")
        else:
            hangi_kume.append(2)  # 2. merkeze daha yakın
            print(f"{il_isimleri[i]} -> 2. Kümeye atandı (Mesafe 1: {mesafe_merkez1:.2f}, Mesafe 2: {mesafe_merkez2:.2f})")
            
    # 4. ADIM: Merkezleri Güncelleme (Ortalama Alma)
    # 1. kümeye düşen illerin enlem ve boylamlarının ortalamasını bulup yeni Merkez 1 yapacağız.
    # 2. kümeye düşen illerin ortalamasını bulup yeni Merkez 2 yapacağız.
    
    kume1_enlem_toplam = 0.0
    kume1_boylam_toplam = 0.0
    kume1_eleman_sayisi = 0
    
    kume2_enlem_toplam = 0.0
    kume2_boylam_toplam = 0.0
    kume2_eleman_sayisi = 0
    
    # 7 ili gezip kümelerine göre koordinatları topluyoruz
    for i in range(7):
        if hangi_kume[i] == 1:
            kume1_enlem_toplam = kume1_enlem_toplam + enlemler[i]
            kume1_boylam_toplam = kume1_boylam_toplam + boylamlar[i]
            kume1_eleman_sayisi = kume1_eleman_sayisi + 1
        else:
            kume2_enlem_toplam = kume2_enlem_toplam + enlemler[i]
            kume2_boylam_toplam = kume2_boylam_toplam + boylamlar[i]
            kume2_eleman_sayisi = kume2_eleman_sayisi + 1
            
    # Yeni merkez koordinatlarını (ortalamalarını) hesaplıyoruz
    if kume1_eleman_sayisi > 0:
        merkez1_enlem = kume1_enlem_toplam / kume1_eleman_sayisi
        merkez1_boylam = kume1_boylam_toplam / kume1_eleman_sayisi
        
    if kume2_eleman_sayisi > 0:
        merkez2_enlem = kume2_enlem_toplam / kume2_eleman_sayisi
        merkez2_boylam = kume2_boylam_toplam / kume2_eleman_sayisi
        
    print(f"\n{adim + 1}. Adım Sonunda Yeni Merkez 1:", round(merkez1_enlem, 4), round(merkez1_boylam, 4))
    print(f"{adim + 1}. Adım Sonunda Yeni Merkez 2:", round(merkez2_enlem, 4), round(merkez2_boylam, 4))


# ==============================================================================
# 5. ADIM: Sonuçları Görselleştirme (Basit Grafik Çizimi)
# ==============================================================================

# 1. kümedeki illerin x ve y koordinatları
kume1_x = []
kume1_y = []

# 2. kümedeki illerin x ve y koordinatları
kume2_x = []
kume2_y = []

for i in range(7):
    if hangi_kume[i] == 1:
        kume1_x.append(boylamlar[i])
        kume1_y.append(enlemler[i])
    else:
        kume2_x.append(boylamlar[i])
        kume2_y.append(enlemler[i])

# Grafiğe noktaları basalım
# 1. Küme Mavi, 2. Küme Kırmızı olsun
plt.scatter(kume1_x, kume1_y, color="blue", label="1. Küme İlleri", s=70)
plt.scatter(kume2_x, kume2_y, color="red", label="2. Küme İlleri", s=70)

# Merkezleri de siyah çarpı ile gösterelim
plt.scatter([merkez1_boylam], [merkez1_enlem], color="black", marker="x", s=150, label="1. Merkez")
plt.scatter([merkez2_boylam], [merkez2_enlem], color="black", marker="x", s=150, label="2. Merkez")

# Hangi noktanın hangi il olduğunu yanına yazdıralım
for i in range(7):
    plt.text(boylamlar[i] + 0.1, enlemler[i] + 0.1, il_isimleri[i], fontsize=9)

plt.title("İlk 7 İl İçin K-Means Mantığı (k = 2)")
plt.xlabel("Boylam (Doğu - Batı)")
plt.ylabel("Enlem (Kuzey - Güney)")
plt.legend()
plt.grid(True)
plt.show()
