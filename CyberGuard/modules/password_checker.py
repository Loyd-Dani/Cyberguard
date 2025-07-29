from colorama import Style,Fore
import time
import string
def password():
 while True:
  s=input("Enter The Password: ")
  print("Checking The Password",end="",flush=True)
  for _ in range(4):
   time.sleep(0.5)
   print(".", end="", flush=True)
  print()
  l=len(s)
  if  l<8:
   print(Fore.RED + "Password should be at least 8 characters long ❌")
  else:
   break
 upper = False
 lower = False
 digit = False
 special = False
 special_chars = "!@#$%^&*()-_+=<>?/"
 for char in s:
      if char.isupper():
          upper=True
      elif char.islower():
          lower=True
      elif char.isdigit():
          digit=True
      elif char in special_chars:
          special=True
 print("Done,Here Are The Results")
 print(f"Presence of Upper Case: {'✅' if upper else '❌'}")
 print(f"Presence of Lower Case: {'✅' if lower else '❌'}")
 print(f"Presence of Digits: {'✅' if digit else '❌'}")
 print(f"Presence of Special Characters: {'✅' if special else '❌'}")
 if upper and lower and digit and special:
     print(Fore.GREEN+"✅ It's a Strong Password")
 else:
        print(Fore.RED + "❌ It's a Weak Password")
