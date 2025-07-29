import time
def start():
  import sys
  file_path = input("Please enter the full path to the email text file: ").strip()

  try:
        with open(file_path, 'r', encoding='utf-8') as file:
            email = file.read()
  except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
        return
  except Exception as e:
        print(f"An error occurred: {e}")
        return
  detect_phishing(email)
def detect_phishing(email):
    phishing_keywords = ["urgent", "click here", "verify", "login", "update", "password", "account", "limited time"]
    suspicious_links = ["http://", "https://", "bit.ly", "tinyurl", "ip address"]
    print("Checking The Email",end="",flush=True)
    for _ in range(4):
     time.sleep(0.5)
     print(".", end="", flush=True)
    print()
    
    score = 0

    for keyword in phishing_keywords:
        if keyword.lower() in email.lower():
            score += 1

    for link in suspicious_links:
        if link in email:
            score += 2

    if score >= 5:
        return "⚠️ This email looks like a phishing attempt!"
    elif score >= 3:
        return "❗ This email is suspicious. Be cautious."
    else:
        return "✅ This email seems safe."