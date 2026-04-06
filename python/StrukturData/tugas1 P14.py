# Daftar siswa
siswa = [
    {"nama": "Andi", "nilai": 85, "kelas": "X-A"},
    {"nama": "Budi", "nilai": 90, "kelas": "X-A"},
    {"nama": "Cici", "nilai": 85, "kelas": "X-B"},
    {"nama": "Dewi", "nilai": 95, "kelas": "X-B"},
    {"nama": "Eka",  "nilai": 90, "kelas": "X-C"}
]

# Insertion Sort: berdasarkan nilai (descending), lalu nama (ascending)
def insertion_sort_siswa(data):
    arr = data.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and (
            (arr[j]['nilai'] < key['nilai']) or
            (arr[j]['nilai'] == key['nilai'] and arr[j]['nama'] > key['nama'])
        ):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Sebelum diurutkan
print("Data Siswa (belum diurutkan):")
for s in siswa:
    print(f"{s['nama']} - Nilai: {s['nilai']} - Kelas: {s['kelas']}")

# Sesudah diurutkan
sorted_siswa = insertion_sort_siswa(siswa)
print("\nData Siswa setelah diurutkan (nilai desc, nama asc):")
for s in sorted_siswa:
    print(f"{s['nama']} - Nilai: {s['nilai']} - Kelas: {s['kelas']}")
