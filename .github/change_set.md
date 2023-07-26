Commit ID: 319693b238cbcb3de0354aada97a281fe3e4bc15
PR Merge ID: 65
PR Author: reddyfull
Approved by: reddyfull

Commit ID: 0c8b5f43c06141afebd8e056f7e1ca0ea1eebeaa
PR Merge ID: 66
PR Author: reddyfull
Approved by: reddyfull

Commit ID: aad3f31cd267d1dcbc99ea0ead46a49feed9d66c
PR Merge ID: 70
PR Author: reddyfull
Approved by: reddyfull

Changes made:
diff --git a/.github/change_set.md b/.github/change_set.md
index 4aea889..5ef7496 100644
--- a/.github/change_set.md
+++ b/.github/change_set.md
@@ -8,3 +8,9 @@ PR Merge ID: 66
 PR Author: reddyfull
 Approved by: reddyfull
 
+Commit ID: aad3f31cd267d1dcbc99ea0ead46a49feed9d66c
+PR Merge ID: 70
+PR Author: reddyfull
+Approved by: reddyfull
+
+Changes made:
diff --git a/.github/workflows/pr_merge_actions.yml b/.github/workflows/pr_merge_actions.yml
index 6e73005..0fbcdcd 100644
--- a/.github/workflows/pr_merge_actions.yml
+++ b/.github/workflows/pr_merge_actions.yml
@@ -14,6 +14,7 @@ jobs:
       - name: Checkout code
         uses: actions/checkout@v2
         with:
+          token: ${{ secrets.PAT }}
           fetch-depth: 0
       - name: Install GitHub CLI
         run: |

Commit ID: 7b2046d8fbb4ca00ab3aa1479cbebf7bbd099048
PR Merge ID: 71
PR Author: reddyfull
Approved by: reddyfull
PR was merged from branch: main
PR was merged into branch: Release-1.0

Changes made:
diff --git a/.github/change_set.md b/.github/change_set.md
index fed46de..7804d8f 100644
--- a/.github/change_set.md
+++ b/.github/change_set.md
@@ -41,3 +41,11 @@ index 6e73005..0fbcdcd 100644
        - name: Install GitHub CLI
          run: |
 
+Commit ID: 7b2046d8fbb4ca00ab3aa1479cbebf7bbd099048
+PR Merge ID: 71
+PR Author: reddyfull
+Approved by: reddyfull
+PR was merged from branch: main
+PR was merged into branch: Release-1.0
+
+Changes made:
diff --git a/.github/workflows/pr_merge_actions.yml b/.github/workflows/pr_merge_actions.yml
index 0fbcdcd..4d52e26 100644
--- a/.github/workflows/pr_merge_actions.yml
+++ b/.github/workflows/pr_merge_actions.yml
@@ -25,8 +25,12 @@ jobs:
         run: |
           PR_AUTHOR=$(gh pr view https://github.com/${{ github.repository }}/pull/${{ github.event.pull_request.number }} --json author -q ".author.login")
           PR_MERGED_BY=$(gh pr view https://github.com/${{ github.repository }}/pull/${{ github.event.pull_request.number }} --json mergedBy -q ".mergedBy.login")
+          PR_BASE_REF=$(gh pr view https://github.com/${{ github.repository }}/pull/${{ github.event.pull_request.number }} --json baseRefName -q ".baseRefName")
+          PR_HEAD_REF=$(gh pr view https://github.com/${{ github.repository }}/pull/${{ github.event.pull_request.number }} --json headRefName -q ".headRefName")
           echo "PR_AUTHOR=$PR_AUTHOR" >> $GITHUB_ENV
           echo "PR_MERGED_BY=$PR_MERGED_BY" >> $GITHUB_ENV
+          echo "PR_BASE_REF=$PR_BASE_REF" >> $GITHUB_ENV
+          echo "PR_HEAD_REF=$PR_HEAD_REF" >> $GITHUB_ENV
         env:
           GH_TOKEN: ${{ secrets.PAT }}
       - name: Append to change_set.md
@@ -35,6 +39,8 @@ jobs:
           echo "PR Merge ID: ${{ github.event.pull_request.number }}" >> .github/change_set.md
           echo "PR Author: $PR_AUTHOR" >> .github/change_set.md
           echo "Approved by: $PR_MERGED_BY" >> .github/change_set.md
+          echo "PR was merged from branch: $PR_HEAD_REF" >> .github/change_set.md
+          echo "PR was merged into branch: $PR_BASE_REF" >> .github/change_set.md
           echo "" >> .github/change_set.md
       - name: Get and append changes
         run: |
diff --git a/welcome.html b/welcome.html
index 4fea51c..5ceddfe 100644
--- a/welcome.html
+++ b/welcome.html
@@ -1,7 +1,7 @@
 <!DOCTYPE html>
 <html lang="en">
 <head>
-    <title>Welcome to Test ChangeSEt 2 to 3</title>
+    <title>Welcome to Test ChangeSEt 2 to 4</title>
 </head>
 <body>
     <h1>Mocha Testing2</h1>

