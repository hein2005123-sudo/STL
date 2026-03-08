import hashlib

def generate_ruijie_codes(mac_addr):
    clean_mac = mac_addr.replace(":", "").replace("-", "").lower()
    results = []
    for i in range(1, 7):
        seed = f"{clean_mac}{i}"
        hash_obj = hashlib.sha256(seed.encode())
        full_hash = int(hash_obj.hexdigest(), 16)
        voucher = str(full_hash)[-6:]
        results.append(voucher)
    return results

if __name__ == "__main__":
    mac = input("Enter Router MAC: ")
    codes = generate_ruijie_codes(mac)
    print("\nGenerated Voucher Codes:")
    for i, code in enumerate(codes, 1):
        print(f"Voucher {i}: {code}")
        
