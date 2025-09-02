
from src.git_helper import GitHelper
from src.repo_initializer import initialize_sample_repo
def test_git_helper_init():
    initialize_sample_repo("gh_repo")
    gh = GitHelper("gh_repo")
    assert gh.repo is not None
