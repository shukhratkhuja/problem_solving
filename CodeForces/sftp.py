import paramiko
import pysftp

# Установка соединения с SFTP-сервером
# sftp = paramiko.SFTPClient()
# sftp.connect('10.190.36.146', username='sftpuser', password='Pa$$123456')

# Define the SFTP server connection parameters
sftp_host = '0.190.36.146'
sftp_port = 8185  # The default SFTP port is 22
sftp_user = 'sftpuser'
sftp_password = 'Pa$$123456'

# Establish an SFTP connection
with pysftp.Connection(sftp_host, port=sftp_port, username=sftp_user, password=sftp_password) as sftp:
    print(sftp.getcwd())