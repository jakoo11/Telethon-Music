import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5556290984:AAEIk2nZQCW1lRpfBabTi4d_XwviVxoJd0M")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu8YQHXCbJfOaC84nCM8YjLpIsLKNk7BhRJwCAwSYwRdnGYF1yqOTV51acR7yHEBaVi22YFZBc0Q4HgQetARNWTtw3ABIuiUdxWjNIhanifclxth07MWm9tbY5NHY8jCnqydaLWuxfd71kF-pw9dlE7l4LHb7sRzmN-ZNRsvrP0cK58Ju4SzqCbdFpgSlHfHW4qopbTx8P1en2AdXYV0OqyEXv93RwMOaI4_iGC1y21QGdDbtJ7idxH2HwhPrF5f3VuZ3yujMFtnRoRKk8-QeoBdHR_PJVWeOgaPOUYTYjKaB4yXJ3rcUnIVemXvhKjrtwbqpnHa83AO7LK253kWyPb0=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Jhffgy677_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
