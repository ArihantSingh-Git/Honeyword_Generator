import random
import string
import csv
import os
from datetime import datetime

# =======================
# Banner
# =======================
def show_banner():
    print("=" * 60)
    print("   🔐 HONEYWORD INTRUSION DETECTION SYSTEM (H-IDS) 🔐")
    print("=" * 60)
    print("   Real-time detection | Logging | Security Monitoring")
    print("=" * 60)


# =======================
# CSV Logger Setup
# =======================
LOG_FILE = "alerts.csv"

def init_csv():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Event Type", "Entered Password"])


def log_event(event_type, password):
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), event_type, password])


# =======================
# Honeyword Generator
# =======================
def generate_honeywords(real_password, count=5):
    honeywords = set()
    honeywords.add(real_password)

    while len(honeywords) < count + 1:
        pw = list(real_password)

        operation = random.choice(['replace', 'add', 'swap'])

        if operation == 'replace' and len(pw) > 0:
            idx = random.randint(0, len(pw) - 1)
            pw[idx] = random.choice(string.ascii_letters + string.digits + "@#$%")

        elif operation == 'add':
            pw.append(random.choice(string.digits))

        elif operation == 'swap' and len(pw) > 1:
            i, j = random.sample(range(len(pw)), 2)
            pw[i], pw[j] = pw[j], pw[i]

        honeywords.add("".join(pw))

    return list(honeywords)


# =======================
# Real-Time Alert System
# =======================
def trigger_alert(message):
    print("\n" + "🚨" * 10)
    print(f"🚨 ALERT: {message}")
    print("🚨" * 10)


# =======================
# Login + Detection
# =======================
def check_login(real_password, honeywords):
    print("\n[ LOGIN MODULE ]")
    entered_password = input("Enter password to login: ")

    if entered_password == real_password:
        print("\n[ ✔ ] ACCESS GRANTED")
        log_event("SUCCESSFUL_LOGIN", entered_password)

    elif entered_password in honeywords:
        trigger_alert("HONEYWORD USED - POSSIBLE BREACH!")
        log_event("HONEYWORD_ALERT", entered_password)

    else:
        print("\n[ ✖ ] ACCESS DENIED")
        log_event("FAILED_LOGIN", entered_password)


# =======================
# Main Program
# =======================
def main():
    init_csv()
    show_banner()

    real_password = input("\nEnter your real password: ")
    count = int(input("Number of honeywords to generate: "))

    honeywords = generate_honeywords(real_password, count)

    print("\n[ GENERATED PASSWORD SET ]")
    for i, pw in enumerate(honeywords, 1):
        print(f"{i}. {pw}")

    print("\n[ INFO ] One of the above is the real password.")

    # Run login simulation
    check_login(real_password, honeywords)

    print("\n[ SYSTEM ] Logs saved in alerts.csv")


if __name__ == "__main__":
    main()