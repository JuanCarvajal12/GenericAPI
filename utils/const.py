# JWT
JWT_SECRET_KEY  = "c8f1d35225c1932bc2c53270439d539c0ff0afb2c6fbe7d8dc692496c16ecba5"
# secret key generated using `$ openssl rand -hex 32`
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_TIME_MINUTES = 60*24*5

# Documentation strings
TOKEN_DESCRIPTION = "description sample for the /token"
TOKEN_SUMMARY = "token summary sample"
REF_DESCRIPTION = "sample description for a field"
USER_SUMMARY = "Create new User in personel"

# database
DB_HOST = "localhost"
DB_USER = "juan"
DB_PASSWORD = "Juan1234"
DB_NAME = "genericapi"
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Upload photo
UPLOAD_PHOTO_APIKEY = "900b9c8362c84215824dd1322563a2df"
UPLOAD_PHOTO_URL = f"https://api.imgbb.com/1/upload?key={UPLOAD_PHOTO_APIKEY}"

# redis cache-ing
REDIS_URL = 'redis://localhost'

#%--- TESTING
TESTING = True

# test database
TEST_DB_HOST = "localhost"
TEST_DB_USER = "test"
TEST_DB_PASSWORD = "test"
TEST_DB_NAME = "test"
TEST_DB_URL = f"postgresql://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}/{TEST_DB_NAME}"

# test redis
TEST_REDIS_URL = 'redis://localhost'