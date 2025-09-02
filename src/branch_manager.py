
from git import Repo
from src.utils import log_info, log_error

class BranchManager:
    def __init__(self, repo_path):
        self.repo = Repo(repo_path)

    def create_branch(self, branch_name):
        try:
            new_branch = self.repo.create_head(branch_name)
            log_info(f"Branch '{branch_name}' created")
        except Exception as e:
            log_error(f"Error creating branch: {e}")

    def switch_branch(self, branch_name):
        try:
            self.repo.git.checkout(branch_name)
            log_info(f"Switched to branch '{branch_name}'")
        except Exception as e:
            log_error(f"Error switching branch: {e}")

    def merge_branch(self, source_branch, target_branch):
        try:
            self.repo.git.checkout(target_branch)
            self.repo.git.merge(source_branch)
            log_info(f"Merged '{source_branch}' into '{target_branch}'")
        except Exception as e:
            log_error(f"Error merging branches: {e}")
