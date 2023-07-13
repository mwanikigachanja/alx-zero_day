import requests
import iptc

# Fetch threat intelligence data
def get_threat_intelligence():
    response = requests.get('https://example.com/threat-feed')
    threat_data = response.json()
    return threat_data

# Parse threat data and update firewall rules
def update_firewall_rules():
    threat_data = get_threat_intelligence()
    for threat in threat_data:
        if threat['type'] == 'malicious_ip':
            rule = iptc.Rule()
            rule.src = threat['ip']
            target = rule.create_target("DROP")
            chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
            chain.insert_rule(rule)
            print(f"Blocking malicious IP: {threat['ip']}")

# Continuously update firewall rules
while True:
    update_firewall_rules()
    time.sleep(3600)

