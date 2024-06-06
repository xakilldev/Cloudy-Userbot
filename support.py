from pyrogram import Client, filters
from pyrogram.types import Message
import random
import datetime

from utils.misc import (
    modules_help,
    prefix,
    userbot_version,
    python_version,
    gitrepo,
)


@Client.on_message(filters.command(["support", "repo"], prefix) & filters.me)
async def support(_, message: Message):
    devs = ["@john_ph0nk", "@fuccsoc2"]
    random.shuffle(devs)

    commands_count = float(
        len([cmd for module in modules_help for cmd in module])
    )

    await message.edit(
        f"<b>Cloudy-Userbot\n\n"
        "GitHub: <a href=https://github.com/Cloudy-Userbot/Cloudy-Userbot>Cloudy-Userbot/Cloudy-Userbot</a>\n"
        "Custom modules repository: <a href=https://github.com/Cloudy-Userbot/custom_modules>"
        "Cloudy-Userbot/custom_modules</a>\n"
        f"Developer: @cryptoaccurately \n\n"
        f"Python version: {python_version}\n"
        f"Modules count: {len(modules_help) / 1}\n"
        f"Commands count: {commands_count}</b>",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command(["version", "ver"], prefix) & filters.me)
async def version(client: Client, message: Message):
    changelog = ""
    ub_version = ".".join(userbot_version.split(".")[:2])
    async for m in client.search_messages(
        "cLoUdY_uB_cHaNgElOg", query=ub_version + "."
    ):
        if ub_version in m.text:
            changelog = m.id

    await message.delete()

    remote_url = list(gitrepo.remote().urls)[0]
    commit_time = (
        datetime.datetime.fromtimestamp(gitrepo.head.commit.committed_date)
        .astimezone(datetime.timezone.utc)
        .strftime("%Y-%m-%d %H:%M:%S %Z")
    )

    await message.reply(
        f"<b>Cloudy Userbot version: {userbot_version}\n"
        + (
            f"<b>Branch: <a href={remote_url}/tree/{gitrepo.active_branch}>{gitrepo.active_branch}</a>\n"
            if gitrepo.active_branch != "master"
            else ""
        )
        + f"Commit: <a href={remote_url}/commit/{gitrepo.head.commit.hexsha}>"
        f"{gitrepo.head.commit.hexsha[:7]}</a> by {gitrepo.head.commit.author.name}\n"
        f"Commit time: {commit_time}</b>",
    )


modules_help["support"] = {
    "support": "Information about userbot",
    "version": "Check userbot version",
}
