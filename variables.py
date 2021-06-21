import json

result = """
{
    "interfaces": {
        "Ethernet2": {
            "name": "Ethernet2",
            "interfaceStatus": "connected",
            "interfaceAddress": {
                "ipAddr": {
                    "maskLen": 24,
                    "address": "2.2.2.2"
                }
            },
            "ipv4Routable240": false,
            "lineProtocolStatus": "up",
            "mtu": 1500
        },
        "Management0": {
            "name": "Management0",
            "interfaceStatus": "connected",
            "interfaceAddress": {
                "ipAddr": {
                    "maskLen": 24,
                    "address": "192.168.0.21"
                }
            },
            "ipv4Routable240": false,
            "lineProtocolStatus": "up",
            "mtu": 1500
        },
        "Ethernet1": {
            "name": "Ethernet1",
            "interfaceStatus": "connected",
            "interfaceAddress": {
                "ipAddr": {
                    "maskLen": 24,
                    "address": "1.1.1.1"
                }
            },
            "ipv4Routable240": false,
            "lineProtocolStatus": "up",
            "mtu": 1500
        }
    }
}
"""
dictionary = json.loads(result)

for interface in dictionary['interfaces']:
    print(dictionary['interfaces'][interface]['interfaceAddress']['ipAddr']['address']) 

