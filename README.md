# Python VPN Proxy via Docker

## 🇬🇧 What is this project?

This project sets up a Python-based HTTP proxy in a Docker container that forwards outbound HTTP(S) requests **through a VPN connection**, using OpenVPN. The OpenVPN client also runs in a Docker container.

### 🔧 How It Works

1. `openvpn-client` container connects to a VPN using a `.ovpn` config file.
2. `python-proxy` container sends all its HTTP(S) requests through that VPN.
3. A Java application or browser can send requests to the Python proxy, which forwards them over the VPN and returns the response.

### 📁 File Structure

docker_python_vpn_proxy/
├── proxy/            # Python Flask app
├── vpn/              # Place your .ovpn and auth.txt here (excluded from Git)
├── docker-compose.yml
└── README.md


---

## 🛠️ How to Use

### 1. Prepare your VPN files
- Copy your `.ovpn` config file into `vpn/dockvpn.ovpn`.
- Copy your VPN credentials into `vpn/auth.txt`  
  - Format:  
    ```
    your-vpn-username
    your-vpn-password
    ```
- Make sure your `.ovpn` file has:
  ```text
  auth-user-pass /etc/openvpn/auth.txt

Note: The `vpn/` directory is versioned with a `.gitkeep` file. Do not add your real VPN credentials to Git.

---NEW---
Stopped using up.sh script: Using the up.sh script inside the OpenVPN container caused issues with adding the NAT rule, so a different method was chosen.

NAT processing moved to a separate container: Created a small container named vpn-nat.

vpn-nat container depends on openvpn-client: Starts only after the openvpn-client container is running.

Added a 20-second startup delay: To ensure the VPN connection and tun0 interface are fully up and ready.

vpn-nat container adds the NAT rule using iptables: It masquerades traffic originating from the 172.18.0.0/16 subnet through the tun0 interface.

vpn-nat container keeps running: Uses tail -f /dev/null to keep the container alive.

Working flow:
The openvpn-client container starts and establishes the VPN connection.

The vpn-nat container starts after openvpn-client is up.

vpn-nat waits 20 seconds to ensure the tun0 interface is ready.

Then it adds the NAT rule with iptables.

The NAT rule is active, and traffic flows out via the VPN tunnel.


### 🛠️ How to Run

1. Copy your `.ovpn` and `auth.txt` files into the `vpn/` directory.
2. Make sure `.ovpn` does **not** contain `auth-user-pass`, or comment it out.
3. Run:

```bash
docker-compose up --build
```
4. Send a request to test:
```bash
curl "http://localhost:5000/proxy?url=https://ipinfo.io/ip"
```


## 🇹🇷 Bu Proje Nedir?
Bu proje, bir Python proxy sunucusunun OpenVPN üzerinden dış dünyaya çıkmasını sağlayan Docker tabanlı bir yapı kurar. Tüm HTTP/HTTPS istekleri, VPN üzerinden yapılır.

🌐 Kullanım Senaryosu
Windows bilgisayarında bir Java (veya başka bir) uygulaman var.

Bu uygulamanın internete çıkışını VPN üzerinden yapmak istiyorsun.

Projede kurulan proxy, http://localhost:5000/proxy?url=https://... üzerinden çalışır.

Gönderdiğin istek, VPN üzerinden yönlendirilir ve sana HTTP yanıtı döner.

🔧 Nasıl Çalışır?
openvpn-client container, .ovpn dosyasını kullanarak VPN'e bağlanır.

python-proxy container, tüm internet çıkışını bu VPN üzerinden yapar.

Windows'taki bir Java programı ya da tarayıcı, bu proxy'e istek göndererek, VPN üzerinden dış dünyaya ulaşır.

### 📁 Dosya Yapısı
docker_python_vpn_proxy/
├── proxy/            # Python Flask uygulaması
├── vpn/              # .ovpn ve auth.txt buraya (Git'e dahil edilmez)
├── docker-compose.yml
└── README.md

Not: `vpn/` klasörü `.gitkeep` dosyası ile birlikte repoya dahil edilmiştir. Gerçek VPN bilgilerinizi burada tutmayın.

🛠️ Nasıl Çalıştırılır?
1 .ovpn ve auth.txt dosyalarını vpn/ klasörüne koy.

2 .ovpn içindeki auth-user-pass satırını sil ya da # ile yorum satırı yap.

3 Aşağıdaki komutu çalıştır:
```bash
docker-compose up --build
```

4. Test etmek için:
```bash
curl "http://localhost:5000/proxy?url=https://ipinfo.io/ip"
```

🔥 Özet: Yapılan Değişiklikler ve Çalışma Sistemi
Türkçe
up.sh scripti kullanımı bırakıldı: OpenVPN container içindeki up.sh ile NAT kuralı eklemek sorun çıkarıyordu, bu yüzden farklı bir yöntem tercih edildi.

NAT işlemi ayrı bir container olarak yapıldı: vpn-nat adında küçük bir container oluşturuldu.

vpn-nat container’ı openvpn-client container’ına bağlı çalışıyor: depends_on ile openvpn-client başladıktan sonra başlıyor.

Başlangıçta 20 saniye bekletme eklendi: Bu, VPN bağlantısının tam kurulmasını ve tun0 arayüzünün hazır olmasını sağlamak için.

vpn-nat container’ı iptables ile NAT kuralını ekliyor: 172.18.0.0/16 subnetinden çıkan trafiği tun0 üzerinden MASQUERADE yapıyor.

vpn-nat container’ı sürekli çalışıyor: tail -f /dev/null ile container kapanmıyor.

Çalışma Sistemi:
openvpn-client container başlar ve VPN bağlantısını kurar.

vpn-nat container, openvpn-client çalışmaya başladıktan sonra başlar.

vpn-nat 20 saniye bekler, böylece tun0 arayüzü tam hazır olur.

Ardından iptables ile NAT kuralını ekler.

NAT kuralı aktif olur ve trafik VPN üzerinden çıkmaya başlar.

⚠️ Uyarılar
1 .ovpn ve auth.txt kesinlikle Git'e yüklenmemeli.

2 auth.txt sadece 2 satır içermeli: kullanici ve sifre.

3 Bu yapı sadece istemci taraflı (client-mode) OpenVPN bağlantısı içindir.

✅ Ne Zaman Kullanılır?
VPN üzerinden HTTP(S) istekleri yapmak gerektiğinde.

Java ya da başka bir programın VPN üzerinden internete çıkması gerekiyorsa.

Proxy olarak davranan ama gerçek çıkışı bir VPN'e yönlendiren yapı gerektiğinde.
