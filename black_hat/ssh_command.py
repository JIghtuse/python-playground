# paramiko usage example

import paramiko


BUFFER_SIZE = 1024


def ssh_command(ip, user, password, command, keys_path=None):
    client = paramiko.SSHClient()
    if keys_path is not None:
        client.load_host_keys(keys_path)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=password)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(BUFFER_SIZE))


if __name__ == "__main__":
    ssh_command("localhost", "<username>", "<secret>", 'id')
