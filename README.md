# Duvardan Kaçan Kaplumbağa 

Bu proje, ROS 2 Humble üzerinde `turtlesim` paketi kullanılarak geliştirilmiş otonom bir kaplumbağa düğümünü (node) içermektedir. Kaplumbağa, belirlenen sınır değerlerine ulaştığında yön değiştirerek duvarlara çarpmaktan kaçınır ve saniyede bir konumunu terminale loglar.

## Özellikler
* **Yayıncı (Publisher):** `/turtle1/cmd_vel` konusu üzerinden kaplumbağayı ileri sürer ve sınırlarda dönüş hızları gönderir.
* **Abone (Subscriber):** `/turtle1/pose` konusunu dinleyerek X ve Y koordinatlarını anlık olarak alır[cite: 1].
* **Loglama:** Kaplumbağanın anlık koordinatları saniyede bir terminale `info` seviyesinde yazdırılır[cite: 1].
* **Parametrik Yapı (Bonus):** Hız (`speed`), alt sınır (`limit_alt`) ve üst sınır (`limit_ust`) değerleri kod içinde parametrik hale getirilmiştir.

## Kurulum ve Çalıştırma

1. Çalışma alanına gidip paketi derleyin:
   ```bash
   cd ~/ros2_ws
   colcon build --packages-select turtle_duvar_py
   source install/setup.bash
   
2. Birinci terminalde turtlesim simülasyonunu başlatın:
   ros2 run turtlesim turtlesim_node

3. İkinci terminalde otonom kaçış düğümünü çalıştırın:
   ros2 run turtle_duvar_py kacan_kaplumbaga
