from databases import Database
from utils.const import DB_URL, IS_LOAD_TEST, TESTING, TEST_DB_URL, IS_PRODUCTION, DB_URL_PRODUCTION

if TESTING or IS_LOAD_TEST:
    db = Database(TEST_DB_URL)
elif IS_PRODUCTION:
    db = Database(DB_URL_PRODUCTION)
else:
    db = Database(DB_URL)