import os


class Config(object):
    db_uri = f"{os.getenv('DB_SERVICE')}://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}" \
             f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
