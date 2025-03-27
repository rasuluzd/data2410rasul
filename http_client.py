import socket
import sys
import argparse

# --- Hent kommandolinjeargumenter ---
parser = argparse.ArgumentParser(description="Enkel HTTP-klient")
parser.add_argument("-i", "--ip", required=True, help="Serverens IP-adresse eller hostname")
parser.add_argument("-p", "--port", type=int, required=True, help="Serverporten")
parser.add_argument("-f", "--file", required=True, help="Filnavn som skal hentes")
args = parser.parse_args()

# --- Opprett en TCP-socket ---
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Koble til serveren
clientSocket.connect((args.ip, args.port))

# --- Bygg og send GET-forespørselen ---
request = "GET /" + args.file + " HTTP/1.1\r\nHost: " + args.ip + "\r\n\r\n"
clientSocket.send(request.encode())

# --- Mottar responsen fra serveren ---
response = clientSocket.recv(4096)
print(response.decode())

clientSocket.close()
