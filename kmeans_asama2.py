import math
import matplotlib.pyplot as plt

# 81 İL İÇİN K-MEANS DENEMESİ

# 1. ADIM: 81 İlin İsimleri ve Koordinatları
il_isimleri = [
    "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir",
    "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli",
    "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari",
    "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir",
    "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir",
    "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat",
    "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman",
    "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
]

# Enlemler ve boylamlar 
koordinatlar = [
    [37.0000, 35.3213], [37.7648, 38.2786], [38.7507, 30.5567], [39.7191, 43.0503], [40.6501, 35.8353],
    [39.9334, 32.8597], [36.8969, 30.7133], [41.1828, 41.8183], [37.8560, 27.8416], [39.6484, 27.8826],
    [40.1451, 29.9799], [38.8847, 40.4939], [38.4006, 42.1095], [40.7350, 31.6061], [37.7203, 30.2889],
    [40.1885, 29.0610], [40.1553, 26.4142], [40.6013, 33.6134], [40.5506, 34.9556], [37.7765, 29.0864],
    [37.9144, 40.2306], [41.6772, 26.5557], [38.6810, 39.2264], [39.7500, 39.5000], [39.9043, 41.2679],
    [39.7767, 30.5206], [37.0662, 37.3833], [40.9128, 38.3895], [40.4600, 39.4700], [37.5833, 43.7333],
    [36.2023, 36.1606], [37.7648, 30.5566], [36.8000, 34.6333], [41.0082, 28.9784], [38.4192, 27.1287],
    [40.6013, 43.0975], [41.3887, 33.7827], [38.7312, 35.4853], [41.7333, 27.2167], [39.1425, 34.1709],
    [40.7667, 29.9167], [37.8667, 32.4833], [39.4167, 29.9833], [38.3552, 38.3095], [38.6191, 27.4289],
    [37.5858, 36.9371], [37.3212, 40.7245], [37.2153, 28.3636], [38.7432, 41.5064], [38.6244, 34.7144],
    [37.9667, 34.6833], [40.9839, 37.8764], [41.0201, 40.5206], [40.7569, 30.3783], [41.2928, 36.3313],
    [37.9333, 41.9500], [42.0231, 35.1531], [39.7477, 37.0179], [40.9833, 27.5167], [40.3167, 36.5500],
    [41.0015, 39.7178], [39.1079, 39.5401], [37.1591, 38.7969], [38.6823, 29.4082], [38.4891, 43.4089],
    [39.8181, 34.8147], [41.4564, 31.7987], [38.3687, 34.0370], [40.2552, 40.2249], [37.1759, 33.2287],
    [39.8468, 33.5153], [37.8812, 41.1294], [37.5164, 42.4918], [41.6344, 32.3375], [41.1105, 42.7022],
    [39.9196, 44.0450], [40.6500, 29.2769], [41.2061, 32.6204], [36.7184, 37.1147], [37.0742, 36.2467],
    [40.8438, 31.1565]
]

# 2. ADIM: 7 Tane İl Seçip Başlangıç Merkezi Yapma
# 7 bölge için 7 tane ili elle göz kararı seçtim.
# 5: Ankara, 33: İstanbul, 34: İzmir, 6: Antalya, 54: Samsun, 24: Erzurum, 20: Diyarbakır
# Döngüyle tek seferde almak yerine tek tek çektim:
m0 = [koordinatlar[5][0], koordinatlar[5][1]]    # Ankara
m1 = [koordinatlar[33][0], koordinatlar[33][1]]  # İstanbul
m2 = [koordinatlar[34][0], koordinatlar[34][1]]  # İzmir
m3 = [koordinatlar[6][0], koordinatlar[6][1]]    # Antalya
m4 = [koordinatlar[54][0], koordinatlar[54][1]]  # Samsun
m5 = [koordinatlar[24][0], koordinatlar[24][1]]  # Erzurum
m6 = [koordinatlar[20][0], koordinatlar[20][1]]  # Diyarbakır
merkezler = [m0, m1, m2, m3, m4, m5, m6]

print("Seçtiğim ilk 7 merkez:")
for sayac in range(7):
    print("Merkez", sayac, "=", merkezler[sayac])
print("--------------------------------------------------")

# 3. ADIM: Kümeleme ve Merkez Güncelleme Döngüsü
# 8 kere dönsün??
adim_sayisi = 8

