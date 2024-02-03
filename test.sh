#!/bin/bash

log_file_path='logfile.txt'
json_file='request.json'

# Function to read log file, convert to 1 line, and escape double quotes
process_log_file() {
    log_data=$(cat "$1" | tr '\n' '\\n' | sed 's/"/\\"/g')
    echo "$log_data"
}

# Your JSON data
json_data='{
    "contents": [
        {
            "role": "USER",
            "parts": {"text": "- This is logs from GitlabCI job\n- This job is for analyzing Kustomize repository and make sure it up to our company standard\n- This job is failing\nWith these context, I want you to analyze logs why this job is failing , what is the potential issues and what is potential fix that pipeline user can fix it themself\nNote that error should be in few latest row of logs not the start\nAnswer in this example format\nPotential Issues\n- There are no placeholder keys found in the overlay directory.\nPotential Fix\n- Verify that you have set the correct placeholder keys in the overlay directory for secrets like KAFKA_USERNAME, KAFKA_PASSWORD and WELFARE_EP_EKYC_ENCRYPTION_KEY, WELFARE_EP_EKYC_ENCRYPTION_IV, WELFARE_CID_ENCRYPTION_KEY, WELFARE_CID_ENCRYPTION_IV.\n- Make sure that the placeholder keys are valid and correspond to actual secret values stored in the secrets manager\n\nError Logs Start Below\n\n- This is logs from GitlabCI job \\- This job is for analyzing Kustomize repository and make sure it up to our company standard\\- This job is failing\\\\With these context, I want you to analyze logs why this job is failing , what is the potential issues and what is potential fix that pipeline user can fix it themself\\Note that error should be in few latest row, and we usually include human readable error in on why it failing leverage that for providing more understandable context for pipeline user\\\\Answer in this context\\- Potential Issues\\- Potential Fix\\- Relevant Logs (Get from input only , provide top 3 row of relevant logs)\n\nError Log Start Below\n\n"}
        }
    ],
    "generation_config": {
        "maxOutputTokens": 2048,
        "temperature": 0.9,
        "topP": 1
    }
}'

# Append log data to ["contents"][0]["parts"]["text"]
json_data=$(echo "$json_data" | jq --arg log "$(process_log_file "$log_file_path")" '.contents[0].parts.text += "\n\($log)"')

# Write the updated JSON to a file named request.json
echo "$json_data" | jq '.' > "$json_file"

# Print the updated JSON to the console
cat "$json_file"

API_ENDPOINT="asia-southeast1-aiplatform.googleapis.com"
PROJECT_ID="ccoe-lab"
MODEL_ID="gemini-pro"
LOCATION_ID="asia-southeast1"

response=$(curl -s \
    -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/${LOCATION_ID}/publishers/google/models/${MODEL_ID}:streamGenerateContent" \
    -d "@$json_file"
)

# Parse and print relevant information from the response
potential_issues=$(echo "$response" | jq -r '.[0].candidates[0].content.parts[0].text')
echo -e "\n$potential_issues"
