#Exercise 01 Created by Zide Yang Feb 11,2013
def check_fermat (a,b,c,n):
    """checks to see if Fermats theorem holds. If n is greater than 2 and 
    the program should print: “Holy smokes, Fermat was wrong!”
    Otherwise the program should print:> “No, that doesnt work.”"""
    if n>2 and (a**n+b**n)==c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn\'t work.")
#Ex102
def check():
  """prompts the user to input values 
  for a, b, c and n, converts them to integers
  and uses check_fermat to check whether they violate Fermat theorem."""
  a=int(input("please enter a value for a"))
  b=int(input("please enter a value for b"))
  c=int(input("please enter a value for c"))
  n=int(input("please enter a value for n"))    
  check_fermat(a,b,c,n)
  

check()

