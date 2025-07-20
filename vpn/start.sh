echo "[INFO] start.sh çalıştı"
# OpenVPN başlat
openvpn --config /etc/openvpn/config.ovpn --auth-user-pass /etc/openvpn/auth.txt

#!/bin/sh
openvpn --config /etc/openvpn/client.conf &

echo "[INFO] VPN bağlantısı kuruluyor, 20 saniye bekleniyor..."
sleep 20

echo "[INFO] NAT kuralı ekleniyor..."
iptables -t nat -A POSTROUTING -s 172.18.0.0/16 -o tun0 -j MASQUERADE

wait