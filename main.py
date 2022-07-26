# """
#  *****************************************************************************
#    FILE:        marathon.py
#
#    AUTHOR:      {Zoila-Lee Harris}
#
#    ASSIGNMENT: A marathon calculator to determine if a U.S. participant can
#    run in the Tokyo Marathon. 
#
#    DATE:         {06/15/2022}
#
#    DESCRIPTION: {Your Description Here}
#
#  *****************************************************************************

# $1 = 134.28¥
JAPANESE_YEN = 134.28

# 1 mi = 1609.34 meters
METERS_IN_MILE = 1609.34 

# Insert Code Below
def fitness():
  print("Tokyo Marathon Qualifer")
  name = input("Please into your name: ")
  pace = float(input("How many miles can you run in 10 minutes? "))
  marathon_money = float(input("How much U.S.$ do you have saved for the marathon? "))
  money_saved = JAPANESE_YEN * marathon_money
  print(money_saved)
  km_in_mi = METERS_IN_MILE/1000
  pace2 = (km_in_mi * pace)/ 10
  print(pace2)
  last_name_index = name.find(" ")
  last_name = name[last_name_index:]
  print(f"Dear {last_name}, you have a pace of {pace2}km/min.\nAdditionally, you only have {money_saved} to spent.")
    # This ignores our code so that we do not get an error Remove 'pass' when you want to start testing code.
    
# This invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    fitness()

