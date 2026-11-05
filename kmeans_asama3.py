import math
import random
import matplotlib.pyplot as plt

# ==============================================================================
# AŞAMA 3: OPTİMİZE EDİLMİŞ K-MEANS ALGORİTMASI (81 İL, k = 7)
# Kendi merkezlerini rastgele seçer, yakınsayınca (durma kriteri) otomatik durur.
# ==============================================================================

# 1. ADIM: 81 İlin İsim ve Koordinat Verisi
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

# Koordinatlar: [Enlem, Boylam]
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

# 2. ADIM: Otomatik ve Rastgele 7 Merkez Seçimi
K = 7

# Her çalıştırmada tutarlı sonuç alıp incelemek istersen seed verebilirsin (örn: random.seed(42))
# Tamamen her seferinde farklı rastgele merkezler istiyorsan seed satırını yorumda bırakabilirsin.
random.seed(42)

# 81 il arasından birbirinden farklı 7 ilin indeksini rastgele seçiyoruz
rastgele_indeksler = random.sample(range(len(koordinatlar)), K)

merkezler = []
for idx in rastgele_indeksler:
    # Seçilen ilin [enlem, boylam] değerini kopya olarak merkeze alıyoruz
    merkezler.append([koordinatlar[idx][0], koordinatlar[idx][1]])

print("--- BAŞLANGIÇTA RASTGELE SEÇİLEN 7 MERKEZ İL ---")
for i in range(K):
    il_adi = il_isimleri[rastgele_indeksler[i]]
    print(f"Merkez {i + 1} ({il_adi}): Enlem={merkezler[i][0]}, Boylam={merkezler[i][1]}")
print("=" * 70)


# 3. ADIM: Optimize Yakınsama Döngüsü (Convergence Loop)
# Sabit döngü sayısı yerine, sistem kararlı hale gelene kadar döner (En fazla 100 tur emniyet payı).
max_iterasyon = 100

# Önceki turdaki atamaları saklayıp karşılaştırma yapacağız
onceki_atamalar = [-1] * len(koordinatlar)

for iterasyon in range(max_iterasyon):
    # Bu turdaki atamaları tutacak liste
    su_anki_atamalar = []
    
    # Adım 3A: Her ili en yakın merkeze ata
    for i in range(len(koordinatlar)):
        il_enlem = koordinatlar[i][0]
        il_boylam = koordinatlar[i][1]
        
        en_yakin_mesafe = float("inf") # Sonsuz büyük sayı ile başlatma
        en_yakin_merkez_id = -1
        
        for m in range(K):
            fark_enlem = il_enlem - merkezler[m][0]
            fark_boylam = il_boylam - merkezler[m][1]
            
            # Mesafe karşılaştırmasında karekök almak işlem maliyeti yaratır.
            # a^2 + b^2 karşılaştırması sıralamayı değiştirmez (Optimizasyon adımı).
            kare_mesafe = (fark_enlem ** 2) + (fark_boylam ** 2)
            
            if kare_mesafe < en_yakin_mesafe:
                en_yakin_mesafe = kare_mesafe
                en_yakin_merkez_id = m
                
        su_anki_atamalar.append(en_yakin_merkez_id)
        
    # Adım 3B: Yakınsama Kontrolü (Erken Durma / Early Stopping)
    # Eğer hiçbir ilin kümesi bir önceki tura göre değişmediyse merkezler artık oynamaz, döngü biter.
    if su_anki_atamalar == onceki_atamalar:
        print(f"\n[BİLGİ] Algoritma {iterasyon}. iterasyonda kararlı hale geldi (Yakınsadı/Converged).")
        break
        
    # Değişiklik varsa bir sonraki kontrol için kaydet
    onceki_atamalar = list(su_anki_atamalar)
    
    # Adım 3C: Kümelerin Ağırlık Merkezini Hesaplayıp Güncelleme
    enlem_toplamlari = [0.0] * K
    boylam_toplamlari = [0.0] * K
    eleman_sayilari = [0] * K
    
    for i in range(len(koordinatlar)):
        kume_id = su_anki_atamalar[i]
        enlem_toplamlari[kume_id] += koordinatlar[i][0]
        boylam_toplamlari[kume_id] += koordinatlar[i][1]
        eleman_sayilari[kume_id] += 1
        
    for m in range(K):
        # Kümeye en az 1 il düşmüşse merkezini o illerin ortalamasına taşı
        if eleman_sayilari[m] > 0:
            merkezler[m][0] = enlem_toplamlari[m] / eleman_sayilari[m]
            merkezler[m][1] = boylam_toplamlari[m] / eleman_sayilari[m]

print("\n--- NİHAİ 7 KÜME MERKEZİ KOORDİNATLARI ---")
for m in range(K):
    print(f"Küme {m + 1} -> İlin Sayısı: {eleman_sayilari[m]}, Merkez: [Enlem: {merkezler[m][0]:.4f}, Boylam: {merkezler[m][1]:.4f}]")


# ==============================================================================
# 4. ADIM: Sonuçları Görselleştirme ve Gerçek Bölgelerle Karşılaştırma
# ==============================================================================
renkler = ["#e6194b", "#3cb44b", "#ffe119", "#4363d8", "#f58231", "#911eb4", "#46f0f0"]

plt.figure(figsize=(15, 8))

# İlleri kümelerine göre çizdirme
for i in range(len(koordinatlar)):
    kume_id = onceki_atamalar[i]
    plt.scatter(koordinatlar[i][1], koordinatlar[i][0], color=renkler[kume_id], s=45)
    plt.text(koordinatlar[i][1] + 0.08, koordinatlar[i][0] + 0.08, il_isimleri[i], fontsize=6.5, alpha=0.75)

# Nihai merkezleri büyük siyah X ile işaretleme
for m in range(K):
    plt.scatter(merkezler[m][1], merkezler[m][0], color="black", marker="X", s=180, edgecolors="white", linewidth=1.5)

plt.title("81 İlin K-Means ile Optimize 7 Kümeye Ayrılması (Otomatik Merkez & Erken Durma)")
plt.xlabel("Boylam (°D)")
plt.ylabel("Enlem (°K)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
