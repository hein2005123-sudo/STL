import os

def start_tool():
    print("Checking updates...")
    os.system('git pull --quiet')
    print("Starting Ruijie Voucher Generator...")
    import starlink

if __name__ == "__main__":
    start_tool()
    
