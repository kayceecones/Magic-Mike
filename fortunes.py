import random 

from fortune_list import FORTUNES_LIST

def get_random_fortune(fortunes): 
  return random.choice(fortunes)

def magic_8_ball():
  print("welcome weary traveller... we have been waiting for you.") 

def main():
  input("To recieve your truth, you must share one first. Tell us, what is your deepest truth?")
  fortune = get_random_fortune(FORTUNES_LIST) 
  print(f"I can see it clearly... your future is bright, but it hinges on this moment. Here is what your future self needs you to know now: {fortune}")


if __name__ == '__main__':
  main()