for adim in range(adim_sayisi):
    print("Döngü Adımı:", adim + 1)
    
    kume_sonuclari = []  # Hangi il hangi merkeze gitti onu tutacak
    
    # 81 ili tek tek gezip mesafeleri buluyorum
    for i in range(81):
        il_x = koordinatlar[i][1]  # boylam
        il_y = koordinatlar[i][0]  # enlem
        
        # 7 merkeze olan mesafeleri tek tek hesaplatıyorum 
        d0 = math.sqrt((il_y - merkezler[0][0])**2 + (il_x - merkezler[0][1])**2)
        d1 = math.sqrt((il_y - merkezler[1][0])**2 + (il_x - merkezler[1][1])**2)
        d2 = math.sqrt((il_y - merkezler[2][0])**2 + (il_x - merkezler[2][1])**2)
        d3 = math.sqrt((il_y - merkezler[3][0])**2 + (il_x - merkezler[3][1])**2)
        d4 = math.sqrt((il_y - merkezler[4][0])**2 + (il_x - merkezler[4][1])**2)
        d5 = math.sqrt((il_y - merkezler[5][0])**2 + (il_x - merkezler[5][1])**2)
        d6 = math.sqrt((il_y - merkezler[6][0])**2 + (il_x - merkezler[6][1])**2)
        
        mesafeler = [d0, d1, d2, d3, d4, d5, d6]
        
        # En küçük mesafeyi bulma (min fonksiyonu yerine if-else mantığıyla)
        en_kucuk = mesafeler[0]
        en_yakin_kume = 0
        
        for k in range(7):
            if mesafeler[k] < en_kucuk:
                en_kucuk = mesafeler[k]
                en_yakin_kume = k
                
        kume_sonuclari.append(en_yakin_kume)
        
    # 4. ADIM: Merkezleri Tekrar Hesaplama 
    # Her küme için enlem ve boylam toplamları ile sayaçları tutuyorum:
    toplam_enlem = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    toplam_boylam = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    eleman_sayisi = [0, 0, 0, 0, 0, 0, 0]
    
    # İlleri gezip toplamları biriktir
    for i in range(81):
        kume_no = kume_sonuclari[i]
        toplam_enlem[kume_no] += koordinatlar[i][0]
        toplam_boylam[kume_no] += koordinatlar[i][1]
        eleman_sayisi[kume_no] += 1
        
    # Yeni merkezleri güncelle
    for m in range(7):
        # 0'a bölme hatası vermesin diye kontrol koydum
        if eleman_sayisi[m] != 0:
            yeni_enlem = toplam_enlem[m] / eleman_sayisi[m]
            yeni_boylam = toplam_boylam[m] / eleman_sayisi[m]
            merkezler[m] = [yeni_enlem, yeni_boylam]
        else:
            # Kümede eleman yoksa eski merkez kalsın
            pass

print("Son adımdaki güncellenmiş merkezler:")
for m in range(7):
    print("Nihai Merkez", m, ":", merkezler[m])

# 5. ADIM: Çizdirme (Basit Matplotlib Grafiği)
#İsteğe bağlı ben görmek için istedim.
renk_listesi = ["red", "blue", "green", "orange", "purple", "brown", "gray"]

plt.figure(figsize=(12, 6))

for i in range(81):
    atanan_kume = kume_sonuclari[i]
    # x ekseni boylam, y ekseni enlem
    plt.scatter(koordinatlar[i][1], koordinatlar[i][0], color=renk_listesi[atanan_kume])
    # isimleri de basalım ama çok sıkışık olabilir
    plt.text(koordinatlar[i][1], koordinatlar[i][0], il_isimleri[i], fontsize=6)

# Merkezleri büyük siyah x ile basalım
for m in range(7):
    plt.scatter(merkezler[m][1], merkezler[m][0], color="black", marker="x", s=100)

plt.title("Aşama 2: 81 İl İçin 7 Merkezli K-Means")
plt.xlabel("Boylam")
plt.ylabel("Enlem")
plt.show()


# # ==============================================================================
# # ==============================================================================
# # ==============================================================================
# # ==============================================================================


# import math
# import matplotlib.pyplot as plt

# # ==============================================================================
# # AŞAMA 2: TÜM 81 İL İÇİN K-MEANS (k = 7)
# # ==============================================================================

# # 1. ADIM: 81 İlin Koordinat Listesi
# # 81 ili tek tek ekliyoruz.
# # Kod çok karmaşıklaşmasın diye her ili [enlem, boylam] ikilisi şeklinde listede tutuyoruz.

