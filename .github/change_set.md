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

Commit ID: 58e00863e369677cac329c2bf5d1301ef171e3b5
PR Merge ID: 72
PR Author: reddyfull
Approved by: reddyfull
PR was merged from branch: main
PR was merged into branch: Release-1.0

Changes made:
diff --git a/.github/change_set.md b/.github/change_set.md
index ac79b59..bc67e09 100644
--- a/.github/change_set.md
+++ b/.github/change_set.md
@@ -105,3 +105,11 @@ index 4fea51c..5ceddfe 100644
  <body>
      <h1>Mocha Testing2</h1>
 
+Commit ID: 58e00863e369677cac329c2bf5d1301ef171e3b5
+PR Merge ID: 72
+PR Author: reddyfull
+Approved by: reddyfull
+PR was merged from branch: main
+PR was merged into branch: Release-1.0
+
+Changes made:
diff --git a/welcome.html b/welcome.html
index 5ceddfe..786c2b9 100644
--- a/welcome.html
+++ b/welcome.html
@@ -1,10 +1,10 @@
 <!DOCTYPE html>
 <html lang="en">
 <head>
-    <title>Welcome to Test ChangeSEt 2 to 4</title>
+    <title>Welcome to Test ChangeSEt 4 to 5</title>
 </head>
 <body>
-    <h1>Mocha Testing2</h1>
+    <h1>Changeset Testing</h1>
     <a href="https://www.google.com" target="_blank">Welcome to Google</a>
 </body>
 </html>

Commit ID: 12e84271afae9b539f8b1cdeb128c76b76e1f35e
PR Merge ID: 73
PR Author: reddyfull
Approved by: reddyfull
PR was merged from branch: main
PR was merged into branch: Release-1.0

Changes made:
diff --git a/.github/change_set.md b/.github/change_set.md
index f1b8fac..34710f0 100644
--- a/.github/change_set.md
+++ b/.github/change_set.md
@@ -147,3 +147,11 @@ index 5ceddfe..786c2b9 100644
  </body>
  </html>
 
