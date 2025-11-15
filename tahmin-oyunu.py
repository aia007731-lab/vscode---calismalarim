import random

# İSTATİSTİKLER -Oyun başında
toplam_oyun = 0
toplam_galibiyet = 0
secim_sayaci = {"taş": 0, "kağıt": 0, "makas": 0}

while True:
    # İstatistik gösterimi
    print(f"\nToplam oyun: {toplam_oyun} | ", end=""
    if toplam_oyun > 0:
        print(f"Kazanma: %{toplam_galibiyet/toplam_oyun*100:.1f}")
    else:
        print("İlk oyununuz!")

    print("\n3 raund oynayalım!")

    secenekler = ["taş", "kağıt", "makas"]
    oyuncu_skor = 0
    bilgisayar_skor = 0

    # 3 raund
    for raund in range(1, 4):
        print(f"\n{raund}. Raund:")
        
        # Oyuncu seçimi + istatistik
        while True:
            secim = input("Seçimin (taş/kağıt/makas): ").lower()
            if secim in secenekler:
                secim_sayaci[secim] += 1 # İstatistik için
                break
            print("Geçersiz! Tekrar dene.")
    
        # Bilgisayar seçimi
        bilgisayar = random.choice(secenekler)
        print(f"Bilgisayar: {bilgisayar}")
    
        # Kazananı belirle
        if secim == bilgisayar:
            print("Berabere!")
        elif (secim == "taş" and bilgisayar == "makas") or \
         (secim == "makas" and bilgisayar == "kağıt") or \
         (secim == "kağıt" and bilgisayar == "taş"):
            print("Sen kazandın!")
            oyuncu_skor += 1
        else:
            print("Bilgisayar kazandı!")
            bilgisayar_skor += 1

    # Sonuç + istatistik güncelleme
    toplam_oyun += 1
    if oyuncu_skor > bilgisayar_skor:
        toplam_galibiyet += 1
        print("Kazandın!")
    elif oyuncu_skor < bilgisayar_skor:
        print("Kaybettin!")
    else:
        print("Berabere!")

    # En çok kullanılan seçim
    en_cok = max(secim_sayaci, key=secim_sayaci.get)
    print(f"En çok kullandığınız: {en_cok} ({secim_sayaci[en_cok]} kez)")

    # Tekrar oyna döngüsü
    while True:
        devam = input("\nTekrar oynamak ister misin? (e/h): ").lower()
        if devam == 'e':
            break  
        elif devam == 'h':
            print("Güle güle! Yine bekleriz.")
            print(f"Toplam oyun: {toplam_oyun}")
            print(f"Galibiyet: {toplam_galibiyet}")
            print(f"Kazanma oranı: %{toplam_galibiyet/toplam_oyun*100:.1f}")
            exit()  # Programdan çık
        else:
            print("Lütfen 'e' veya 'h' yaz!")