# il_isimleri = [
#     "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir",
#     "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli",
#     "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari",
#     "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir",
#     "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir",
#     "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat",
#     "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman",
#     "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
# ]

# # Koordinatlar: [Enlem, Boylam]
# koordinatlar = [
#     [37.0000, 35.3213], [37.7648, 38.2786], [38.7507, 30.5567], [39.7191, 43.0503], [40.6501, 35.8353],
#     [39.9334, 32.8597], [36.8969, 30.7133], [41.1828, 41.8183], [37.8560, 27.8416], [39.6484, 27.8826],
#     [40.1451, 29.9799], [38.8847, 40.4939], [38.4006, 42.1095], [40.7350, 31.6061], [37.7203, 30.2889],
#     [40.1885, 29.0610], [40.1553, 26.4142], [40.6013, 33.6134], [40.5506, 34.9556], [37.7765, 29.0864],
#     [37.9144, 40.2306], [41.6772, 26.5557], [38.6810, 39.2264], [39.7500, 39.5000], [39.9043, 41.2679],
#     [39.7767, 30.5206], [37.0662, 37.3833], [40.9128, 38.3895], [40.4600, 39.4700], [37.5833, 43.7333],
#     [36.2023, 36.1606], [37.7648, 30.5566], [36.8000, 34.6333], [41.0082, 28.9784], [38.4192, 27.1287],
#     [40.6013, 43.0975], [41.3887, 33.7827], [38.7312, 35.4853], [41.7333, 27.2167], [39.1425, 34.1709],
#     [40.7667, 29.9167], [37.8667, 32.4833], [39.4167, 29.9833], [38.3552, 38.3095], [38.6191, 27.4289],
#     [37.5858, 36.9371], [37.3212, 40.7245], [37.2153, 28.3636], [38.7432, 41.5064], [38.6244, 34.7144],
#     [37.9667, 34.6833], [40.9839, 37.8764], [41.0201, 40.5206], [40.7569, 30.3783], [41.2928, 36.3313],
#     [37.9333, 41.9500], [42.0231, 35.1531], [39.7477, 37.0179], [40.9833, 27.5167], [40.3167, 36.5500],
#     [41.0015, 39.7178], [39.1079, 39.5401], [37.1591, 38.7969], [38.6823, 29.4082], [38.4891, 43.4089],
#     [39.8181, 34.8147], [41.4564, 31.7987], [38.3687, 34.0370], [40.2552, 40.2249], [37.1759, 33.2287],
#     [39.8468, 33.5153], [37.8812, 41.1294], [37.5164, 42.4918], [41.6344, 32.3375], [41.1105, 42.7022],
#     [39.9196, 44.0450], [40.6500, 29.2769], [41.2061, 32.6204], [36.7184, 37.1147], [37.0742, 36.2467],
#     [40.8438, 31.1565]
# ]

# # 2. ADIM: Başlangıçta 7 Merkez Seçimi (k = 7)
# # 1. aşamada iki il seçmiştik, şimdi Türkiye geneline yayılmış 7 ili elle başlangıç merkezi yapıyoruz.
# # Seçtiğimiz illerin indeksleri:
# # 5: Ankara, 33: İstanbul, 34: İzmir, 6: Antalya, 54: Samsun, 24: Erzurum, 20: Diyarbakır
# secilen_indeksler = [5, 33, 34, 6, 54, 24, 20]

# merkezler = []
# for idx in secilen_indeksler:
#     merkezler.append([koordinatlar[idx][0], koordinatlar[idx][1]])

# print("Başlangıçta seçilen 7 merkez:")
# for m_no in range(7):
#     print(f"{m_no + 1}. Merkez ({il_isimleri[secilen_indeksler[m_no]]}): Enlem={merkezler[m_no][0]}, Boylam={merkezler[m_no][1]}")
# print("=" * 60)


# # 3. ADIM: İlleri En Yakın Merkeze Atama ve Merkezleri Güncelleme Döngüsü
# # 81 il olduğu için dengelenmesi adına döngüyü 10 kere çalıştırıyoruz.

# toplam_adim = 10

# for adim in range(toplam_adim):
#     print(f"\n>>> DÖNGÜ ADIMI {adim + 1} BAŞLADI <<<")
    
#     # Her ilin hangi merkeze (0, 1, 2, 3, 4, 5, 6) gittiğini tutan liste
#     kume_atamalari = []
    
