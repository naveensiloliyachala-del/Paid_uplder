import os

API_ID = os.environ.get("API_ID", "29020892")

API_HASH = os.environ.get("API_HASH", "15bfac43cfbeb3993c942ce2f11ec3f8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8096675089:AAFBP7q9ripjNz8oKIEk7szXDRKDX-dq8Ko")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", ))

LOG = ,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7068000043").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


