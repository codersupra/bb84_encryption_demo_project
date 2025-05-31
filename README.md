# 🔐 Quantum Key Distribution using BB84 Protocol

This project demonstrates a secure communication system based on the **BB84 Quantum Key Distribution (QKD)** protocol. The system uses **Qiskit** to simulate quantum key exchange and showcases two types of encryption:

- 🔑 **Bitwise XOR encryption** for simple message confidentiality
- 🛡️ **Fernet symmetric encryption (AES-128)** using a BB84-derived key

---

## 🧠 How It Works

### 1. Quantum Key Distribution (QKD) with BB84
- Simulates Alice and Bob's quantum communication
- Handles eavesdropping detection via basis comparison
- Generates a **shared secret key**

### 2. Message Encryption
- Converts plaintext to binary
- XORs each bit with the BB84 key (`bitwise` mode) **OR**
- Derives a Fernet AES key from BB84 key (`fernet` mode)
- Encrypts & decrypts messages securely

---

## 📁 File Structure
.
├── bb84.py # BB84 protocol implementation
├── example_1.py # XOR-based encryption using BB84 key
├── fernet_crypto.py # Fernet encryption using BB84-derived key
├── example_2.py # Fernet encrytion usecase
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 💻 Installation

```bash
git clone https://github.com/yourusername/bb84-secure-communication.git
cd bb84-secure-communication
pip install -r requirements.txt
```

## References:
For BB84 Circuit - Pedone, Ignazio & Atzeni, Andrea & Canavese, Daniele & Lioy, Antonio. (2021). Toward a Complete Software Stack to Integrate Quantum Key Distribution in a Cloud Environment. IEEE Access. PP. 1-1. 10.1109/ACCESS.2021.3102313. 