+Commit ID: 12e84271afae9b539f8b1cdeb128c76b76e1f35e
+PR Merge ID: 73
+PR Author: reddyfull
+Approved by: reddyfull
+PR was merged from branch: main
+PR was merged into branch: Release-1.0
+
+Changes made:
diff --git a/.github/workflows/deploy_on_pr_close.yml b/.github/workflows/deploy_on_pr_close.yml
new file mode 100644
index 0000000..b89aebd
--- /dev/null
+++ b/.github/workflows/deploy_on_pr_close.yml
@@ -0,0 +1,112 @@
+name: CI
+
+on:
+  pull_request:
+    types: [closed]
+    branches:
+      - Release-*
+  workflow_dispatch:
+    inputs:
+      run_id:
+        description: 'Run ID'
+        required: true
+
+jobs:
+  build:
+    runs-on: ubuntu-latest
+    environment: 
+      name: 'Test'
+    steps:
+    - name: Print Github Ref
+      run: echo ${{ github.ref }}
+    - name: Print PR merged status
+      run: echo ${{ github.event.pull_request.merged }}
+    - name: Print Run ID
+      run: echo ${{ github.event.inputs.run_id }}
+    - uses: actions/checkout@v2
+    - name: Azure Login
+      uses: azure/login@v1
+      with:
+        creds: ${{ secrets.AZURE_CREDENTIALS }}
+    - name: Login to ACR
+      run: az acr login --name srikali2009
+    - name: Build and push Docker image
+      uses: docker/build-push-action@v2
+      with:
+        context: .
+        push: true
+        tags: srikali2009.azurecr.io/myapp:${{ github.sha }}
+    - name: Validate JSON
+      run: jq . < test_appsettings.json
+    - name: Set Azure Web App settings
+      run: |
+        JSON=`cat test_appsettings.json`
+        for key in $(jq -r 'keys[]' <<< "$JSON"); do
+            value=$(jq -r --arg key "$key" '.[$key]' <<< "$JSON")
+            az webapp config appsettings set --name srikali2009 --resource-group srikali2009 --settings $key=$value
+        done
+    - name: Deploy to Azure Web App
+      uses: azure/webapps-deploy@v2
+      with:
+        app-name: ${{ secrets.AZURE_WEBAPP_NAME }}
+        publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
+        images: srikali2009.azurecr.io/myapp:${{ github.sha }}
+    - name: Dump Github context
+      env:
+        GITHUB_CONTEXT: ${{ toJson(github) }}
+      run: echo "$GITHUB_CONTEXT"
+
+  deploy_to_stage:
+    needs: build
+    if: github.event.pull_request.merged == true
+    runs-on: ubuntu-latest
+    environment:
+      name: 'Stage'
+    steps:
+    - uses: actions/checkout@v2
+    - name: Azure Login
+      uses: azure/login@v1
+      with:
+        creds: ${{ secrets.AZURE_CREDENTIALS }}
+    - name: Validate JSON
+      run: jq . < stage_appsettings.json
+    - name: Set Azure Web App settings
+      run: |
+        JSON=`cat stage_appsettings.json`
+        for key in $(jq -r 'keys[]' <<< "$JSON"); do
+            value=$(jq -r --arg key "$key" '.[$key]' <<< "$JSON")
+            az webapp config appsettings set --name srikalistage2009 --resource-group srikali2009 --settings $key=$value
+        done
+    - name: Deploy to Azure Web App
+      uses: azure/webapps-deploy@v2
+      with:
+        app-name: ${{ secrets.AZURE_STAGE_WEBAPP_NAME }}
+        publish-profile: ${{ secrets.AZURE_STAGE_WEBAPP_PUBLISH_PROFILE }}
+        images: srikali2009.azurecr.io/myapp:${{ github.sha }}
+
+  deploy_to_perf:
+    needs: deploy_to_stage
+    if: github.event.pull_request.merged == true
+    runs-on: ubuntu-latest
+    environment: 
+      name: 'Performance'
+    steps:
+    - uses: actions/checkout@v2
+    - name: Azure Login
+      uses: azure/login@v1
+      with:
+        creds: ${{ secrets.AZURE_CREDENTIALS }}
+    - name: Validate JSON
+      run: jq . < perf_appsettings.json
+    - name: Set Azure Web App settings
+      run: |
+        JSON=`cat perf_appsettings.json`
+        for key in $(jq -r 'keys[]' <<< "$JSON"); do
+            value=$(jq -r --arg key "$key" '.[$key]' <<< "$JSON")
+            az webapp config appsettings set --name srikaliperf2009 --resource-group srikali2009 --settings $key=$value
+        done
+    - name: Deploy to Azure Web App
+      uses: azure/webapps-deploy@v2
+      with:
+        app-name: ${{ secrets.AZURE_PERF_WEBAPP_NAME }}
+        publish-profile: ${{ secrets.AZURE

Commit ID: fd6ac20eb7316dca4bf3a44ea2fd25f2b0f364b5
PR Merge ID: 74
PR Author: reddyfull
Approved by: reddyfull
PR was merged from branch: main
PR was merged into branch: Release-1.0

Changes made:
diff --git a/.github/change_set.md b/.github/change_set.md
index a658ce3..000eec3 100644
--- a/.github/change_set.md
+++ b/.github/change_set.md
@@ -290,3 +290,11 @@ index 0000000..b89aebd
 +        app-name: ${{ secrets.AZURE_PERF_WEBAPP_NAME }}
 +        publish-profile: ${{ secrets.AZURE
 
+Commit ID: fd6ac20eb7316dca4bf3a44ea2fd25f2b0f364b5
+PR Merge ID: 74
+PR Author: reddyfull
+Approved by: reddyfull
+PR was merged from branch: main
+PR was merged into branch: Release-1.0
+
+Changes made:
diff --git a/.github/workflows/deploy_on_pr_close.yml b/.github/workflows/deploy_on_pr_close.yml
index b89aebd..8123984 100644
--- a/.github/workflows/deploy_on_pr_close.yml
+++ b/.github/workflows/deploy_on_pr_close.yml
@@ -109,4 +109,6 @@ jobs:
       uses: azure/webapps-deploy@v2
       with:
         app-name: ${{ secrets.AZURE_PERF_WEBAPP_NAME }}
-        publish-profile: ${{ secrets.AZURE
+        publish-profile: ${{ secrets.AZURE_PUBLISH_PROFILE }}
+        images: srikali2009.azurecr.io/myapp:${{ github.sha }}
+

Commit ID: db62764daee47b61d5cc79d2bb756e2c43c556db
PR Merge ID: 75
PR Author: reddyfull
Approved by: reddyfull
PR was merged from branch: main
PR was merged into branch: Release-1.0

Changes made:
diff --git a/.github/change_set.md b/.github/change_set.md
index 5ecb5ef..61e67ac 100644
--- a/.github/change_set.md
+++ b/.github/change_set.md
@@ -327,3 +327,11 @@ index b89aebd..8123984 100644
 +        images: srikali2009.azurecr.io/myapp:${{ github.sha }}
 +
 
+Commit ID: db62764daee47b61d5cc79d2bb756e2c43c556db
+PR Merge ID: 75
+PR Author: reddyfull
+Approved by: reddyfull
+PR was merged from branch: main
+PR was merged into branch: Release-1.0
+
+Changes made:
diff --git a/.github/workflows/deploy_on_pr_close.yml b/.github/workflows/deploy_on_pr_close.yml
index 8123984..19722bd 100644
--- a/.github/workflows/deploy_on_pr_close.yml
+++ b/.github/workflows/deploy_on_pr_close.yml
@@ -1,10 +1,6 @@
-name: CI
+name: Manual Workflow
 
 on:
-  pull_request:
-    types: [closed]
-    branches:
-      - Release-*
   workflow_dispatch:
     inputs:
       run_id:
@@ -12,103 +8,10 @@ on:
         required: true
 
 jobs:
-  build:
+  run_manual_job:
     runs-on: ubuntu-latest
-    environment: 
-      name: 'Test'
     steps:
-    - name: Print Github Ref
-      run: echo ${{ github.ref }}
-    - name: Print PR merged status
-      run: echo ${{ github.event.pull_request.merged }}
-    - name: Print Run ID
-      run: echo ${{ github.event.inputs.run_id }}
-    - uses: actions/checkout@v2
-    - name: Azure Login
-      uses: azure/login@v1
-      with:
-        creds: ${{ secrets.AZURE_CREDENTIALS }}
-    - name: Login to ACR
-      run: az acr login --name srikali2009
-    - name: Build and push Docker image
-      uses: docker/build-push-action@v2
-      with:
-        context: .
-        push: true
-        tags: srikali2009.azurecr.io/myapp:${{ github.sha }}
-    - name: Validate JSON
-      run: jq . < test_appsettings.json
-    - name: Set Azure Web App settings
-      run: |
-        JSON=`cat test_appsettings.json`
-        for key in $(jq -r 'keys[]' <<< "$JSON"); do
-            value=$(jq -r --arg key "$key" '.[$key]' <<< "$JSON")
-            az webapp config appsettings set --name srikali2009 --resource-group srikali2009 --settings $key=$value
-        done
-    - name: Deploy to Azure Web App
-      uses: azure/webapps-deploy@v2
-      with:
-        app-name: ${{ secrets.AZURE_WEBAPP_NAME }}
-        publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
-        images: srikali2009.azurecr.io/myapp:${{ github.sha }}
-    - name: Dump Github context
-      env:
-        GITHUB_CONTEXT: ${{ toJson(github) }}
-      run: echo "$GITHUB_CONTEXT"
-
-  deploy_to_stage:
-    needs: build
-    if: github.event.pull_request.merged == true
-    runs-on: ubuntu-latest
-    environment:
-      name: 'Stage'
-    steps:
-    - uses: actions/checkout@v2
-    - name: Azure Login
-      uses: azure/login@v1
-      with:
-        creds: ${{ secrets.AZURE_CREDENTIALS }}
-    - name: Validate JSON
-      run: jq . < stage_appsettings.json
-    - name: Set Azure Web App settings
-      run: |
-        JSON=`cat stage_appsettings.json`
-        for key in $(jq -r 'keys[]' <<< "$JSON"); do
-            value=$(jq -r --arg key "$key" '.[$key]' <<< "$JSON")
-            az webapp config appsettings set --name srikalistage2009 --resource-group srikali2009 --settings $key=$value
-        done
-    - name: Deploy to Azure Web App
-      uses: azure/webapps-deploy@v2
-      with:
-        app-name: ${{ secrets.AZURE_STAGE_WEBAPP_NAME }}
-        publish-profile: ${{ secrets.AZURE_STAGE_WEBAPP_PUBLISH_PROFILE }}
-        images: srikali2009.azurecr.io/myapp:${{ github.sha }}
-
-  deploy_to_perf:
-    needs: deploy_to_stage
-    if: github.event.pull_request.merged == true
-    runs-on: ubuntu-latest
-    environment: 
-      name: 'Performance'
-    steps:
-    - uses: actions/checkout@v2
-    - name: Azure Login
-      uses: azure/login@v1
-      with:
-        creds: ${{ secrets.AZURE_CREDENTIALS }}
-    - name: Validate JSON
-      run: jq . < perf_appsettings.json
-    - name: Set Azure Web App settings
-      run: |
-        JSON=`cat perf_appsettings.json`
-        for key in $(jq -r 'keys[]' <<< "$JSON"); do
-            value=$(jq -r --arg key "$key" '.[$key]' <<< "$JSON")
-            az webapp config appsettings set --name srikaliperf2009 --resource-group srikali2009 --settings $key=$value
-        done
-    - name: Deploy to Azure Web App
-      uses: azure/webapps-deploy@v2
-      with:
-        app-name: ${{ secrets.AZURE_PERF_WEBAPP_NAME }}
-        publish-profile: ${{ secrets.AZURE_PUBLISH_PROFILE }}
-        images: srikali2009.azurecr.io/myapp:${{ github.sha }}
-
+      - name: Checkout repository
+        uses: actions/checkout@v2
+      - name: Print run_id
+        run: echo ${{ github.event.inputs.run_id }}

