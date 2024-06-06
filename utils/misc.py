from sys import version_info
from .db import db
import git

__all__ = [
    "modules_help",
    "requirements_list",
    "python_version",
    "prefix",
    "gitrepo",
    "userbot_version",
]


modules_help = {}
requirements_list = []

python_version = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"

prefix = db.get("core.main", "prefix", ".")

try:
    gitrepo = git.Repo(".")
except git.exc.InvalidGitRepositoryError:
    repo = git.Repo.init()
    origin = repo.create_remote(
        "origin", "https://github.com/Cloudy-Userbot/Cloudy-Userbot"
    )
    origin.fetch()
    repo.create_head("master", origin.refs.master)
    repo.heads.master.set_tracking_branch(origin.refs.master)
    repo.heads.master.checkout(True)
    gitrepo = git.Repo(".")

commits_since_tag = list(gitrepo.iter_commits(f"{gitrepo.tags[-1].name}..HEAD"))
userbot_version = f"4.0.{len(commits_since_tag)}"
