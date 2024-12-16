import os
from dotenv import load_dotenv
load_dotenv()

# DATABASES = {
#     'default': {
#         'DATABASE_NAME':os.getenv('DATABASE_NAME'),
#         'DATABASE_USER':os.getenv('DATABASE_USER'),
#         'DATABASE_PASSWORD':os.getenv('DATABASE_PASSWORD'),
#         'DATABASE_HOST':os.getenv('DATABASE_HOST'),   
#         'DATABASE_PORT':os.getenv('DATABASE_PORT')
#     },
# }

DATABASES = {
    'default': {
        'DATABASE_NAME':'postgres',
        'DATABASE_USER':'postgres',
        'DATABASE_PASSWORD':'postgres',
        'DATABASE_HOST':'db',
        'DATABASE_PORT':5432
}
}