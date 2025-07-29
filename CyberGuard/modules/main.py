from colorama import Style,Fore
from password_checker import password
from phishing import start
import pyttsx3,shutil,time
prog=pyttsx3.init()
def p1():
 width=shutil.get_terminal_size().columns
 print(Fore.CYAN, end="")
 for _ in range(width):
    print("*", end="", flush=True)
    time.sleep(0.001)
 print("Welcome To CyberGuard".center(width))
 prog.say("Welcome To CyberGuard")
 prog.runAndWait()
 print("Your Personal CyberSecurity ToolKit".center(width))
 prog.say("Your Personal CyberSecurity ToolKit")
 for _ in range(width):
    print("*", end="", flush=True)
    time.sleep(0.001)
 print(Style.RESET_ALL)
 prog.runAndWait()
 prog.say("Choose your desired security feature by entering its corresponding number from the list below")
 prog.runAndWait()
 print("1. Password Strength Check")
 k=input()
 if k=='1':
  password()
if __name__ == "__main__":
  p1()
  print(Style.RESET_ALL) 
  input("\nPress Enter to exit...")
