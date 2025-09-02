
from src.branch_manager import BranchManager
from src.repo_initializer import initialize_sample_repo
def test_branch():
    initialize_sample_repo("bm_repo")
    bm = BranchManager("bm_repo")
    bm.create_branch("test-branch")
    # no exception = pass
    assert True
