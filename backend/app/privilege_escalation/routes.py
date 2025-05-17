from flask import Blueprint, jsonify
import subprocess

privilege_bp = Blueprint('privilege_escalation', __name__)

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

@privilege_bp.route('/check', methods=['GET'])
def check_privilege_escalation():
    results = {}

    # Check sudo privileges
    results['sudo_l'] = run_command('sudo -l')

    # Find files with SUID bit set
    results['suid_files'] = run_command('find / -perm -4000 -type f 2>/dev/null')

    # Get capabilities
    results['capabilities'] = run_command('getcap -r / 2>/dev/null')

    return jsonify(results)
