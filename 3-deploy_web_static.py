#!/usr/bin/python3
""" Fabric script (based on the file 2-do_deploy_web_static.py) that
creates and distributes an archive to your web servers
using the function deploy: """


from fabric.api import *
from datetime import datetime
from os.path import exists, isdir


env.hosts = ['54.157.145.55', '100.25.139.164']


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """ distributes an archive to my web servers
    """
    if exists(archive_path) is False:
        return False

    try:
        filename = archive_path.split('/')[-1]
        no_tgz = filename.split('.')[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run("mkdir -p {}{}/".format(path, no_tgz))
        run("tar -xzf /tmp/{} -C {}{}/".format(filename, path, no_tgz))
        run("rm /tmp/{}".format(filename))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, no_tgz))
        run("rm -rf {}{}/web_static".format(path, no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, no_tgz))
        return True
    except:
        return False


def deploy():
    """ creates and distributes an archive to your web servers
    """
    new_archive_path = do_pack()
    if exists(new_archive_path) is False:
        return False
    result = do_deploy(new_archive_path)
    return result
