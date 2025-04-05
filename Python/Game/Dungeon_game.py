from data_dungeonGame import*
from time import*
class hero():
    def __init__(self, nama, health, armour, senjata, damage):
        self.nama = nama
        self.health = health
        self.armor = armour
        self.senjata = senjata
        self.serangan = damage
    def info(self):
        print('Nama Karakter:', self.nama)
        print('Health:', self.health)
        print('Armour:', self.armor)
        print('Senjata:', self.senjata)
        print('Damage:', self.serangan, '\n')
    def serang(self, enemy):
        print('--> SERANG')
        print(self.nama, 'menyerang', enemy.nama, 'menggunakan', self.senjata, '\n')
        enemy.armor -= self.serangan
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armour = 0
        print(enemy.nama , 'terkena serangan')
        print('Armour drop ke', enemy.armor)
        print('Health drop ke', enemy.health, '\n')
        if enemy.health <= 0:
            print(enemy.nama, 'Kamu mati')
    def regen(self):
            if self.health <100:
                self.health += 20
                print('Health behasil dipulihkan menjadi:', self.health)
            elif self.health == 100:
                print('Health Sudah Full', self.health)

masukkan_nama = input('Masukkan Nama:')
print('1 - Pedang Bengkulu\n2 - Tombak Mahkota Simprug')
pilih_senjata = input('Pilih salah satu senjata (ketik angka senjata yang dipilih)')
if pilih_senjata in data_senjata:
    nama_senjata = data_senjata[pilih_senjata]['nama_senjata']
    damage_senjata = data_senjata[pilih_senjata]['Damage']

MC = hero(masukkan_nama, 100, 50, nama_senjata, damage_senjata)
orang_jahat = hero('Z', 100, 50, 'Sabit Sunda', 20)
MC.info()
orang_jahat.info()
print('Z itu musuh')
sleep(0.5)
print('1 - Serang\n2 - Regen')
gerak = input('Apa yang ingin kamu lakukan (ketik angka untuk gerakan yang dipilih)')
sleep(0.5)
if gerak == '1':
    MC.serang(orang_jahat)
elif gerak == '2':
    MC.regen()