import requests
import json
from bs4 import BeautifulSoup
import re
import random
import string
import time
from dotenv import load_dotenv
from os import getenv

load_dotenv()

DOMAIN = getenv("DOMAIN")
KEY = getenv("KEY")
MAILDROP_API_URL = F"https://api.{DOMAIN}/graphql"
HEADERS = {"Content-Type": "application/json"}

def generate_random_username(length=20):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def extract_verification_code(html):
    soup = BeautifulSoup(html, "html.parser")
    for b_tag in soup.find_all("b"):
        text = b_tag.get_text(strip=True)
        if re.fullmatch(r"\d+", text):
            return text
    return None

def get_inbox(mailbox):
    query = f"""
    query {{
        inbox(mailbox: "{mailbox}") {{
            id
            headerfrom
            subject
            date
        }}
    }}
    """
    data = {"query": query}
    response = requests.post(MAILDROP_API_URL, headers=HEADERS, data=json.dumps(data))
    response.raise_for_status()
    return response.json()["data"]["inbox"]

def get_message(mailbox, message_id):
    query = f"""
    query {{
        message(mailbox: "{mailbox}", id: "{message_id}") {{
            id
            headerfrom
            subject
            date
            html
        }}
    }}
    """
    data = {"query": query}
    response = requests.post(MAILDROP_API_URL, headers=HEADERS, data=json.dumps(data))
    response.raise_for_status()
    return response.json()["data"]["message"]

def get_latest_message(mailbox):
    inbox = get_inbox(mailbox)
    if not inbox:
        return None
    latest_message = inbox[0]
    return get_message(mailbox, latest_message["id"])

async def get_username():
    return f"{generate_random_username()}@{DOMAIN}"

async def get_verification_code(mailbox):
    verification_code = None
    for _ in range(10):
        message = get_latest_message(mailbox)
        if message:
            verification_code = extract_verification_code(message.get("html", ""))
            if verification_code:
                break
        time.sleep(3)
    return verification_code