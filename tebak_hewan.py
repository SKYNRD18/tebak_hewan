# Program Tebak Hewan Berdasarkan Ciri-Ciri

# List hewan dengan ciri-cirinya
hewan_dan_ciri = {
    "gajah": ["memiliki belalai", "berukuran besar", "tinggal di darat"],
    "singa": ["raja hutan", "memiliki surai", "pemangsa"],
    "ikan paus": ["hidup di laut", "berukuran sangat besar", "mamalia laut"],
    "burung elang": ["memiliki sayap", "pemangsa dari udara", "tajam penglihatannya"],
    "kura-kura": ["memiliki tempurung", "bergerak lambat", "hidup di darat dan air"],
}

# Fungsi untuk memulai permainan
def tebak_hewan():
    print("Selamat datang di permainan tebak hewan!")
    print("Saya akan memberi ciri-ciri hewan, dan kamu harus menebak hewannya.")
    print("Ketik 'akhiri' kapan saja jika ingin mengakhiri permainan.\n")
    
    # Loop untuk setiap hewan dalam dictionary
    for hewan, ciri_list in hewan_dan_ciri.items():
        print("Tebak hewan apa ini berdasarkan ciri-cirinya:")
        for ciri in ciri_list:
            print("- " + ciri)
        
        # Input jawaban dari pengguna
        jawaban = input("Masukkan tebakan kamu atau ketik 'akhiri' untuk keluar: ").lower()
        
        # Cek apakah pengguna ingin mengakhiri permainan
        if jawaban == "akhiri":
            print("Permainan diakhiri. Terima kasih sudah bermain!")
            return  # Keluar dari fungsi untuk mengakhiri permainan
        
        # Cek jawaban
        if jawaban == hewan:
            print("Benar! Hewan tersebut adalah", hewan.capitalize(), "\n")
        else:
            print("Salah. Hewan yang benar adalah", hewan.capitalize(), "\n")
    
    print("Permainan selesai. Terima kasih sudah bermain!")

# Memulai program hanya jika pengguna mengetik "mulai"
perintah = input("Ketik 'mulai' untuk memulai permainan: ").lower()
if perintah == "mulai":
    tebak_hewan()
else:
    print("Permainan dibatalkan. Ketik 'mulai' jika ingin bermain lain kali.")
