from flask import Blueprint, request, jsonify
import subprocess

remote_bp = Blueprint('remote_control', __name__)

@remote_bp.route('/execute', methods=['POST'])
def execute_command():
    data = request.get_json()
    command = data.get('command')

    if not command:
        return jsonify({'error': 'No command provided'}), 400

    try:
        # Simulate remote command execution
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        output = result.stdout
        error = result.stderr
        return jsonify({'output': output, 'error': error})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
