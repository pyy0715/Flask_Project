import os
from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b"\x82&+y\xf2\xa0\x0b4\x9a'%K\x1e\xfb+V"
