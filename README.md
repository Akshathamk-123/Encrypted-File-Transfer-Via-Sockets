# Encrypted-File-Transfer-Via-Sockets
This project is a part of Academic Mini-Project for the Subject Computer Networks.
This project demonstrates an encrypted file transfer system using AES (Advanced Encryption Standard) in EAX mode. The system consists of three main components: a key generation script, a receiver (server), and a sender (client). The server receives an encrypted file from the client and decrypts it.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x
- `pycryptodome` library (for AES encryption and decryption)
- A local network or two machines that can communicate over TCP/IP

## Installation

1. **Install the required library:**

   ```bash
   pip install pycryptodome
   ```

2. **Download the project files:**

   - `generate_key.py`
   - `receiver.py`
   - `sender.py`
   - A file named `file` to be transferred

## File Descriptions

- `generate_key.py`: This script demonstrates basic AES encryption and decryption for a sample message ("Hello World!").
- `receiver.py`: This script sets up a server that listens for an incoming connection, receives an encrypted file, and decrypts it.
- `sender.py`: This script connects to the server, reads a file, encrypts its contents, and sends it to the server.

## How to Run the Project

### Step 1: Generate Key and Nonce (Optional)

The `generate_key.py` script demonstrates how encryption and decryption work. This is optional for understanding but not necessary for running the main project.

```bash
python generate_key.py
```

### Step 2: Start the Server (Receiver)

Run the `receiver.py` script on the machine that will act as the server. Make sure to use the correct IP address and port.

```bash
python receiver.py
```

This script will:

1. Create a socket and bind it to `localhost` on port `9999`.
2. Listen for incoming connections.
3. Accept a connection from a client.
4. Receive the file name and size.
5. Receive the encrypted file data.
6. Decrypt the file data and save it.

### Step 3: Run the Client (Sender)

Run the `sender.py` script on the machine that will act as the client. Replace `192.168.191.221` with the server's IP address.

```bash
python sender.py
```

This script will:

1. Create a socket and connect to the server's IP address and port `9999`.
2. Read the file named `file` from the current directory.
3. Encrypt the file data.
4. Send the file name and size to the server.
5. Send the encrypted file data to the server.
6. Close the connection.

## Example

1. Place a file named `file` in the same directory as `sender.py` on the client machine.
2. Run `receiver.py` on the server machine.
3. Run `sender.py` on the client machine.

The server will receive the file, decrypt it, and save it in the current directory.

## Notes

- Ensure that both machines are on the same network if using different machines.
- You may need to adjust firewall settings to allow the connection.
- This example uses hardcoded keys and nonces for simplicity. In a production environment, use secure key management practices.

## Conclusion

This project demonstrates a simple yet effective way to transfer files securely using AES encryption. It can be extended and modified for more robust use cases and security measures.
