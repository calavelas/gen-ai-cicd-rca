import vertexai
from vertexai.preview.language_models import TextGenerationModel

vertexai.init(project="ccoe-lab", location="asia-southeast1")
parameters = {
    "max_output_tokens": 2048,
    "temperature": 0.9,
    "top_p": 1
}
model = TextGenerationModel.from_pretrained("gemini-pro")
response = model.predict(
    """- This is logs from GitlabCI job 
- This job is for analyzing Kustomize repository and make sure it up to our company standard
- This job is failing

With these context, I want you to analyze logs why this job is failing , what is the potential issues and what is potential fix that pipeline user can fix it themself
Note that error should be in few latest row, and we usually include human readable error in on why it failing leverage that for providing more understandable context for pipeline user

input: [0KRunning with gitlab-runner 15.5.0 (0d4137b8)[0;m
[0K  on ccoe-ss-gitlab-runner-84d9bcfbb6-kd4nn 4VHoLdsc[0;m
section_start:1706600641:prepare_executor
[0K[0K[36;1mPreparing the \"kubernetes\" executor[0;m[0;m
[0KUsing Kubernetes namespace: ccoe-ss[0;m
[0KUsing Kubernetes executor with image asia.gcr.io/krungthai-next-devops/poc/ccoe-mergeci-utility:7e615b6c ...[0;m
[0KUsing attach strategy to execute scripts...[0;m
section_end:1706600641:prepare_executor
[0Ksection_start:1706600641:prepare_script
[0K[0K[36;1mPreparing environment[0;m[0;m
Waiting for pod ccoe-ss/runner-4vholdsc-project-9797-concurrent-1ng2lr to be running, status is Pending
	ContainersNotInitialized: \"containers with incomplete status: [init-permissions]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Waiting for pod ccoe-ss/runner-4vholdsc-project-9797-concurrent-1ng2lr to be running, status is Pending
	ContainersNotInitialized: \"containers with incomplete status: [init-permissions]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Waiting for pod ccoe-ss/runner-4vholdsc-project-9797-concurrent-1ng2lr to be running, status is Pending
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Waiting for pod ccoe-ss/runner-4vholdsc-project-9797-concurrent-1ng2lr to be running, status is Pending
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Running on runner-4vholdsc-project-9797-concurrent-1ng2lr via ccoe-ss-gitlab-runner-84d9bcfbb6-kd4nn...

section_end:1706600668:prepare_script
[0Ksection_start:1706600668:get_sources
[0K[0K[36;1mGetting source from Git repository[0;m[0;m
[32;1mFetching changes with git depth set to 50...[0;m
Initialized empty Git repository in /builds/cicd/kustomize/welfare-platform/customer-update-info-subscriber/.git/
[32;1mCreated fresh repository.[0;m
[32;1mChecking out 454bf11d as refs/merge-requests/21/head...[0;m

[32;1mSkipping Git submodules setup[0;m

section_end:1706600671:get_sources
[0Ksection_start:1706600671:step_script
[0K[0K[36;1mExecuting \"step_script\" stage of the job script[0;m[0;m
[32;1m$ analyzer run[0;m
[0;32m[INFO] [secrets] [2024-01-30T07:44:31Z] ▶ GitLab secrets analyzer v5.1.3[0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:31Z] ▶ Detecting project[0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:31Z] ▶ Analyzer will attempt to analyze all projects in the repository[0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:31Z] ▶ Running analyzer[0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:31Z] ▶ [0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:31Z] ▶     ○[0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:31Z] ▶     │╲[0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:31Z] ▶     │ ○[0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:31Z] ▶     ○ ░[0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:31Z] ▶     ░    gitleaks[0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:31Z] ▶ [0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:32Z] ▶ [90m7:44AM[0m [32mINF[0m 6 commits scanned.[0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:32Z] ▶ [90m7:44AM[0m [32mINF[0m scan completed in 247ms[0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:32Z] ▶ [90m7:44AM[0m [32mINF[0m no leaks found[0m
[0;32m[INFO] [secrets] [2024-01-30T07:44:32Z] ▶ Creating report[0m
[32;1m$ cat gl-secret-detection-report.json | jq \'.\'[0;m
{
  \"version\": \"15.0.4\",
  \"vulnerabilities\": [],
  \"dependency_files\": [],
  \"scan\": {
    \"analyzer\": {
      \"id\": \"secrets\",
      \"name\": \"secrets\",
      \"url\": \"https://gitlab.com/gitlab-org/security-products/analyzers/secrets\",
      \"vendor\": {
        \"name\": \"GitLab\"
      },
      \"version\": \"5.1.3\"
    },
    \"scanner\": {
      \"id\": \"gitleaks\",
      \"name\": \"Gitleaks\",
      \"url\": \"https://github.com/zricethezav/gitleaks\",
      \"vendor\": {
        \"name\": \"GitLab\"
      },
      \"version\": \"\"
    },
    \"type\": \"secret_detection\",
    \"start_time\": \"2024-01-30T07:44:31\",
    \"end_time\": \"2024-01-30T07:44:32\",
    \"status\": \"success\"
  }
}
[32;1m$ leak_found=$(cat gl-secret-detection-report.json | jq \'.vulnerabilities | length > 0\')[0;m
[32;1m$ FAIL_FLAG=\"false\"[0;m
[32;1m$ if [ \"$leak_found\" = \"true\" ]; then # collapsed multi-line command[0;m
[92;1mScan Complete, No Leak Found.[0m
[32;1m$ KUSTOMIZE_PRD_PATH=$(echo $CI_PROJECT_DIR | cut -c 8- | sed \"s/\\/kustomize\\//\\/kustomize-prd\\//g\")[0;m
[32;1m$ for OVERLAY_PRD_PATH in ${OVERLAY_PRD_PATHS} # collapsed multi-line command[0;m
[1mSecret Keys Validation for overlays/prd[0m
[94mSecret Key                              [94mPlaceholder Key                           [94mStatus           [94mDescription                                                    
[97mKAFKA_USERNAME                          [97mscsmsg_privilege_system                   [91mInvalid          [93mPlaceholder key not found, Please contact DevOps team          
[97mKAFKA_PASSWORD                          [97m[MASKED]                           [91mInvalid          [93mPlaceholder key not found, Please contact DevOps team          
[97mKAFKA_TRUSTSTORE_PASSWORD               [97m[MASKED]                                [91mInvalid          [93mPlaceholder key not found, Please contact DevOps team          
[97mWELFARE_EP_EKYC_ENCRYPTION_KEY          [97mkbcptgpm5OegmJN7                          [91mInvalid          [93mPlaceholder key not found, Please contact DevOps team          
[97mWELFARE_EP_EKYC_ENCRYPTION_IV           [97mnlOqfSqvdTj8                              [91mInvalid          [93mPlaceholder key not found, Please contact DevOps team          
[97mWELFARE_CID_ENCRYPTION_KEY              [97m[MASKED]          [91mInvalid          [93mPlaceholder key not found, Please contact DevOps team          
[97mWELFARE_CID_ENCRYPTION_IV               [97mk2pz8UqJuKBVoLJgwb93JQ                    [91mInvalid          [93mPlaceholder key not found, Please contact DevOps team          


section_end:1706600673:step_script
[0Ksection_start:1706600673:after_script
[0K[0K[36;1mRunning after_script[0;m[0;m
[32;1mRunning after script...[0;m
[32;1m$ leak_found=$(cat gl-secret-detection-report.json | jq \'.vulnerabilities | length > 0\')[0;m
[32;1m$ if [ \"$leak_found\" = \"true\" ]; then # collapsed multi-line command[0;m

section_end:1706600674:after_script
[0Ksection_start:1706600674:cleanup_file_variables
[0K[0K[36;1mCleaning up project directory and file based variables[0;m[0;m

section_end:1706600675:cleanup_file_variables
[0K[31;1mERROR: Job failed: command terminated with exit code 1
[0;m
output: Potential Issues 
- There are no placeholder keys found in the overlay directory.

Potential Fix
- Verify that you have set the correct placeholder keys in the overlay directory for secrets like KAFKA_USERNAME, KAFKA_PASSWORD and WELFARE_EP_EKYC_ENCRYPTION_KEY, WELFARE_EP_EKYC_ENCRYPTION_IV, WELFARE_CID_ENCRYPTION_KEY, WELFARE_CID_ENCRYPTION_IV.
- Make sure that the placeholder keys are valid and correspond to actual secret values stored in the secrets manager.

input: Running with gitlab-runner 15.5.0 (0d4137b8)
  on ccoe-ss-gitlab-runner-84d9bcfbb6-gf5k5 XnQYL9rZ
Preparing the \"kubernetes\" executor
00:00
Using Kubernetes namespace: ccoe-ss
Using Kubernetes executor with image asia.gcr.io/krungthai-next-devops/poc/ccoe-mergeci-utility:7e615b6c ...
Using attach strategy to execute scripts...
Preparing environment
00:25
Waiting for pod ccoe-ss/runner-xnqyl9rz-project-29668-concurrent-02khwl to be running, status is Pending
Waiting for pod ccoe-ss/runner-xnqyl9rz-project-29668-concurrent-02khwl to be running, status is Pending
	ContainersNotInitialized: \"containers with incomplete status: [init-permissions]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Waiting for pod ccoe-ss/runner-xnqyl9rz-project-29668-concurrent-02khwl to be running, status is Pending
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Waiting for pod ccoe-ss/runner-xnqyl9rz-project-29668-concurrent-02khwl to be running, status is Pending
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Running on runner-xnqyl9rz-project-29668-concurrent-02khwl via ccoe-ss-gitlab-runner-84d9bcfbb6-gf5k5...
Getting source from Git repository
00:02
Fetching changes with git depth set to 20...
Initialized empty Git repository in /builds/cicd/kustomize/paotang-gov-cmmn/pt-gov-geography-api/.git/
Created fresh repository.
Checking out e2df611b as refs/merge-requests/18/head...
Skipping Git submodules setup
Executing \"step_script\" stage of the job script
00:05
$ git config --global user.email \"runner@devops.krungthai.com\"
$ git config --global user.name \"runner\"
$ curl -LO https://github.com/yannh/kubeconform/releases/download/v${KUBE_CONFORM_VERSION}/kubeconform-linux-amd64.tar.gz && tar xf kubeconform-linux-amd64.tar.gz && chmod +x ./kubeconform && mv ./kubeconform /usr/local/bin/kubeconform
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 5604k  100 5604k    0     0  5519k      0  0:00:01  0:00:01 --:--:-- 30.2M
$ git fetch --all
From https://gitdev.devops.krungthai.com/cicd/kustomize/paotang-gov-cmmn/pt-gov-geography-api
 * [new branch]      develop       -> origin/develop
 * [new branch]      main          -> origin/main
 * [new branch]      main-02c9e7cb -> origin/main-02c9e7cb
$ git branch -r
  origin/develop
  origin/main
  origin/main-02c9e7cb
$ echo -e \"\\e[34;1mPreparing files for compare from target branch \'$CI_MERGE_REQUEST_TARGET_BRANCH_NAME\'\\e[0m\"
Preparing files for compare from target branch \'main\'
$ ls
LICENSE
README.md
base
kubeconform-linux-amd64.tar.gz
overlays
$ git checkout $CI_MERGE_REQUEST_TARGET_BRANCH_NAME
Previous HEAD position was e2df611 remove probe
branch \'main\' set up to track \'origin/main\'.
Switched to a new branch \'main\'
$ mkdir temp
$ cp -R overlays temp
$ ls
LICENSE
README.md
base
kubeconform-linux-amd64.tar.gz
overlays
temp
$ ls temp
overlays
$ git checkout $CI_MERGE_REQUEST_SOURCE_BRANCH_NAME
branch \'develop\' set up to track \'origin/develop\'.
Switched to a new branch \'develop\'
$ echo \"Done ...\"
Done ...
$ echo -e \"\\e[34;1mChecking MR title pattern, expect [ENV] Ex. [sit]/[SIT]\\e[0m\"
Checking MR title pattern, expect [ENV] Ex. [sit]/[SIT]
$ TARGET_OVERLAY=$(echo $CI_MERGE_REQUEST_TITLE | grep -Eo \'^\\[(.*(([sS][iI][tT])|([uU][aA][tT])|([sS][tT][gG])|([pP][fF][mM])|([pP][rR][dD])).*)\\]\' |  sed -E \'s/^\\[|\\]$//g\' | awk \'{print tolower($0)}\')
$ if [ \"$TARGET_OVERLAY\" == \"\" ]; then # collapsed multi-line command
$ COMMON_ANCESTOR=$(git merge-base origin/$CI_MERGE_REQUEST_SOURCE_BRANCH_NAME origin/$CI_MERGE_REQUEST_TARGET_BRANCH_NAME)
$ DIFF_DETAILS=$(git diff --name-only $COMMON_ANCESTOR..origin/$CI_MERGE_REQUEST_SOURCE_BRANCH_NAME)
$ if [[ \"$(echo $DIFF_DETAILS | grep -E -v \"overlays/$TARGET_OVERLAY\" | wc -l)\" != \"0\" ]]; then # collapsed multi-line command
Validation Check Failed
Changes outside of overlays/sit are not allowed for this MR.
Please ensure that changes is matching merge request name
Diff Details
Cleaning up project directory and file based variables
00:00
ERROR: Job failed: command terminated with exit code 1
output: Potential Issues (Root Cause Analysis):
- Changes outside of overlays/sit are not allowed for this MR
- There are changes outside of the `overlays/sit` directory, which is not allowed for this merge request.
- The merge request title does not match the expected pattern of `[ENV] Ex. [sit]/[SIT]`.

Potential Fix:
- Ensure that the merge request title follows the expected pattern.
- Make sure that all changes are within the `overlays/sit` directory.

input: Running with gitlab-runner 15.5.0 (0d4137b8)
  on ccoe-ss-gitlab-runner-84d9bcfbb6-hvs7n RrWzBRar
Preparing the \"kubernetes\" executor
00:00
Using Kubernetes namespace: ccoe-ss
Using Kubernetes executor with image asia.gcr.io/krungthai-next-devops/poc/ccoe-mergeci-utility:7e615b6c ...
Using attach strategy to execute scripts...
Preparing environment
00:20
Waiting for pod ccoe-ss/runner-rrwzbrar-project-26984-concurrent-0ggm4c to be running, status is Pending
	ContainersNotInitialized: \"containers with incomplete status: [init-permissions]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Waiting for pod ccoe-ss/runner-rrwzbrar-project-26984-concurrent-0ggm4c to be running, status is Pending
	ContainersNotInitialized: \"containers with incomplete status: [init-permissions]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Waiting for pod ccoe-ss/runner-rrwzbrar-project-26984-concurrent-0ggm4c to be running, status is Pending
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Running on runner-rrwzbrar-project-26984-concurrent-0ggm4c via ccoe-ss-gitlab-runner-84d9bcfbb6-hvs7n...
Getting source from Git repository
00:06
Fetching changes with git depth set to 20...
Initialized empty Git repository in /builds/cicd/kustomize/apm-poc/reg-customer-api/.git/
Created fresh repository.
Checking out 2c0009e0 as refs/merge-requests/1/head...
Skipping Git submodules setup
Executing \"step_script\" stage of the job script
00:06
$ git config --global user.email \"runner@devops.krungthai.com\"
$ git config --global user.name \"runner\"
$ curl -LO https://github.com/yannh/kubeconform/releases/download/v${KUBE_CONFORM_VERSION}/kubeconform-linux-amd64.tar.gz && tar xf kubeconform-linux-amd64.tar.gz && chmod +x ./kubeconform && mv ./kubeconform /usr/local/bin/kubeconform
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 5604k  100 5604k    0     0  3128k      0  0:00:01  0:00:01 --:--:--  195M
$ git fetch --all
From https://gitdev.devops.krungthai.com/cicd/kustomize/apm-poc/reg-customer-api
 * [new branch]      kanin.k-main-patch-0546 -> origin/kanin.k-main-patch-0546
 * [new branch]      main                    -> origin/main
$ git branch -r
  origin/kanin.k-main-patch-0546
  origin/main
$ echo -e \"\\e[34;1mPreparing files for compare from target branch \'$CI_MERGE_REQUEST_TARGET_BRANCH_NAME\'\\e[0m\"
Preparing files for compare from target branch \'main\'
$ ls
LICENSE
README.md
base
kubeconform-linux-amd64.tar.gz
overlays
$ git checkout $CI_MERGE_REQUEST_TARGET_BRANCH_NAME
Previous HEAD position was 2c0009e Update file secret.env
branch \'main\' set up to track \'origin/main\'.
Switched to a new branch \'main\'
$ mkdir temp
$ cp -R overlays temp
$ ls
LICENSE
README.md
base
kubeconform-linux-amd64.tar.gz
overlays
temp
$ ls temp
overlays
$ git checkout $CI_MERGE_REQUEST_SOURCE_BRANCH_NAME
branch \'kanin.k-main-patch-0546\' set up to track \'origin/kanin.k-main-patch-0546\'.
Switched to a new branch \'kanin.k-main-patch-0546\'
$ echo \"Done ...\"
Done ...
$ echo -e \"\\e[34;1mChecking MR title pattern, expect [ENV] Ex. [sit]/[SIT]\\e[0m\"
Checking MR title pattern, expect [ENV] Ex. [sit]/[SIT]
$ TARGET_OVERLAY=$(echo $CI_MERGE_REQUEST_TITLE | grep -Eo \'^\\[(.*(([sS][iI][tT])|([uU][aA][tT])|([sS][tT][gG])|([pP][fF][mM])|([pP][rR][dD])).*)\\]\' |  sed -E \'s/^\\[|\\]$//g\' | awk \'{print tolower($0)}\')
$ if [ \"$TARGET_OVERLAY\" == \"\" ]; then # collapsed multi-line command
$ COMMON_ANCESTOR=$(git merge-base origin/$CI_MERGE_REQUEST_SOURCE_BRANCH_NAME origin/$CI_MERGE_REQUEST_TARGET_BRANCH_NAME)
$ DIFF_DETAILS=$(git diff --name-only $COMMON_ANCESTOR..origin/$CI_MERGE_REQUEST_SOURCE_BRANCH_NAME)
$ if [[ \"$(echo $DIFF_DETAILS | grep -E -v \"overlays/$TARGET_OVERLAY\" | wc -l)\" != \"0\" ]]; then # collapsed multi-line command
$ RAW_RE=\"dev sit uat stg pfm prd datadog dynatrace\"
$ for CONST_RE in $RAW_RE; do # collapsed multi-line command
Adding (.*dev.*)
Adding (.*sit.*)
Adding (.*stg.*)
Adding (.*pfm.*)
Adding (.*prd.*)
Adding (.*datadog.*)
Adding (.*dynatrace.*)
$ echo $RE
(.*dynatrace.*)|(.*datadog.*)|(.*prd.*)|(.*pfm.*)|(.*stg.*)|(.*sit.*)|(.*dev.*)
$ if [[ \"$(echo $DIFF_DETAILS | grep -E $RE | wc -l)\" != \"0\" ]]; then # collapsed multi-line command
$ echo -e \"\\e[92;1mValidate target overlays change, Done\\e[0m\"
Validate target overlays change, Done
$ echo \"Running Validation for base folder\"
Running Validation for base folder
$ if [[ \"$(git diff --name-only origin/$CI_MERGE_REQUEST_SOURCE_BRANCH_NAME origin/$CI_MERGE_REQUEST_TARGET_BRANCH_NAME -- base/ | wc -l)\" != \"0\" ]]; then # collapsed multi-line command
Validation for base folder - done
$ echo \"Running Validation for .env configmap file\"
Running Validation for .env configmap file
$ ROOT_DIR=`pwd` # collapsed multi-line command
find: /builds/cicd/kustomize/apm-poc/reg-customer-api/overlays/datadog/configs: No such file or directory
Cleaning up project directory and file based variables
00:01
ERROR: Job failed: command terminated with exit code 1
output: Potential Issues (Root Cause Analysis): Potential Issues (Root Cause Analysis):
- The merge request title does not match the expected pattern of `[ENV] Ex. [sit]/[SIT]`.

Potential Fix:
- Ensure that the merge request title follows the expected pattern.
- Make sure that all changes are within the `overlays/sit` directory.

input: Running with gitlab-runner 15.5.0 (0d4137b8)
  on ccoe-ss-gitlab-runner-84d9bcfbb6-hvs7n RrWzBRar
Preparing the \"kubernetes\" executor
00:00
Using Kubernetes namespace: ccoe-ss
Using Kubernetes executor with image asia.gcr.io/krungthai-next-devops/poc/ccoe-mergeci-utility:7e615b6c ...
Using attach strategy to execute scripts...
Preparing environment
00:29
Waiting for pod ccoe-ss/runner-rrwzbrar-project-22429-concurrent-0lktmj to be running, status is Pending
	ContainersNotInitialized: \"containers with incomplete status: [init-permissions]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Waiting for pod ccoe-ss/runner-rrwzbrar-project-22429-concurrent-0lktmj to be running, status is Pending
	ContainersNotInitialized: \"containers with incomplete status: [init-permissions]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Waiting for pod ccoe-ss/runner-rrwzbrar-project-22429-concurrent-0lktmj to be running, status is Pending
	ContainersNotInitialized: \"containers with incomplete status: [init-permissions]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Waiting for pod ccoe-ss/runner-rrwzbrar-project-22429-concurrent-0lktmj to be running, status is Pending
	ContainersNotInitialized: \"containers with incomplete status: [init-permissions]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Waiting for pod ccoe-ss/runner-rrwzbrar-project-22429-concurrent-0lktmj to be running, status is Pending
	ContainersNotReady: \"containers with unready status: [build helper]\"
	ContainersNotReady: \"containers with unready status: [build helper]\"
Running on runner-rrwzbrar-project-22429-concurrent-0lktmj via ccoe-ss-gitlab-runner-84d9bcfbb6-hvs7n...
Getting source from Git repository
00:03
Fetching changes with git depth set to 50...
Initialized empty Git repository in /builds/cicd/kustomize/next/orchestrator-limit-profile-inquiry/.git/
Created fresh repository.
Checking out fd9a0b86 as refs/merge-requests/6/head...
Skipping Git submodules setup
Executing \"step_script\" stage of the job script
01:36
$ curl -LO https://github.com/yannh/kubeconform/releases/download/v${KUBE_CONFORM_VERSION}/kubeconform-linux-amd64.tar.gz && tar xf kubeconform-linux-amd64.tar.gz && chmod +x ./kubeconform && mv ./kubeconform /usr/local/bin/kubeconform
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 5604k  100 5604k    0     0  3771k      0  0:00:01  0:00:01 --:--:--  115M
$ git fetch --all
From https://gitdev.devops.krungthai.com/cicd/kustomize/next/orchestrator-limit-profile-inquiry
 * [new branch]      develop    -> origin/develop
 * [new branch]      main       -> origin/main
 * [new branch]      release    -> origin/release
$ git branch -r
  origin/develop
  origin/main
  origin/release
$ echo \"Preparing files for compare from target branch \'$CI_MERGE_REQUEST_TARGET_BRANCH_NAME\'\"
Preparing files for compare from target branch \'release\'
$ ls
LICENSE
README.md
base
kubeconform-linux-amd64.tar.gz
overlays
$ git checkout $CI_MERGE_REQUEST_TARGET_BRANCH_NAME
Previous HEAD position was fd9a0b8 Fix baseurl for dev
branch \'release\' set up to track \'origin/release\'.
Switched to a new branch \'release\'
$ mkdir temp
$ cp -R overlays temp
$ ls
LICENSE
README.md
base
kubeconform-linux-amd64.tar.gz
overlays
temp
$ ls temp
overlays
$ git checkout $CI_MERGE_REQUEST_SOURCE_BRANCH_NAME
branch \'develop\' set up to track \'origin/develop\'.
Switched to a new branch \'develop\'
$ echo \"Done ...\"
Done ...
$ echo \"Running Validation for base folder\"
Running Validation for base folder
$ if [[ \"$(git diff --name-only origin/$CI_MERGE_REQUEST_SOURCE_BRANCH_NAME origin/$CI_MERGE_REQUEST_TARGET_BRANCH_NAME -- base/ | wc -l)\" != \"0\" ]]; then # collapsed multi-line command
Base folder has been changed from develop to release. Please carefully review between Development and DevOps team.
$ echo \"Running Validation for .env configmap file\"
Running Validation for .env configmap file
$ ROOT_DIR=`pwd` # collapsed multi-line command
ConfigMap for overlays/aws-dev - ok
ConfigMap for overlays/aws-pfm - ok
ConfigMap for overlays/aws-prd - ok
ConfigMap for overlays/aws-sit - ok
ConfigMap for overlays/aws-stg - ok
ConfigMap for overlays/aws-uat - ok
ConfigMap for overlays/dev - ok
ConfigMap for overlays/pfm - ok
ConfigMap for overlays/prd - ok
ConfigMap for overlays/sit - ok
ConfigMap for overlays/stg - ok
ConfigMap for overlays/uat - ok
Validation for .env config file - done
$ echo \"Running Validation for .env secrets file\"
Running Validation for .env secrets file
$ ROOT_DIR=`pwd` # collapsed multi-line command
Secrets for overlays/aws-dev - ok
Secrets for overlays/aws-pfm - ok
Secrets for overlays/aws-prd - ok
Secrets for overlays/aws-sit - ok
Secrets for overlays/aws-stg - ok
Secrets for overlays/aws-uat - ok
Secrets for overlays/dev - ok
Secrets for overlays/pfm - ok
Secrets for overlays/prd - ok
Secrets for overlays/sit - ok
Secrets for overlays/stg - ok
Secrets for overlays/uat - ok
Validation for .env secrets file - done
$ echo \"Running Validation for set_resources file change.\"
Running Validation for set_resources file change.
$ ENV_OVERLAYS=$(ls overlays) # collapsed multi-line command
set_resources.yaml patch file for overlays aws-dev - ok
kustomization.yaml file for overlays aws-dev - ok
set_resources.yaml patch file for overlays aws-pfm - ok
--- temp_file1.yaml
+++ temp_file2.yaml
@@ -16,6 +16,9 @@
       kind: Deployment
 patchesStrategicMerge:
   - patches/set_resources.yaml
+replicas:
+  - count: 0
+    name: orchestrator-limit-profile-inquiry
 resources:
   - ../pfm
 secretGenerator:
Changes detected! 
The kustomization.yaml file in develop overlays aws-pfm does not match with release branch.
set_resources.yaml patch file for overlays aws-prd - ok
kustomization.yaml file for overlays aws-prd - ok
set_resources.yaml patch file for overlays aws-sit - ok
kustomization.yaml file for overlays aws-sit - ok
set_resources.yaml patch file for overlays aws-stg - ok
kustomization.yaml file for overlays aws-stg - ok
set_resources.yaml patch file for overlays aws-uat - ok
kustomization.yaml file for overlays aws-uat - ok
set_resources.yaml patch file for overlays dev - ok
kustomization.yaml file for overlays dev - ok
set_resources.yaml patch file for overlays pfm - ok
kustomization.yaml file for overlays pfm - ok
set_resources.yaml patch file for overlays prd - ok
kustomization.yaml file for overlays prd - ok
set_resources.yaml patch file for overlays sit - ok
kustomization.yaml file for overlays sit - ok
set_resources.yaml patch file for overlays stg - ok
kustomization.yaml file for overlays stg - ok
set_resources.yaml patch file for overlays uat - ok
kustomization.yaml file for overlays uat - ok
Error found. Please check the error message above.
$ set -e
$ echo \"Running Kube Validation\"
Running Kube Validation
$ mkdir kustomize-manifest # collapsed multi-line command
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
Checking kustomize for overlays/aws-dev...
kustomize for overlays/aws-dev - ok
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
Checking kustomize for overlays/aws-pfm...
kustomize for overlays/aws-pfm - ok
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
Checking kustomize for overlays/aws-prd...
kustomize for overlays/aws-prd - ok
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
Checking kustomize for overlays/aws-sit...
kustomize for overlays/aws-sit - ok
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
Checking kustomize for overlays/aws-stg...
kustomize for overlays/aws-stg - ok
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
Checking kustomize for overlays/aws-uat...
kustomize for overlays/aws-uat - ok
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
Checking kustomize for overlays/dev...
kustomize for overlays/dev - ok
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
Checking kustomize for overlays/pfm...
kustomize for overlays/pfm - ok
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
Checking kustomize for overlays/prd...
kustomize for overlays/prd - ok
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
Checking kustomize for overlays/sit...
kustomize for overlays/sit - ok
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
Checking kustomize for overlays/stg...
kustomize for overlays/stg - ok
# Warning: \'patchesStrategicMerge\' is deprecated. Please use \'patches\' instead. Run \'kustomize edit fix\' to update your Kustomization automatically.
Checking kustomize for overlays/uat...
kustomize for overlays/uat - ok
$ export CHECK_BASE # collapsed multi-line command
CHECK_BASE: FAIL
Please check content in 
base/configs/config.env
CHECK_CONFIGMAP: SUCCESS
CHECK_SET_RESOURCE_KUSTOMIZATION: FAIL
 The kustomization.yaml file in develop overlays aws-pfm does not match with release branch.
CHECK_SECRET: SUCCESS
CHECK_KUBE_VALIDATION: SUCCESS
Error found. Please check the error message above.
Cleaning up project directory and file based variables
00:01
ERROR: Job failed: command terminated with exit code 1
output: Potential Issues (Root Cause Analysis):
- The kustomization.yaml file in develop overlays aws-pfm does not match with release branch.

Potential Fix:
- Ensure that the kustomization.yaml file in develop overlays aws-pfm is in sync with the release branch.
- Make sure that any changes made to the kustomization.yaml file in develop overlays aws-pfm are also made to the release branch.
""",
    **parameters
)
print(f"Response from Model: {response.text}")