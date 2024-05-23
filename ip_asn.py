import requests

# Ganti dengan nomor ASN yang ingin Anda cari
ASN_NUMBER = '197207'

# URL untuk mendapatkan informasi ASN dari RIPEstat API
url = f"https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS{ASN_NUMBER}"

# Mengirim request ke API
response = requests.get(url)

# Memeriksa apakah request berhasil
if response.status_code == 200:
    data = response.json()
    prefixes = data.get('data', {}).get('prefixes', [])

    if prefixes:
        # Membuka file untuk menulis hasil
        with open('Blokir_ASN.txt', 'w') as file:
            for prefix in prefixes:
                if 'prefix' in prefix:
                    file.write(f"/ip firewall address-list add list=Blokir_ASN address={prefix['prefix']} comment=\"AS{ASN_NUMBER}\"\n")
        print(f"Daftar prefix berhasil disimpan di Blokir_ASN.txt")
    else:
        print(f"Tidak ada prefix yang ditemukan untuk ASN {ASN_NUMBER}")
else:
    print(f"Gagal mendapatkan data untuk ASN {ASN_NUMBER}, status code: {response.status_code}")
