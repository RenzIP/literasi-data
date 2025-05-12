import random

# Target ID tersembunyi (tidak diketahui oleh penyerang)
target_id = "renz"  # Contoh ID yang ingin ditemukan

def brute_force_simulasi(prefix="", digit=4):
    attempts = 0
    tried = set()

    while True:
        guess_number = ''.join(random.choices("abcrenzopq", k=digit))
        guess = prefix + guess_number

        if guess in tried:
            continue
        tried.add(guess)

        print(f"Mencoba: {guess}")
        attempts += 1

        if guess == target_id:
            print(f"\n[✓] ID ditemukan setelah {attempts} percobaan: {guess}")
            break

brute_force_simulasi()
