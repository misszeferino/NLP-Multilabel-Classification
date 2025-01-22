import json
import requests  

def lambda_handler(event, context):
    # Log the incoming event
    print("Event received from GitHub:", json.dumps(event))

    # Extract the payload from the webhook
    try:
        body = json.loads(event['body'])  # Convert string to a dictionary
        text = body.get('text', '')  # Extract the 'text' field
        print(f"Extracted text: {text}")  # Log the extracted text
    except Exception as e:
        print(f"Error parsing event: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid request'),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS, POST',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }

    # Forward the payload to the EC2 instance
    try:
        print(f"Sending payload to EC2: {json.dumps({'text': text})}")
        ec2_response = requests.post(
            "http://50.16.143.79:8080/predict-tags",
            json={"text": text},
            timeout=10
        )
        ec2_response.raise_for_status()
        print(f"Response from EC2: {ec2_response.text}")
    except Exception as e:
        print(f"Error calling EC2 app: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error connecting to EC2'),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS, POST',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }

    # Return the EC2 response with CORS headers
    return {
        'statusCode': ec2_response.status_code,
        'body': ec2_response.text,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS, POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
    }
