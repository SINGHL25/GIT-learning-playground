
from src.repo_initializer import initialize_sample_repo
import os
def test_init():
    initialize_sample_repo("test_repo")
    assert os.path.exists("test_repo/README.md")
