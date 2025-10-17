import subprocess
import os

def showrun():
    # read https://www.datacamp.com/tutorial/python-subprocess to learn more about subprocess
    command = ['./venv/bin/ansible-playbook', '-i', './ansible/hosts', './ansible/backup_cisco_router_playbook.yaml']
    env = os.environ.copy()
    env['ANSIBLE_CONFIG'] = './ansible/ansible.cfg'
    result = subprocess.run(command, capture_output=True, text=True, env=env)
    result = result.stdout
    if 'failed=0' in result and 'unreachable=0' in result:
        print('Ansible playbook executed successfully.')
        return 'ok'
    else:
        return 'Error: Ansible'
