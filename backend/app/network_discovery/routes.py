from flask import Blueprint, jsonify
import nmap

network_bp = Blueprint('network_discovery', __name__)

@network_bp.route('/scan', methods=['GET'])
def scan_network():
    nm = nmap.PortScanner()
    # Scan local network - example subnet, adjust as needed
    subnet = '192.168.1.0/24'
    try:
        nm.scan(hosts=subnet, arguments='-O -sS')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    hosts = []
    for host in nm.all_hosts():
        host_info = {
            'ip': host,
            'hostname': nm[host].hostname(),
            'state': nm[host].state(),
            'os': nm[host]['osmatch'][0]['name'] if nm[host].has_key('osmatch') and nm[host]['osmatch'] else 'Unknown',
            'open_ports': []
        }
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                port_info = {
                    'port': port,
                    'state': nm[host][proto][port]['state'],
                    'name': nm[host][proto][port]['name']
                }
                host_info['open_ports'].append(port_info)
        hosts.append(host_info)

    return jsonify({'hosts': hosts})
