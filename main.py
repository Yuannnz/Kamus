meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "YTTA": "YTTA, Yang Tau Tau Aja",
            }
            
word = input("Ketik kata yang tidak Kamu mengerti ( Gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print("Makna kata", word, "adalah", meme_dict[word])
else:
    print("Makna kata tidak ditemukan")
