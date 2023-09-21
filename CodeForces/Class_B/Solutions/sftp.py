import pysftp
import paramiko

Hostname = "10.190.36.146"
Hostname = "10.10.10.219:22"
Username = "sftpuser"
Password = "Pa$$123456"



class My_Connection(pysftp.Connection):
    def __init__(self, *args, **kwargs):
        self._sftp_live = False
        self._transport = None
        super().__init__(*args, **kwargs)

try: 
    with My_Connection(Hostname, username=Username, password=Password) as sftp:
        print('come in here')
        l = sftp.listdir()
        print(l)
except paramiko.ssh_exception.SSHException as e:
    print('SSH error, you need to add the public key of your remote in your local known_hosts file first.', e)
