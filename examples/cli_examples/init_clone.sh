
#!/bin/bash
# Initialize local repo and clone remote repo
echo "Initializing local repository..."
git init my_repo
cd my_repo
echo "Cloning remote repository..."
git clone https://github.com/username/sample_repo.git