#     # 81 ili tek tek geziyoruz
#     for i in range(81):
#         il_enlem = koordinatlar[i][0]
#         il_boylam = koordinatlar[i][1]
        
#         en_kucuk_mesafe = 9999999.0  # Karşılaştırma yapabilmek için çok büyük bir sayı ile başlıyoruz
#         en_yakin_merkez_no = -1
        
#         # Bu ilin 7 merkezin her birine olan mesafesini tek tek buluyoruz
#         for m in range(7):
#             merkez_enlem = merkezler[m][0]
#             merkez_boylam = merkezler[m][1]
            
#             # Pisagor formülü: Uzaklık = Karekök((enlem farkı)^2 + (boylam farkı)^2)
#             fark_enlem = il_enlem - merkez_enlem
#             fark_boylam = il_boylam - merkez_boylam
#             mesafe = math.sqrt((fark_enlem ** 2) + (fark_boylam ** 2))
            
#             # Eğer hesaplanan mesafe o ana kadarki en küçük mesafeyse güncelliyoruz
#             if mesafe < en_kucuk_mesafe:
#                 en_kucuk_mesafe = mesafe
#                 en_yakin_merkez_no = m
                
#         # İl en yakın olduğu merkezin numarasına atanıyor
#         kume_atamalari.append(en_yakin_merkez_no)

#     # 4. ADIM: 7 Merkezin Yeni Koordinatlarını Hesaplama (Aritmetik Ortalama)
#     # Her bir küme için enlem ve boylam toplamlarını sıfırlıyoruz
#     enlem_toplamlari = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#     boylam_toplamlari = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#     eleman_sayilari = [0, 0, 0, 0, 0, 0, 0]
    
#     # 81 ili kontrol edip hangi kümeye düşmüşse onun toplamına ekliyoruz
#     for i in range(81):
#         kume_id = kume_atamalari[i]
#         enlem_toplamlari[kume_id] = enlem_toplamlari[kume_id] + koordinatlar[i][0]
#         boylam_toplamlari[kume_id] = boylam_toplamlari[kume_id] + koordinatlar[i][1]
#         eleman_sayilari[kume_id] = eleman_sayilari[kume_id] + 1
        
#     # Ortalamaları alıp merkezler listesini güncelliyoruz
#     for m in range(7):
#         if eleman_sayilari[m] > 0:
#             merkezler[m][0] = enlem_toplamlari[m] / eleman_sayilari[m]
#             merkezler[m][1] = boylam_toplamlari[m] / eleman_sayilari[m]
#             print(f"Merkez {m + 1} Güncellendi -> İlin sayısı: {eleman_sayilari[m]}, Yeni Koordinat: [{merkezler[m][0]:.4f}, {merkezler[m][1]:.4f}]")


# # ==============================================================================
# # 5. ADIM: Sonuçları 81 İl İçin Harita Üzerinde Çizdirme
# # ==============================================================================

# # 7 farklı küme için 7 ayrı renk belirliyoruz
# renkler = ["red", "blue", "green", "orange", "purple", "brown", "cyan"]

# plt.figure(figsize=(15, 8))

# # 81 ili ait oldukları kümenin rengiyle tek tek grafiğe ekliyoruz
# for i in range(81):
#     il_kumesi = kume_atamalari[i]
#     il_rengi = renkler[il_kumesi]
    
#     # X ekseni: Boylam, Y ekseni: Enlem
#     plt.scatter(koordinatlar[i][1], koordinatlar[i][0], color=il_rengi, s=50)
    
#     # İl isimlerini grafiğe küçük yazılarla ekliyoruz
#     plt.text(koordinatlar[i][1] + 0.08, koordinatlar[i][0] + 0.08, il_isimleri[i], fontsize=7, alpha=0.8)

# # Son olarak güncellenen 7 yeni merkezi siyah çarpı (X) ile çizdiriyoruz
# for m in range(7):
#     plt.scatter(merkezler[m][1], merkezler[m][0], color="black", marker="x", s=180, linewidth=2)

# plt.title("81 İlin 7 Merkeze Göre K-Means ile Kümelenmesi (Aşama 2)")
# plt.xlabel("Boylam (Doğu - Batı)")
# plt.ylabel("Enlem (Kuzey - Güney)")
# plt.grid(True, linestyle="--", alpha=0.6)
# plt.tight_layout()
# plt.show()
