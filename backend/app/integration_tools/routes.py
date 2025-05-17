from flask import Blueprint, request, jsonify, current_app
import requests

integration_bp = Blueprint('integration_tools', __name__)

@integration_bp.route('/shodan', methods=['POST'])
def shodan_search():
    data = request.get_json()
    query = data.get('query')
    api_key = current_app.config.get('SHODAN_API_KEY')

    if not api_key:
        return jsonify({'error': 'Shodan API key not configured'}), 500
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    url = f'https://api.shodan.io/shodan/host/search?key={api_key}&query={query}'
    try:
        response = requests.get(url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@integration_bp.route('/virustotal', methods=['POST'])
def virustotal_scan():
    data = request.get_json()
    resource = data.get('resource')
    api_key = current_app.config.get('VIRUSTOTAL_API_KEY')

    if not api_key:
        return jsonify({'error': 'VirusTotal API key not configured'}), 500
    if not resource:
        return jsonify({'error': 'No resource provided'}), 400

    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': api_key, 'resource': resource}
    try:
        response = requests.get(url, params=params)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@integration_bp.route('/metasploit', methods=['POST'])
def metasploit_rpc():
    # Placeholder for Metasploit RPC API integration
    return jsonify({'msg': 'Metasploit RPC integration not implemented yet'}), 501
