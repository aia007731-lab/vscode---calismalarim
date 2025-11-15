import random

print("TAŞ-KAĞIT-MAKAS OYUNU")
print("3 raund oynayalım!")

secenekler = ["taş", "kağıt", "makas"]
oyuncu_skor = 0
bilgisayar_skor = 0

for raund in range(1, 4):
    print(f"\n{raund}. Raund:")
    
    # Oyuncu seçimi - geçerli mi?
    while True:
        secim = input("Seçimin (taş/kağıt/makas): ").lower()
        if secim in secenekler:
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

# Final sonuç
print(f"\n🏁 SONUÇ: Sen {oyuncu_skor} - Bilgisayar {bilgisayar_skor}")
if oyuncu_skor > bilgisayar_skor:
    print("Tebrikler! Oyunu sen kazandın!")
elif oyuncu_skor < bilgisayar_skor:
    print("Bilgisayar kazandı!")
else:
    print("Berabere bitti!")