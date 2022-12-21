from time import *
import random as r


def mistake(partest,usertest):
      error=0
      for i in range(len(partest)):
            try:
                  if partest[i]!=usertest[i]:
                        error+=1
            except:
                  error+=1;
      return error

def speed_time(time_s,time_e,userinput):
      time_delay = time_e-time_s
      time_round=round(time_delay,2)
      speed=len(userinput*60)/(5*time_round)
      return round(speed)

test=["Income before securities transactions was up 10.8 percent from $13.49 million in 1982 to $14.95 million in 1983. Earnings per share (adjusted for a 10.5 percent stock dividend distributed on August 26) advanced 10 percent to $2.39 in 1983 from $2.17 in 1982. Earnings may rise for 7 years. Hopefully, earnings per share will grow another 10 percent. Kosy, Klemin, and Bille began selling on May 23, 1964. Their second store was founded in Renton on August 3, 1965. From 1964 to 1984, they opened more than 50 stores through-out the country. As they expanded, 12 regional offices had to be organized.",
      "Each of these 12 regional offices had to be organized. Each of these 12 regions employs from 108 to 578 people. National headquarters employs 1,077 people. Carole owns 118 stores located in 75 cities ranging as far west as Seattle and as far east as Boston. She owns 46 stores south of the Mason-Dixon line and 24 stores north of Denver. Carole buys goods from 89 companies located in 123 countries and all 50 states. Carole started in business on March 3, 1975. She had less than $6,000 in capital assets.",
      "One study examining 30 subjects, of varying different styles and expertise, has found minimal difference in typing speed between touch typists and self-taught hybrid typists. According to the study",
      "The number of fingers does not determine typing speed... People using self-taught typing strategies were found to be as fast as trained typists... instead of the number of fingers, there are other factors that predict typing speed",
      "December 17, 1903, is the birth date of all airplanes. Orville and Wilbur Wright started building gliders in 1900. In 1903, they built a motor and propeller for their glider. Orville made the first flight, which lasted 12 seconds, and flew 120 feet. Wilbur's flight was 852 feet in 59 seconds. These first flights in 1903 were just the start of the evolution of planes. By the year 1909, Bleriot had crossed the English Channel.",
      "By the year 1912, a two-piece plywood fuselage was built for greater strength. By the 1930s, the all-metal fuselage was tried, and it soon appeared in DC3s. From the Wrights' 1903 motor and prop came the engines for the 1950 turbojet that generated at least 19,600 pounds of thrust. The big Boeing 747 has four engines with 50,000 pounds of thrust each. The future holds an advanced super-sonic jet with a saving of almost 40 percent in fuel usage.",

      " Their second store was founded in Renton on August 3, 1965.From 1964 to 1984, they opened more than 50 stores through-out the country."]

test1 = r.choice(test)
print("    ****** Typing speed calculator ******   ")
print(test1)
print()
print()
time_1=time()
testinput=input("Enter: ")
time_2=time()

print("Speed : ", speed_time(time_1,time_2,testinput),"words/min")
print("Accuracy :", round(((len(test1)-mistake(test1,testinput))/len(testinput))*100),"%")



