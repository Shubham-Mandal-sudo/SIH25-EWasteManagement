from inference_sdk import InferenceHTTPClient

# Initialize client
CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="x2P8cdyvpvNtakN5oHZC"   # paste your Roboflow API key
)

# Run inference on an image
result = CLIENT.infer(
    "WhatsApp Image 2025-08-22 at 10.49.53_c416c0b0.jpg",   # replace with the path to your local image
    model_id="e-waste-dataset-r0ojc/43"  # model name and version
)

print(result)