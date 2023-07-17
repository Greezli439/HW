from mongoengine import connect
import environ

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')
MONGODB_CONECRION = env('MONGODB_CONECRION')
connect(host='MONGODB_CONECRION')
