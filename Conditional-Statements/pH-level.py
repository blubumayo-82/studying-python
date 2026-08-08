# This is to know if the inputted pH level is Basic, Acidic, or Neutral.
ph = int(input("Input the pH level of the liquid (0-14): "))

if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")
