import datetime
import sys
from pyrogram import Client, errors

from utils import config

if __name__ == "__main__":
    app = Client(
        "my_account",
        api_id=config.api_id,
        api_hash=config.api_hash,
        hide_password=True,
        test_mode=config.test_server,
    )

    if config.db_type in ["mongo", "mongodb"]:
        from pymongo import MongoClient, errors

        db = MongoClient(config.db_url)
        try:
            db.server_info()
        except errors.ConnectionFailure as e:
            raise RuntimeError(
                "MongoDB server isn't available! "
                f"Provided url: {config.db_url}. "
                "Enter valid URL and restart installation"
            ) from e

    install_type = sys.argv[1] if len(sys.argv) > 1 else "3"
    if install_type == "1":
        restart = "pm2 restart cloudy"
    elif install_type == "2":
        restart = "sudo systemctl restart cloudy"
    else:
        restart = "cd Cloudy-Userbot/ && python main.py"

    app.start()
    try:
        app.send_message(
            "me",
            f"<b>[{datetime.datetime.now()}] Cloudy-Userbot launched! \n"
            f"For restart, enter:</b>\n"
            f"<code>{restart}</code>",
        )
    except errors.RPCError:
        pass
    app.stop()
