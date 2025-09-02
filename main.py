

---

### `main.py`
```python
"""
Optional simple CLI / demo for git-learning-playground.
Run: python main.py
"""
import argparse
from src.repo_initializer import initialize_sample_repo
from src.git_helper import GitHelper
from src.utils import log_info

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--init", help="Initialize sample repo", action="store_true")
    parser.add_argument("--demo-commit", help="Demo commit in sample_repo", action="store_true")
    args = parser.parse_args()

    if args.init:
        initialize_sample_repo("sample_repo")
        log_info("Sample repo initialized in ./sample_repo")

    if args.demo_commit:
        gh = GitHelper("sample_repo")
        if not gh.repo:
            print("Repo not found. Run --init first.")
            return
        # create a demo file
        with open("sample_repo/demo.txt", "w") as f:
            f.write("demo commit\n")
        gh.add_commit_push(["demo.txt"], "Add demo file", branch="main")
        log_info("Demo commit pushed (if remote configured).")

if __name__ == "__main__":
    main()
