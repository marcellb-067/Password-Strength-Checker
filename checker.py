print("Welcome to the P@$$w0rd Strength Checker!")
print("-----------------------------------------------")

password = input("Please enter your password: ")

print("You entered:", password)

if len(password) >= 8:
    print("✓ Your Password is good enough (at least 8 characters long).")
else:
    print("✗ Your Password is too short (less than 8 characters).")

has_upper = False
has_lower = False
has_digit = False
has_special = False

symbols = "!@#$%^&*()_+-=[]{}/?<>.,;:'\"\\|`~"

for character in password:
    if character.isupper():
        has_upper = True
    elif character.islower():
        has_lower = True
    elif character.isdigit():
        has_digit = True
    elif character in symbols:
        has_special = True

if has_upper:
    print("✓ Contains uppercase letter.")
else: 
    print("✗ Missing uppercase letter.")

if has_lower:
    print("✓ Contains lowercase letter.")
else:
    print("✗ Missing lowercase letter.")

if has_digit:
    print("✓ Contains digit.")
else:
    print("✗ Missing digit.")

if has_special:
    print("✓ Contains symbols.")
else:
    print("✗ Missing symbols.")

common_passwords = []

try:
    with open ("common_passwords.txt", "r", encoding="utf-8", errors="ignore") as file:
              for line in file:
                  common_passwords.append(line.strip())
    print(f"[Loaded {len(common_passwords)} common passwords from common_passwords.txt]")
except FileNotFoundError:
    print("[WARNING: common_passwords.txt file not found. Skipping common password check.]")

if password.lower() in common_passwords:
    print ("✗ WARNING!! Your password is too common. Please choose a more unique password.")
    is_common = True
else:
    print ("✓ Your password is not a common password.")
    is_common = False

score = 0

if len(password) >= 8:
    score = score + 1
if len(password) >= 12:
    score = score + 1
if has_upper:
    score = score + 1
if has_lower:
    score = score + 1
if has_digit:
    score = score + 1
if has_special:
    score = score + 1
if is_common:
    score = 0

print()
print("-----------------------------------------------")
print("   FINAL PASSWORD STRENGTH SCORE   ")
print("-----------------------------------------------")
print(f"Password: {password}")
print(f"Score: {score} out of 6")

if score == 0:
    rating = "VERY WEAK - DO NOT USE "
elif score <= 2:
    rating = "WEAK - Consider improving your password."
elif score <= 4:
    rating = "MODERATE - Your password could be stronger."
elif score == 5:
    rating = "STRONG - Nice! Your password is strong."
else:
    rating = "VERY STRONG - Excellent! Your password is secured"

print(f"Rating: {rating}")
print("-----------------------------------------------")