
from git_helper import GitHelper
import os

def initialize_sample_repo(path):
    if not os.path.exists(path):
        os.makedirs(path)
    gh = GitHelper(path)
    gh.init_repo()
    # create initial README
    with open(os.path.join(path, 'README.md'), 'w') as f:
        f.write("# Sample Repo\nInitialized using repo_initializer.py\n")
    gh.add_commit_push(['README.md'], 'Initial commit')

if __name__ == "__main__":
    initialize_sample_repo('sample_repo')
