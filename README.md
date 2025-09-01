# GIT-learning-playground
<img width="2048" height="2048" alt="Gemini_Generated_Image_xryevtxryevtxrye" src="https://github.com/user-attachments/assets/4c76f3b4-822a-4f4e-a4a8-6e544caeb957" />

```Plain text

git-learning-playground/
│── README.md                     # Overview, objectives, setup instructions
│── requirements.txt              # Python libraries if any (GitPython, etc.)
│── .gitignore                    # Ignore venv, logs, temp files
│── main.py                       # Optional dashboard or practice script
│
├── docs/
│   ├── intro.md                  # What is Git, version control, benefits
│   ├── git_vs_github.md          # Differences: Git, GitHub, GitLab, Bitbucket
│   ├── installation.md           # Git CLI setup for Windows, Linux, Mac
│   ├── basic_commands.md         # git init, clone, add, commit, push, pull
│   ├── branching.md              # git branch, checkout, merge, rebase
│   ├── remote_repo.md            # git remote add, fetch, push, pull, clone
│   ├── github_workflow.md        # Fork, pull request, issues, releases
│   ├── gitlab_workflow.md        # CI/CD pipelines, issues, merge requests
│   ├── advanced_git.md           # Revert, reset, stash, cherry-pick, tags
│   ├── cli_vs_gui.md             # Git CLI vs GUI (GitHub Desktop, GitKraken)
│   └── best_practices.md         # Commit messages, branching strategy, hooks
│
├── src/
│   ├── __init__.py
│   ├── git_helper.py             # Python wrapper for Git commands (GitPython)
│   ├── repo_initializer.py       # Initialize sample repo programmatically
│   ├── branch_manager.py         # Create, merge, delete branches
│   ├── commit_manager.py         # Automate commits, messages
│   └── utils.py                  # Helper functions (logging, errors)
│
├── examples/
│   ├── cli_examples/             # Bash/PowerShell CLI examples
│   │    ├── init_clone.sh
│   │    ├── commit_push.sh
│   │    └── branch_merge.sh
│   ├── github_examples/          # GitHub real use-case repo structure
│   │    ├── README.md
│   │    ├── main.py
│   │    └── feature_branch.py
│   └── gitlab_examples/          # GitLab repo & CI/CD pipeline example
│        ├── .gitlab-ci.yml
│        ├── app.py
│        └── tests/
│             └── test_app.py
│
├── notebooks/
│   ├── 01_git_basics.ipynb       # Practice Git commands with Python (GitPython)
│   ├── 02_branching.ipynb        # Branch creation, merging, conflicts demo
│   ├── 03_github.ipynb           # Connect repo, create PRs, manage issues
│   ├── 04_gitlab.ipynb           # CI/CD pipeline demo & commits
│   ├── 05_advanced_git.ipynb     # Revert, reset, stash, tag practice
│   └── 06_real_usecase.ipynb     # End-to-end repo workflow simulation
│
├── tests/
│   ├── test_repo_initializer.py
│   ├── test_branch_manager.py
│   ├── test_commit_manager.py
│   └── test_git_helper.py
│
└── results/
    ├── logs/                     # Git CLI outputs, merge conflicts logs
    ├── screenshots/              # GUI examples, GitHub/GitLab views
    │    ├── github_pr.png
    │    ├── gitlab_pipeline.png
    │    ├── branch_merge.png
    │    └── commit_history.png
    └── plots/                    # Optional workflow diagrams
         ├── git_flow.png
         ├── commit_graph.png
         └── ci_cd_flow.png
