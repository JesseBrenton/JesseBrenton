# CSC500 Module 3 Part 2: 24-hour alarm clock
# get current time
time=input("Enter current hour in 24-hour format: ")
hour=int(time)
# shortcut bad hour entry
if hour<1 or hour>24:
    print('Invalid hour')
    exit()
# get hours before alarm, and combine with type int
wait_hrs= input("Enter hours until alarm: ")
wait_hrs=int(wait_hrs)
# normalize hours over one day
while wait_hrs>24:
    wait_hrs=wait_hrs-24
alarm=wait_hrs+hour
# normalize alarm time over 24
while alarm>24:
    alarm=alarm-24
print("alarm will be set for hour ", alarm)

