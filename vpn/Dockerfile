FROM kylemanna/openvpn

USER root

RUN apk add --no-cache iptables iproute2

COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
