from git import Repo
from src.utils import log_info, log_error

class CommitManager:
    def __init__(self, repo_path):
        self.repo = Repo(repo_path)

    def commit_file(self, file_path, message):
        try:
            self.repo.index.add([file_path])
            self.repo.index.commit(message)
            log_info(f"Committed '{file_path}' with message '{message}'")
        except Exception as e:
            log_error(f"Error committing file: {e}")

    def list_commits(self, max_count=10):
        commits = list(self.repo.iter_commits('main', max_count=max_count))
        for commit in commits:
            print(f"{commit.hexsha[:7]} - {commit.message.strip()}")

