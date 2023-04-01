import socket

dns_table = {
    "www.amazon.com": "192.0.2.1",
    "www.lenskart.com": "198.51.100.1",
    "www.zomato.com": "203.0.113.1",
    "www.instagram.com": "192.0.2.2"
}

cname_record = {
    "www.amazon.com": "host.amazon.com",
    "www.lenskart.com": "host.lenskart.com",
    "www.zomato.com": "host.zomato.com",
    "www.instagram.com": "host.instagram.com"
}


def start_dns_server(port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", port)
    server_socket.bind(server_address)
    print(f"DNS server is running on {server_address}")

    while True:
        data, address = server_socket.recvfrom(512)
        print(f"Request received from {address}: {data.decode()}")

        domain_name = data.decode()
        ip = dns_table.get(domain_name, "not found!").encode()
        cname = cname_record.get(domain_name, "requested").encode()

        server_socket.sendto(ip, address)
        server_socket.sendto(cname, address)
        print(
            f"Response sent to {address}: IP Address: {ip.decode()}, CNAME Record: {cname.decode()}")


start_dns_server(port=5000)