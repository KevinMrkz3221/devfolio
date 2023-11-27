AWS_ACCESS_KEY_ID = 'DO00EF7DY8L67W29HCQ4'
AWS_SECRET_ACCESS_KEY ='FXIh/XA2y/HD7xxwoio30FR08iwkJvZvgx8sMwvKa60'
AWS_STORAGE_BUCKET_NAME = 'kevinarmport'
AWS_S3_ENDPOINT_URL ='https://nyc3.digitaloceanspaces.com'

AWS_S3_OBJECTS_PARAMETERS = {
    "CacheControl": "max-age=86400"
}
AWS_LOCATION = 'https://kevinarmport.nyc3.digitaloceanspaces.com'


DEFAULT_FILE_STORAGE = "config.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE= "config.cdn.backends.StaticRootS3Boto3Storage"

