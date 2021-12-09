import os

RUN_VER = os.environ.get("APIGW_RUN_VER","dev")

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS_WORD = os.environ.get('DB_PASS_WORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

# apigw访问地址
APIGW_HOST = os.environ.get('APIGW_HOST','')
