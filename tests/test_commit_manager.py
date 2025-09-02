
from src.commit_manager import CommitManager
from src.repo_initializer import initialize_sample_repo
def test_commit_list():
    initialize_sample_repo("cm_repo")
    cm = CommitManager("cm_repo")
    commits = cm.list_commits()
    assert isinstance(commits, list)
