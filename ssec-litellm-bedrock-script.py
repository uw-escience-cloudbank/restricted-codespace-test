import openai
import os
import base64

client = openai.OpenAI(
    api_key=os.environ.get("ANTHROPIC_AUTH_TOKEN"),
	base_url=os.environ.get("ANTHROPIC_BASE_URL")
)

# Helper function to encode images to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Example with text only
response = client.chat.completions.create(
    model="cloudbank-claude-haiku-4-5",
    messages=[
    {
        "role": "user",
        "content": "write me a haiku about my spunky grey cat PJ"
    },
    {
        "role": "assistant",
        "content": "# PJ\n\nSilver whiskers twitch—\ngrey pounce, fearless and nimble,\nspunk in soft fur coiled"
    }
]
)

print(response)

# Example with image or PDF (uncomment and provide file path to use)
# base64_file = encode_image("path/to/your/file.jpg")  # or .pdf
# response_with_file = client.chat.completions.create(
#     model="cloudbank-claude-haiku-4-5",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "Your prompt here"
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{base64_file}"  # or data:application/pdf;base64,{base64_file}
#                     }
#                 }
#             ]
#         }
#     ]
# )
# print(response_with_file)

