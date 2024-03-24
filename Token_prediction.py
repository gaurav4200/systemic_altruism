import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

# Initialize Selenium WebDriver
driver = webdriver.Chrome()

def extract_wallet_addresses(token_url):
    driver.get(token_url)
    time.sleep(5)  # Allowing time for the page to load
    wallet_elements = driver.find_elements_by_class_name("wallet-address")
    wallet_addresses = [element.text for element in wallet_elements]
    return wallet_addresses

# Function to check if a wallet address is new
def is_new_wallet(wallet_address):
    return True

# Function to notify via Telegram
def send_telegram_notification(message):
    bot_token = 'YOUR_BOT_TOKEN'
    chat_id = 'YOUR_CHAT_ID'
    telegram_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    response = requests.get(telegram_api_url, params=params)
    return response.json()

# Main function
def main():
    token_url = 'https://dextools.io/app/solana/pair-explorer/0x965f5d86431436e25e5746196034d1877cd4d5af'
    wallet_addresses = extract_wallet_addresses(token_url)
    for wallet_address in wallet_addresses:
        if is_new_wallet(wallet_address):
            message = f"New potential big buyer detected! Wallet Address: {wallet_address}"
            send_telegram_notification(message)

# Run the main function
if __name__ == "__main__":
    main()
