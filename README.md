# Welcome to the Packet Sniffer Tool!

This Python program allows users to capture and analyze network packets. It is developed for educational purposes and demonstrates how to retrieve and display information such as source and destination IP addresses, network protocols, and packet payloads using the `scapy` library.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Description

The Packet Sniffer Tool is a basic Python-based network traffic analyzer. It captures live packets from a specified network interface and extracts useful information like source/destination IPs and protocol type (TCP/UDP). It is a great tool to understand how network packets work under the hood and serves as a foundation for more advanced networking projects.

## Features

- Capture live network traffic on a specified interface.
- Analyze TCP and UDP packets in real time.
- Display source and destination IP addresses, along with the protocol type.
- Optionally, display packet payloads when available.

## Requirements

- Python 3.x
- `scapy` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/packet-sniffer-tool.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd packet-sniffer-tool
    ```

3. **Install dependencies:**

    You will need the `scapy` library, which can be installed via `pip`:

    ```bash
    pip install scapy
    ```

## Usage

1. Run the program using Python:

    ```bash
    python packet_sniffer.py
    ```

2. When prompted, specify the network interface you want to sniff (e.g., `eth0` for Ethernet or `wlan0` for WiFi).

3. The tool will start capturing packets and display relevant information in real-time.

## Example

```
Starting packet sniffing on interface: wlan0
[2024-09-09 14:55:22] Source: 192.168.0.101, Destination: 192.168.0.103, Protocol: TCP
Payload: b'Example payload data...'
[2024-09-09 14:55:25] Source: 192.168.0.102, Destination: 192.168.0.104, Protocol: UDP
No Payload
```

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Developed by [Your Name] for educational purposes.

---

Feel free to customize this `README.md` file with your personal information and project details. Let me know if you'd like additional sections or modifications!
