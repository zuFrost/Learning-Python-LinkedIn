
# def SetAnnual():
#   annual=10000
# def PrintMonthly():
#   print(" base Your monthly payment is "+annual/12+" USD.")
# SetAnnual()
# PrintMonthly()


# annual=0
# def SetAnnual():
#   annual=10000
# def PrintMonthly():
#   print("1 Your monthly payment is "+annual/12+" USD.")
# SetAnnual()
# PrintMonthly()


# annual=0
# def SetAnnual():
#   annual=10000
# def PrintMonthly():
#   print("2 Your monthly payment is "+str(annual/12)+" USD.")
# SetAnnual()
# PrintMonthly()


# annual=0
# def SetAnnual():
#   global annual=10000
# def PrintMonthly():
#   print("3 Your monthly payment is "+annual/12+" USD.")
# SetAnnual()
# PrintMonthly()


def SetAnnual():
  global annual
  annual=10000
def PrintMonthly():
  print("4 Your monthly payment is "+str(annual/12)+" USD.")
SetAnnual()
PrintMonthly()