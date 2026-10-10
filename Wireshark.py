from collections import Counter
from datetime import datetime

print("NETWORK TRAFFIC ANALYSIS")
print("------------------------")

# Sample packet data for demonstration
packets = [
    {"protocol": "TCP", "source": "192.168.1.2", "destination": "142.250.1.1", "port": 443},
    {"protocol": "DNS", "source": "192.168.1.2", "destination": "8.8.8.8", "port": 53},
    {"protocol": "UDP", "source": "192.168.1.2", "destination": "8.8.8.8", "port": 53},
    {"protocol": "TCP", "source": "192.168.1.2", "destination": "192.168.1.5", "port": 80},
    {"protocol": "HTTP", "source": "192.168.1.2", "destination": "192.168.1.5", "port": 80}
]

print("Capture Time:", datetime.now())
print("\nPacket Details:")

for i, packet in enumerate(packets, 1):
    print("\nPacket", i)
    print("Protocol:", packet["protocol"])
    print("Source:", packet["source"])
    print("Destination:", packet["destination"])
    print("Port:", packet["port"])

print("\nProtocol Summary:")
counts = Counter(p["protocol"] for p in packets)

for protocol, count in counts.items():
    print(protocol, ":", count, "packets")

print("\nAnalysis completed successfully!")