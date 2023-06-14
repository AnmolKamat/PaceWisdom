import traceback
import logging
from pymongo import MongoClient
from datetime import date

def invalidChoice():
    print("invalid choice")

# Connection Function
def connection():
    try:
        client = MongoClient('mongodb+srv://AnmolKamath:7892539801@cluster0.gjgpfjd.mongodb.net/?retryWrites=true')
        db = client['python_workshop']
        return db
    except Exception as e:
        print(e)


# Create collections
def createCollections():
    db = connection()
    db.users.create_index("user_id", unique=True)


# Create user
def createUser(name, password):
    db = connection()
    userId = db.users.count_documents({})+1
    user = {
        "user_id":userId,
        "name": name,
        "password": password
    }
    
    result = db.users.insert_one(user)
    print(f"User added. Your User id is {userId}")
    login()


# User login
def userLogin(user_id, password):
    db = connection()
    user = db.users.find_one({"user_id": user_id})
    if user:
        if user["password"] == password:
            return 1
        else:
            return 2
    else:
        return 3


# View workouts
def viewWorkouts(user_id):
    db = connection()
    workouts = db.workouts.find({"user_id": user_id})
    if db.workouts.count_documents({"user_id": user_id})>0:
        for workout in workouts:
            activity = db.activities.find_one({"number":int(workout['activity_id'])},{"name":1,"_id":0})["name"]
            print(f"Workout id: {workout['_id']}")
            print(f"Activity : {activity}")
            print(f"Date: {workout['date']}")
            print(f"Duration: {workout['duration']}")
            print(f"Distance: {workout['distance']}\n")
    else:
        print("No workouts")
    mainMenu(user_id)


# View measurements
def viewMeasurements(user_id):
    db = connection()
    measurements = db.measurements.find({"user_id": user_id})
    if db.measurements.count_documents({"user_id": user_id})>0:
        for measurement in measurements:
            print(f"Measurement ID: {measurement['_id']}")
            print(f"Date: {measurement['date']}")
            print(f"Weight: {measurement['weight']}")
            print(f"Body Fat: {measurement['body_fat_percentage']}%\n")
    else:
        print("No measurements")
    mainMenu(user_id)


# Update measurement
def updateMeasurement(user_id, weight, body_fat_percentage, date):
    db = connection()
    measurement = {
        "user_id": user_id,
        "date": date,
        "weight": weight,
        "body_fat_percentage": body_fat_percentage
    }
    db.measurements.insert_one(measurement)
    print("\nUpdated Measurement...!!!")
    mainMenu(user_id)


# Add workout
def addWorkout(user_id, activity_id, date, duration, distance):
    db = connection()
    workout = {
        "user_id": user_id,
        "activity_id": activity_id,
        "date": date,
        "duration": duration,
        "distance": distance
    }
    db.workouts.insert_one(workout)

    print("Added Workout Details")
    mainMenu(user_id)


# Main menu
def mainMenu(user_id):
    menu = {
        "1": "View Workouts",
        "2": "View Measurements",
        "3": "Update Measurements",
        "4": "Add Workout",
        "5": "Logout",
        "6": "Exit"
    }
    for item, value in menu.items():
        print(item + ". " + value)
    mainChoice = input("\nChoose: ")
    if mainChoice == "1":
        viewWorkouts(user_id)
    elif mainChoice == "2":
        viewMeasurements(user_id)
    elif mainChoice == "3":
        weight = float(input("Enter weight: "))
        bodyFat = float(input("Enter Body fat %: "))
        meas_date = date.today().isoformat()
        updateMeasurement(user_id, weight, bodyFat, meas_date)
    elif mainChoice == "4":
        activity_id = input("Enter the Activity Performed (1.Running/2.Cycling/3.Weightlifting/4.Swimming): ")
        act_date = date.today().isoformat()
        duration = input("Enter duration: ")
        distance = input("Enter distance (leave empty for Weightlifting): ")
        addWorkout(user_id, activity_id, act_date, duration, distance)
    elif mainChoice == "5":
        login()
    elif mainChoice == "6":
        exit(0)
    else:
        invalidChoice()
        mainMenu(user_id)


# Login
def login():
    menu = {
        "1": "New User",
        "2": "Old User"
    }

    try:
        for item, value in menu.items():
            print(item + ". " + value)
        choice = input("Choose: ")
        if choice not in menu.keys():
            invalidChoice()
            login()
        elif choice == "1":
            name = input("Enter name: ")
            password = input("Enter password: ")
            createUser(name, password)
        else:
            user_id = int(input("Enter user id: "))
            password = input("Enter password: ")
            loginFlag = userLogin(user_id, password)
            if loginFlag == 1:
                print("Login successful\n")
                mainMenu(user_id)
            elif loginFlag == 2:
                print("Invalid password. Try again!!!")
                exit(0)
            else:
                print("User id is wrong. Try again")
                exit(0)
    except Exception as e:
        logging.error(str(e))


# Main function
def main():
    try:
        createCollections()
        login()
    except Exception as e:
        logging.error(str(e))
        logging.error(traceback.format_exc())


main()
