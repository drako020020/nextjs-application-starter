from flask import Blueprint, request, jsonify
import networkx as nx

ai_bp = Blueprint('ai_planner', __name__)

# Simple rule-based decision tree for demonstration
def plan_attack(topology, devices, permissions):
    G = nx.DiGraph()

    # Add nodes for devices
    for device in devices:
        G.add_node(device['ip'], type=device.get('type', 'unknown'))

    # Add edges based on topology
    for connection in topology:
        G.add_edge(connection['from'], connection['to'])

    # Simple rules for recommended actions
    actions = []
    for device in devices:
        ip = device['ip']
        if permissions.get(ip) == 'admin':
            actions.append({'ip': ip, 'action': 'Maintain access'})
        elif permissions.get(ip) == 'user':
            actions.append({'ip': ip, 'action': 'Attempt privilege escalation'})
        else:
            actions.append({'ip': ip, 'action': 'Scan and exploit'})

    return actions

@ai_bp.route('/plan', methods=['POST'])
def plan():
    data = request.get_json()
    topology = data.get('topology', [])
    devices = data.get('devices', [])
    permissions = data.get('permissions', {})

    actions = plan_attack(topology, devices, permissions)
    return jsonify({'actions': actions})
