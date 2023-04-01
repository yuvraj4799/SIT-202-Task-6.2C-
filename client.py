import socket


def run_dns_client(server_address="127.0.0.1", port=5000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        domain_name = input("Enter a domain name (or 'exit' to quit): ")
        if domain_name.lower() == "exit":
            break

        client_socket.sendto(domain_name.encode(), (server_address, port))
        data, address = client_socket.recvfrom(512)
        cname, address = client_socket.recvfrom(512)

        ip_address = data.decode().strip()
        cname_record = cname.decode().strip()

        message = f"The IP address of {cname_record} is {ip_address}."
        print(message)

    client_socket.close()


run_dns_client(server_address="127.0.0.1", port=5000)
