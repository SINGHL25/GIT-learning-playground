
#!/bin/bash
# Create, switch, merge branch
git checkout -b feature_branch
echo "Some changes" >> feature.txt
git add feature.txt
git commit -m "Add feature"
git checkout main
git merge feature_branch
