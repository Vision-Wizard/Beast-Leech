try:
    from .ExecVars import ExecVars
except:

    class ExecVars:
        # Set true if its VPS
        IS_VPS = False

        API_HASH = ""
        API_ID = 0
        BOT_TOKEN = ""
        BASE_URL_OF_BOT = ""

        # Edit the server port if you want to keep it default though.
        SERVPORT = 80

        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = []
        OWNER_ID = 0

        # Google Drive Index Link should include the base dir also See readme for more info
        GD_INDEX_URL = "https://drive.hanif-maxx.workers.dev/1:/Maxx-TD/"

        # Time to wait before edit message
        EDIT_SLEEP_SECS = 10

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 2097152000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress
        COMPLETED_STR = "▰"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▱"

        # DB URI for access
        # UNCOMMENT THE BELOW LINE WHEN USING CONTAINER AND COMMENT THE UPPER LINE
        DATABASE_URL = "postgres://mlpsfzvhwkjbvb:bdf333e8b52041560be5238f0748643485cbdd7252dd65b3b699bb676d1439b1@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/d4ts4auv6kddnm"

        # MEGA CONFIG
        MEGA_ENABLE = False
        MEGA_API = ""
        MEGA_UNAME = None
        MEGA_PASS = None

        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "0AAGKChGX7yw2Uk9PVA/1BPEFRmxxCsD4VeeJe82D_6qBTg4o98qS"
        
        # Instagram Credentials Stuff [( if you want InstaDL to work :)]
        INSTA_UNAME = ""
        INSTA_PASS = ""

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = False

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = "[LEECH PRO]
    type = drive
    scope = drive
    root_folder_id =
    token = {"access_token":"ya29.A0ARrdaM8sYBedhLQPdPBMvp0RBHQNzdqBxI0PQSIcCZibDhSsuWikkCBbDPD0C8YPp4INY6A0_I9_taROWZCqWDC5OcwNNnrOOsgeiqtlK2vWC2WSSaWu-mViB1ZUYQUKKVf_L1X-QUg2uCFJS_mWEnpVpUhm","token_type":"Bearer","refresh_token":"1//0gKrLkzZxC3pOCgYIARAAGBASNwF-L9IrbUegaESDxH5TSreETokH3TIeeEkaPliMj2qU0-v9PeUnRBi3PDcJAoe8NUCHH6MfH9k","expiry":"2022-05-10T09:35:46.589105363Z"}
    team_drive = 0AAGKChGX7yw2Uk9PVA"

        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = "LEECH PRO"

        # Max size of a playlist that is allowed (Number of videos)
        MAX_YTPLAYLIST_SIZE = 20

        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 10

        # Custom Trackers for QBT..
        ADD_CUSTOM_TRACKERS = True
        TRACKER_SOURCE = "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt"

        # Set this to your bot username if you want to add the username of your bot at the end of the commands like
        # /leech@TorToolkitBot so the value will be @TorToolkitBot
        BOT_CMD_POSTFIX = ""

        # Time out for the status Delete.
        STATUS_DEL_TOUT = 20

        # Allow the user settings to be accessed in private
        USETTINGS_IN_PRIVATE = False

        # Torrent max time to collect metadata in seconds
        TOR_MAX_TOUT = 180

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50, 10, 2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        EXPRESS_UPLOAD = True
