import argparse
import paramiko

hostname = "10.167.142.23"
user = "puguiyu_wx"
password = "QWEasd123"
remote_file = "/data/puguiyu_wx/files/"
env_path = "/data/puguiyu_wx/en3v/bin/"
scp_path = "/data/puguiyu_wx/work/utils/scp.py"
mail_path = "/data/puguiyu_wx/work/utils/mail_sender.py"


def ssh_put(hostname, local_file, remote_file, user="puguiyu_wx",
            password="QWEasd123", is_make_dir=True):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=user, password=password)

    remote_path = remote_file[0:remote_file.rfind("/")]

    if is_make_dir:
        # 目录为空
        stdin, stdout, stderr = ssh.exec_command("cd %s" % remote_path)

        err = stderr.read()
        print(err)
        if err:
            stdin, stdout, stderr = ssh.exec_command(
                "mkdir -p %s" % remote_path)
            print(stderr.read())

    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_file)


def ssh_get(hostname, user, password, local_file, remote_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=user, password=password)
    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_file)


def send_mail(local_file):
    """
    直接发送邮件
    :param local_file:
    :return:
    """

    file_name = local_file.split("/")[-1]
    # 先将当前文件拷贝到143这台机器
    ssh_put("10.167.142.23", local_file, remote_file + file_name,
            user=user, password=password, is_make_dir=True)

    # 然后在执行143的文件拷贝命令，将文件拷贝到43
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    hostname2 = "10.167.4.23"
    print(hostname, "****", user, password)

    print(
        "python3  {scp_path} -p {remote_file} {remote_file} --host {hostname}".format(
            hostname=hostname2, scp_path=scp_path,
            remote_file=remote_file + file_name))
    ssh.connect(hostname=hostname, username=user, password=password)
    stdin, stdout, stderr = ssh.exec_command(
        "python3 {scp_path} -p {remote_file} {remote_file} --host {hostname}".format(
            hostname=hostname2,
            scp_path=scp_path,
            remote_file=remote_file + file_name),
        environment={"PATH": env_path})

    print(stderr)

    # 然后通过登录143控制43发送邮件到
    print("python3  {scp_path} --ss {remote_file} ".format(
        remote_file=remote_file + file_name, scp_path=scp_path))
    stdin, stdout, stderr = ssh.exec_command(
        "python3  {scp_path} --ss {remote_file} ".format(
            remote_file=remote_file + file_name, scp_path=scp_path))
    print(stderr)


def ssh_ssh_mail_sender(remote_file_name):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="10.167.4.23", username=user, password=password)
    ssh.exec_command(
        "python {mail_path} -f {remote_file}".format(
            remote_file=remote_file_name, mail_path=mail_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mail", help="发送邮件", action='store_true',
                        default=False)
    # -p 参数 第一个是local_file 第二个是remote_file 如果是发邮件第二个参数不用填
    parser.add_argument("-p", "--put", help="上传文件", nargs="*")
    parser.add_argument("-g", "--get", help="下载文件", action='store_true',
                        default=False)
    parser.add_argument("--host", help="原创主机ip")
    parser.add_argument("-l", "--local_file", help="本地文件路径")
    parser.add_argument("-r", "--remote_file", help="远程文件路径")
    parser.add_argument("--user", help="原创主机ip", default="puguiyu_wx")
    parser.add_argument("--password", help="原创主机ip", default="QWEasd123")
    parser.add_argument("--ss", help="执行远程ssh发送邮件")
    a = parser.parse_args()
    print(a)
    if a.mail:
        send_mail(a.put[0])
    elif a.put:
        ssh_put(a.host, a.put[0], a.put[1], a.user, a.password)
    elif a.get:
        pass
    elif a.ss:
        ssh_ssh_mail_sender(a.ss)
