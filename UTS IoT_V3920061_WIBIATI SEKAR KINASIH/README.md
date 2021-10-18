# Penjelasan Alur Simulasi
Tema yang digunakan pada simulasi IoT ini adalah Smart Home.

Pada simulasi ini terbagi menjadi 4 ruangan, di mana setiap ruangan memiliki home device. 

1.	Garage

Jika CO2 Detector mendeteksi adanya CO2, maka Garage Door dan Window akan terbuka. CO2 terdeteksi saat levelnya bernilai 0,1. Jika CO2 memiliki level < 0,1 artinya tidak akan terdeteksi oleh CO2 Detector sehingga Garage Door dan Window tidak terbuka.

2.	Bedroom

Jika Motion Detector mendeteksi adanya gerakan maka Door terbuka, Lamp dan AC menyala. Namun, jika Motion Detector tidak mendeteksi adanya gerakan maka Door tertutup, Lamp dan AC mati.

3.	Living Room

Jika Motion Detector mendeteksi adanya gerakan maka Fan, Lamp, dan Humidifier menyala. Namun, jika Motion Detector tidak mendeteksi adanya gerakan maka Fan, Lamp, dan Humifier mati.

4.	Kitchen

Jika Applience menyala, Water Drain juga menyala.
Jika Appliance mati, maka Water Drain juga mati.
Pada kitchen juga terdapat Fire Monitor yang digunakan untuk mendeteksi adanya api sumber kebakaran. Jika fire Monitor mendeteksi adanya api kebakaran maka Fire Sprinkle di setiap ruangan akan menyala. Namun, jika tidak mendeteksi adanya api kebakaran maka Fire Sprinkle tidak menyala.

# Penjelasan Kode Program
function setup(){
	setDeviceProperty(getName(), 'IR', 900);
}
Script di atas merupakan script yang digunakan pada komponen api/heating element sehingga element/komponen tersebut dapat terdeteksi oleh sensor api. 900 merupakan value dari element tersebut.
