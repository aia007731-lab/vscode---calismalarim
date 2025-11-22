def test():
    if (True and (False or (True and False))):
        print("🌈 Renkli parantezler!")
        return (1 + (2 * (3 + 4)))

# Karmaşık örnek
sonuc = ((1 + 2) * (3 + 4)) + ((5 - 6) * (7 + 8))
print(f"Sonuç: {sonuc}")