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

