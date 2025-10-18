import subprocess
import os

def showrun():
    # read https://www.datacamp.com/tutorial/python-subprocess to learn more about subprocess
    command = ['ansible-playbook', '-i', 'hosts', 'backup_cisco_router_playbook.yaml']
    result = subprocess.run(command, capture_output=True, text=True)
    result = result.stdout
    if 'failed=0' in result and 'unreachable=0' in result:
        print('Ansible playbook executed successfully.')
        return 'ok'
    else:
        return 'Error: Ansible'
