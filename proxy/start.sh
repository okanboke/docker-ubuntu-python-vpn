#!/bin/sh

# openvpn-client container'ın IP'sini al
VPN_GATEWAY=$(getent hosts openvpn-client | awk '{ print $1 }')

# Tüm outbound trafiği openvpn-client üzerinden yönlendir
ip route del default
ip route add default via $VPN_GATEWAY

# DNS ayarı (gerekirse)
echo "nameserver 8.8.8.8" > /etc/resolv.conf

# Flask başlat
python app.py
