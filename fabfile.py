# coding: utf-8
import os
import sys
import tempfile
from datetime import datetime

from fabric.api import *
from fabric.contrib import django


TIME_FORMAT = "%Y-%m-%dT%H:%M:%S%z"


# -------
# Constantes passíveis de definição via argumentos.
# -------
TEMPDIR = env.get('tempdir', tempfile.gettempdir())


# Açúcar sintático para a declaração e inicialização da variável
# DJANGO_SETTINGS_FILE.
django.project('scielomanager')


# -------
# O diretório base do projeto deve constar em `sys.path`, para que seja
# possível importar seus pacotes e módulos.
# -------
HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_BASE = HERE + '/scielomanager'
if PROJECT_BASE not in sys.path:
    sys.path.insert(0, PROJECT_BASE)


# -------
# Partindo daqui é possível importar pacotes e módulos do projeto.
# -------
from django.conf import settings
from journalmanager import models


@task
def dump_db():
    db = settings.DATABASES['default']
    dump_filename = '{dbname}-{datetime}.sql'.format(
            dbname=db['NAME'], datetime=datetime.now().strftime(TIME_FORMAT))
    dump_filepath = os.path.join(TEMPDIR, dump_filename)

    cmd = 'pg_dump {dbname} -h {host} -p {port} -U {user} > {dump_filepath}'.format(
        dbname=db['NAME'], host=db['HOST'], port=db['PORT'], user=db['USER'],
        dump_filepath=dump_filepath)

    local(cmd)

    return dump_filepath
