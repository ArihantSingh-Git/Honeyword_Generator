import random
import string

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


def check_login(real_password, honeywords):
    print("\n=== Login Simulation ===")
    entered_password = input("Enter password to login: ")

    if entered_password == real_password:
        print("✅ Correct password entered. Access granted.")
    elif entered_password in honeywords:
        print("⚠️ ALERT! Honeyword used. Possible unauthorized access detected!")
    else:
        print("❌ Incorrect password.")


def main():
    print("\n=== Honeyword Generator ===")

    real_password = input("Enter your real password: ")
    count = int(input("How many honeywords to generate? "))

    honeywords = generate_honeywords(real_password, count)

    print("\nGenerated Password List:")
    for i, pw in enumerate(honeywords, 1):
        print(f"{i}. {pw}")

    print("\n(Note: One of these is your real password, others are decoys.)")

    # Login check
    check_login(real_password, honeywords)


if __name__ == "__main__":
    main()