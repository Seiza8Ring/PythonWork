# Task 5: Free Throw Tracker
throws = int(input("How many free throws will you attempt? "))
shot = 'n'
score = 0
for i in range(throws):
    shot = input("Made the shot? (y/n): ").lower()
    if shot == 'y':
        score +=1
        print(f"Current score: {score}")
    else: print(f"Current score: {score}")

print(f"Final score: {score} out of {throws}")
