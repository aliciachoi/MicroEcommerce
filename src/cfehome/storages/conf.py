from cfehome.env import config

AWS_ACCESS_KEY_ID=config("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY=config("AWS_SECRET_ACCESS_KEY", default=None)
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME", default="microecommerce")
AWS_S3_REGION_NAME = "eu-north-1"
AWS_S3_ENDPOINT_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
AWS_DEFAULT_ACL =  "public-read"
AWS_S3_USE_SSL = True

# file upload storage default
DEFAULT_FILE_STORAGE = 'cfehome.storages.backends.MediaStorage'

# staticfiles 
STATICFILES_STORAGE = 'cfehome.storages.backends.StaticFileStorage'