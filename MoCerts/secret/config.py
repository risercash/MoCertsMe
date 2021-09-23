from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), 'secret.env')
load_dotenv(dotenv_path)