import requests
import time

# Base URL for GroupMe API
base_url = "https://api.groupme.com/v3"

# Bot ID
bot_id = "dfa96cfcb39b153744708185d5"

def send_message(message):
    """
    Sends a message to the GroupMe chat via the bot.
    
    Parameters:
        message (str): The text of the message to send.
    """
    # API endpoint for sending a message via bot
    post_url = f"{base_url}/bots/post"
    
    # Prepare the payload
    payload = {
        "bot_id": bot_id,
        "text": message
    }
    
    # Make the POST request to send the message
    response = requests.post(post_url, json=payload)
    
    # Check if the request was successful
    if response.status_code == 202:
        print(f"Message '{message}' sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Reason: {response.reason}")

# List of names to send
names = ["Hock", "Alesso", "Benju", "Majcher", "Sergio", "Pasha", "VH"]

# Loop through the list and send each name
for name in names:
    send_message(name)
    time.sleep(1)  # Optional: Adds a 1-second delay between each message to prevent rate-limiting
