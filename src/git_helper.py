
# Python wrapper for Git commands using GitPython
from git import Repo, GitCommandError
from src.utils import log_info, log_error
import os

class GitHelper:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        if os.path.exists(repo_path):
            self.repo = Repo(repo_path)
        else:
            self.repo = None

    def init_repo(self):
        try:
            self.repo = Repo.init(self.repo_path)
            log_info(f"Initialized repository at {self.repo_path}")
        except GitCommandError as e:
            log_error(f"Error initializing repo: {e}")

    def add_commit_push(self, file_list, commit_msg, remote_name='origin', branch='main'):
        try:
            self.repo.index.add(file_list)
            self.repo.index.commit(commit_msg)
            log_info(f"Committed changes: {commit_msg}")
            origin = self.repo.remote(name=remote_name)
            origin.push(branch)
            log_info(f"Pushed to {branch}")
        except GitCommandError as e:
            log_error(f"Error committing/pushing: {e}")
