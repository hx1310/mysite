# coding:utf-8

from fabric.api import env,run
from fabric.operations import sudo

GIT_REPO="https://github.com/hx1310/mysite.git"

env.user='root'
env.password='xzxxn520'

env.hosts=['www.hx1310.online']
env.port='22'

def deploy():
    source_folder='/home/hx/sites/hx1310.online/mysite'
    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-hx1310.online')
    sudo('service nginx reload')
