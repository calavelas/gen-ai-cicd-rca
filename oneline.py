import json

# Function to read log file, convert to 1 line, and escape double quotes
def process_log_file(log_file_path):
    with open(log_file_path, 'r') as file:
        # Read the log file and replace newline characters with '\n'
        log_data = file.read().replace('\n', '\\n')

        # Escape double quotes
        log_data = log_data.replace('"', '\\"')

        return log_data

# Your JSON data
json_data = {
    "contents": [
        {
            "role": "USER",
            "parts": {"text": "- This is logs from GitlabCI job\n- This job is for analyzing Kustomize repository and make sure it up to our company standard\n- This job is failing\nWith these context, I want you to analyze logs why this job is failing , what is the potential issues and what is potential fix that pipeline user can fix it themself\nNote that error should be in few latest row of logs not the start\nAnswer in this example format\nPotential Issues\n- There are no placeholder keys found in the overlay directory.\nPotential Fix\n- Verify that you have set the correct placeholder keys in the overlay directory for secrets like KAFKA_USERNAME, KAFKA_PASSWORD and WELFARE_EP_EKYC_ENCRYPTION_KEY, WELFARE_EP_EKYC_ENCRYPTION_IV, WELFARE_CID_ENCRYPTION_KEY, WELFARE_CID_ENCRYPTION_IV.\n- Make sure that the placeholder keys are valid and correspond to actual secret values stored in the secrets manager\n\nError Logs Start Below\n"}
        }
    ],
    "generation_config": {
        "maxOutputTokens": 2048,
        "temperature": 0.9,
        "topP": 1
    }
}

# Specify the path to your log file
log_file_path = 'logfile.txt'

# Append log data to ["contents"][1]["parts"]["text"]
json_data["contents"][0]["parts"]["text"] += '\n' + process_log_file(log_file_path)

# Write the updated JSON to a file named request.json
with open('request.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)
