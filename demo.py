# ilk-ders
sozluk = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in sozluk.keys():
    print(sozluk[word])
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    print("yardımcı olamiycam")
    # Kelime eşleşmiyorsa ne yapmalıyız?
