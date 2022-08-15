print("Tip Calculator and Splitter!")

def plus_tip(check_total,tip_percent):
  return(check_total+(check_total*(tip_percent/100)))

def splitter(parts):
  return(plus_tip(check_total,tip_percent)/parts)

check_total = int(input("What is the Total?\t"))
tip_percent = int(input("What percent do you want to Tip?\t"))
parts = int(input("How many ways would you like to split?\t"))
print("Total + Tip - ")
print("$ "+str(plus_tip(check_total,tip_percent)))
print("Individual Total - ")
print("$ "+str(splitter(parts)))