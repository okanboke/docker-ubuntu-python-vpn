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

Note: The `vpn/` directory is versioned with a `.gitkeep` file. Do not add your real VPN credentials to Git.


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

🇹🇷 Bu Proje Nedir?
Bu proje, bir Python proxy sunucusunun OpenVPN üzerinden dış dünyaya çıkmasını sağlayan Docker tabanlı bir yapı kurar. Tüm HTTP/HTTPS istekleri, VPN üzerinden yapılır.

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

⚠️ Uyarılar
1 .ovpn ve auth.txt kesinlikle Git'e yüklenmemeli.

2 auth.txt sadece 2 satır içermeli: kullanici ve sifre.

3 Bu yapı sadece istemci taraflı (client-mode) OpenVPN bağlantısı içindir.

✅ Ne Zaman Kullanılır?
VPN üzerinden HTTP(S) istekleri yapmak gerektiğinde.

Java ya da başka bir programın VPN üzerinden internete çıkması gerekiyorsa.

Proxy olarak davranan ama gerçek çıkışı bir VPN'e yönlendiren yapı gerektiğinde.
