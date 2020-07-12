import os
import json
import asyncio

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from aiocron import crontab


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


@app.route("/slack")
def event_hook(request):
    json_dict = json.loads(request.body.decode("utf-8"))
    # if json_dict["token"] != VERIFICATION_TOKEN:
    #     return {"status": 403}
    if "type" in json_dict:
        if json_dict["type"] == "url_verification":
            response_dict = {"challenge": json_dict["challenge"]}
            return response_dict
    return {"status": 500}


from project import slack_interface
from project.http import process_batch

# crontab(
#     "* * * * *",
#     func=lambda: process_batch([lambda: slack_send_msg("Testing my boundaries!")]),
#     start=True,
# )
