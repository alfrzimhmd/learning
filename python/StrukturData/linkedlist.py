# Mendefinisikan kelas Node untuk merepresentasikan setiap node dalam linked list
class Node:
    def __init__(self, data):
        # Inisialisasi node dengan data yang diberikan
        self.data = data  # Menyimpan data di node
        self.next = None  # Pointer ke node berikutnya, awalnya None

# Mendefinisikan kelas LinkedList untuk mengelola linked list
class LinkedList:
    def __init__(self):
        # Inisialisasi linked list dengan head (kepala) yang awalnya None
        self.head = None  

    def tambah_awal(self, data):
        # Menambahkan node baru di awal linked list
        new_node = Node(data)  # Membuat node baru dengan data
        new_node.next = self.head  # Node baru menunjuk ke head sebelumnya
        self.head = new_node  # Head sekarang menjadi node baru

    def tambah_akhir(self, data):
        # Menambahkan node baru di akhir linked list
        new_node = Node(data)  # Membuat node baru dengan data
        if self.head is None:  # Jika linked list kosong
            self.head = new_node  # Node baru menjadi head
            return

        last = self.head  # Mulai dari head
        while last.next:  # Loop hingga mencapai node terakhir (next-nya None)
            last = last.next  
        last.next = new_node  # Node terakhir menunjuk ke node baru

    def tampil(self):
        # Menampilkan isi linked list
        temp = self.head  # Mulai dari head
        while temp:  # Loop selama temp tidak None (belum mencapai akhir)
            print(temp.data, end=" -> ")  # Print data node
            temp = temp.next  # Pindah ke node berikutnya
        print("None")  # Menandakan akhir linked list
    
    def tambah_tengah(self, data_sebelum, data_baru):
        """Menambahkan node baru setelah node dengan data tertentu."""
        
        if self.head is None:  # Jika linked list kosong
            print("List kosong, tidak bisa menambahkan di tengah.")
            return
        
        current = self.head
        while current and current.data != data_sebelum:
            current = current.next
        
        if current is None:  # Jika data_sebelum tidak ditemukan
            print(f"Node dengan data '{data_sebelum}' tidak ditemukan.")
            return

        new_node = Node(data_baru)
        new_node.next = current.next
        current.next = new_node

# Program utama
# Membuat objek linked list
linked_list = LinkedList()  

# Menambahkan data ke linked list
linked_list.tambah_awal("Malaikat") 
linked_list.tambah_akhir("Hawa") 
linked_list.tambah_awal("Iblis") 
linked_list.tambah_tengah("Malaikat", "Adam")


print("Linked List:")  
linked_list.tampil()