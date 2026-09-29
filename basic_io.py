user_name=input("input your name: ")
user_age=int(input("input your age: "))
fav_num=int(input("input your fav number: "))
new_age=user_age+10 # user age after 10 years
sqr_fav_num=int(fav_num**(1/2)) # the square of fav number
if sqr_fav_num % 2==0:
    type_fav_num="even"
else:
    type_fav_num="odd"
print(f" Hi {user_name}! In 10 years you'll be {new_age}. Your favorite number squared is {sqr_fav_num}, and it's {type_fav_num}.")

#Question
# Why does input() always  return a string, and why is type casting necessary before doing math with it?
#Answer
# Python accepts the inputs as a text (it doesn't know the type of inputs), that's whay it always returns a string .
# When it comes to the neccessity of type casting, the commands related to math can function only with the type  of int,float,etc. not string.

