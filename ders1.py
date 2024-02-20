meme_dict = {
            "LOL" : "komik bir şeye verilen cevap",
            "CRINGE" : "garip ya da utandırıcı bir şey",
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak",
            "CREEPY" : "korkunç",
            "AGGRO" :" agresifleşmek/sinirlenmek"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")  
while True:
    if word in meme_dict.keys():
        # Kelime eşleşiyorsa ne yapmalıyız?
        print(meme_dict[word])
    else:
        # Kelime eşleşmiyorsa ne yapmalıyız?
        print("bu kelimeyi bende bilmiyorum")
