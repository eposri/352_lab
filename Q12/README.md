# Assignment: Symmetric and Public Key Cryptography Basics
### Question 12: RSA and DSA Implementation
#### **Group Members:**
- Maritza Esparza
- Gianna Davila
- Kayla Ngo

## Program Execution Instructions
To run **server.py**, enter in the terminal:
```
python server.py <SERVER_PORT> <16-byte key>

# Example:
python server.py 1235 asdasdasdasdasda
```

To run **client.py**, enter in the terminal:
```
python client.py <SERVER_IP> <SERVER_PORT> <16-byte key>

# Example:
python client.py 1235 127.0.0.1 asdasdasdasdasda
```

On the client-side, users will be prompted to select from the available digital signature options.

The server will continue to accept connections from clients.

## Requirements
```
sudo apt install python3-pip
sudo pip3 install pycryptodomex
```