def calculate_happiness(
    P_red, P_pisman, P_daha_guzel, P_hayal_kirkligi,
    Beklenti_karsilanmasi, Hayal_kirkligi, Yeni_heyecan,
    Mevcut_durum, Üzüntü, Pişmanlık, Nötr
):
    P_kabul = 1 - P_red
    P_rahat = 1 - P_pisman
    P_beklenti = 1 - P_hayal_kirkligi

    # Kıza Açılma Durumu (İtiraf)
    itiraf_mutluluk = (
        (P_kabul * (
            (P_beklenti * Beklenti_karsilanmasi) +
            (P_hayal_kirkligi * Hayal_kirkligi) +
            (P_daha_guzel * Yeni_heyecan) +
            ((1 - P_daha_guzel) * Mevcut_durum)
        )) +
        (P_red * Üzüntü)
    )

    # Kıza Açılmama Durumu (Pişmanlık)
    pismanlik_mutluluk = (
        (P_pisman * Pişmanlık) +
        (P_rahat * Nötr)
    )

    return itiraf_mutluluk, pismanlik_mutluluk

# Kullanıcıdan gerekli değerleri alıyoruz.
P_red = float(input("Red edilme olasılığı (0 ile 1 arasında): "))
P_pisman = float(input("Konuşmazsan pişman olma olasılığı (0 ile 1 arasında): "))
P_daha_guzel = float(input("Daha güzel bir kadın görme olasılığı (0 ile 1 arasında): "))
P_hayal_kirkligi = float(input("Hayal kırıklığı olasılığı (0 ile 1 arasında): "))
Beklenti_karsilanmasi = float(input("Beklenti karşılanması değeri (0 ile 100 arasında): "))
Hayal_kirkligi = float(input("Hayal kırıklığı değeri (0 ile 100 arasında): "))
Yeni_heyecan = float(input("Daha güzel bir kadın bulmanın getireceği heyecan değeri (0 ile 100 arasında): "))
Mevcut_durum = float(input("Mevcut durumda kalmanın getireceği mutluluk değeri (0 ile 100 arasında): "))
Üzüntü = float(input("Reddedilme sonucu üzüntü değeri (0 ile 100 arasında): "))
Pişmanlık = float(input("Konuşmama sonucu pişmanlık değeri (0 ile 100 arasında): "))
Nötr = float(input("Konuşmama sonucu nötr değer (0 ile 100 arasında): "))

# Beklenen mutluluk hesaplanıyor.
itiraf_mutluluk, pismanlik_mutluluk = calculate_happiness(
    P_red, P_pisman, P_daha_guzel, P_hayal_kirkligi,
    Beklenti_karsilanmasi, Hayal_kirkligi, Yeni_heyecan,
    Mevcut_durum, Üzüntü, Pişmanlık, Nötr
)

# Sonuç yüzdelik halde yazdırılıyor.
print(f"İtiraf Durağındaki Beklenen Mutluluk: {itiraf_mutluluk:.2f}%")
print(f"Pişmanlık Durağındaki Beklenen Mutluluk: {pismanlik_mutluluk:.2f}%")
