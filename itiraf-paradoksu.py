# Kullanıcıdan gerekli değerleri alıyoruz.
P_red = float(input("Red edilme olasılığı (0 ile 1 arasında): "))
P_kabul = 1 - P_red  # Kabul edilme olasılığı
P_pişman = float(input("Konuşmazsan pişman olma olasılığı (0 ile 1 arasında): "))
P_rahat = 1 - P_pişman  # Konuşmazsan pişman olmama olasılığı
P_daha_guzel = float(input("Daha güzel bir kadın görme olasılığı (0 ile 1 arasında): "))
P_hayal_kirikligi = float(input("Hayal kırıklığı olasılığı (0 ile 1 arasında): "))
P_beklenti = 1 - P_hayal_kirikligi  # Beklenti karşılanması olasılığı

# Kullanıcıdan duygusal değerleri alıyoruz.
Üzüntü = float(input("Reddedilme sonucu üzüntü değeri (0 ile 100 arasında): "))
Pişmanlık = float(input("Konuşmama sonucu pişmanlık değeri (0 ile 100 arasında): "))
Nötr = float(input("Konuşmama sonucu nötr değer (0 ile 100 arasında): "))
Hayal_kirikligi = float(input("Hayal kırıklığı değeri (0 ile 100 arasında): "))
Beklenti_karşılanması = float(input("Beklenti karşılanması değeri (0 ile 100 arasında): "))
Yeni_heyecan = float(input("Daha güzel bir kadın bulmanın getireceği heyecan değeri (0 ile 100 arasında): "))
Mevcut_durum = float(input("Mevcut durumda kalmanın getireceği mutluluk değeri (0 ile 100 arasında): "))

# Beklenen mutluluk hesaplanıyor.
M = (P_kabul * ((P_beklenti * Beklenti_karşılanması) + (P_hayal_kirikligi * Hayal_kirikligi) + 
     (P_daha_guzel * Yeni_heyecan) + ((1 - P_daha_guzel) * Mevcut_durum))) + \
    (P_red * Üzüntü) + (P_pişman * Pişmanlık) + (P_rahat * Nötr)

# Sonuç yüzdelik halde yazdırılıyor.
print(f"Beklenen mutluluk: {M:.2f}%")
