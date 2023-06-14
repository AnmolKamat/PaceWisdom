import traceback
import logging
import sqlite3
from datetime import date


# connection Function
def connection():
    try:
        conn = sqlite3.connect('python workshop/database.db')
        cursor = conn.cursor()
        return conn,cursor
    except Exception as e:
        print(e)


# create db
def createDatabase():
    conn , cursor = connection()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        password TEXT NOT NULL);
        """)    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activities (
        activity_id INTEGER PRIMARY KEY,
        activity_name TEXT NOT NULL);
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts (
        workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        activity_id INTEGER NOT NULL,
        date DATE NOT NULL,
        duration TIME NOT NULL,
        distance FLOAT,
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (activity_id) REFERENCES Activities(activity_id));
        """ )
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS measurements (
        measurement_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        date DATE NOT NULL,
        weight FLOAT,
        body_fat_percentage FLOAT,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
        ); 
        """ )

    conn.commit()
    conn.close()


# invalid choice
def invalidChoice():
    print("Invalid Choice")

def createUser(nme,pswd):
    conn , cursor = connection()
    cursor.execute("insert into users (name,password) values (?,?)",(nme,pswd))
    conn.commit()
    cursor.execute("SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1;")
    rows = cursor.fetchall() 
    print(f"user added Your User id is {rows[0][0]}")
    login()


# old user login
def userLogin(userId,pswd):
    conn , cursor = connection()
    cursor.execute("select * from users;")
    userTable = cursor.fetchall()
    userIdList = [ i[0] for i in userTable]
    if userId in userIdList:
        cursor.execute(f"select password from users where user_id = {userId}")
        actualPAssword = cursor.fetchall()[0][0]
        if actualPAssword == pswd:
            return 1
        else:
            return 2
    else:
        return 3


#View Workouts 
def viewWorkouts(userId):
    conn , cursor = connection()
    cursor.execute(f"""
                   select w.workout_id,a.activity_name,w.date,w.duration,w.distance
                   from workouts w, activities a 
                   where w.user_id={userId} 
                   and a.activity_id = w.activity_id;
                   """)
    rows = cursor.fetchall()
    if  len(rows)>0:
        count=1
        for i in rows:
            print(str(count),") ")
            print(f"workout id : {i[0]}")
            print(f"Activity  : {i[1]}")
            print(f"Date : {i[2]}")
            print(f"duration : {i[3]}")
            print(f"Distance  : {i[4]}\n")
            count+=1
    else:
        print("no workouts")
    mainMenu(userId)

def viewMeasurements(userId):
    conn , cursor = connection()
    cursor.execute(f"select * from measurements where user_id ={userId}")
    rows = cursor.fetchall()
    count = 1
    if  len(rows)>0:
        for i in rows:
            print(str(count),") ")
            print(f"Measurement ID : {i[0]}")
            print(f"Date : {i[2]}")
            print(f"Weight : {i[3]}")
            print(f"Body Fat : {i[4]}%\n")
            count+=1
    else:
        print("no Measurements")
    mainMenu(userId)

def updateMeasurement(userId,w,b,date):
    conn , cursor = connection()
    try:
        cursor.execute("insert into measurements(user_id,date,weight,body_fat_percentage) values(?,?,?,?)",(userId,date,w,b))
        conn.commit()
        print("\n Updated Measurement......!!!")

    except Exception as e:
        logging.error(str(e))
def addWorkout(userId,activity_id,date,duration,distance):
    conn,cursor = connection()
    try:
        cursor.execute("insert into workouts (user_id,activity_id,date,duration,distance) values(?,?,?,?,?)",(userId,activity_id,date,duration,distance))
        conn.commit()
        print("added Workout Details")
    except Exception as e:
        logging.error(str(e))


def mainMenu(userId):
    menu2 = {
    "1":"View Workouts",
    "2":"view measurements",
    "3":"update measurements",   
    "4":"add Workout",
    "5":"Logout",
    "6":"Exit"
    }
    for item, value in menu2.items():
        print(item+". "+ value)
    mainChoice = input("\n choose: ")
    if mainChoice == "1":
        viewWorkouts(userId)
        mainMenu(userId)
    elif mainChoice == "2":
        viewMeasurements(userId)
        mainMenu(userId)
    elif mainChoice == "3":
        weight = float(input("enter weight: "))
        bodyFat = float(input("enter Body fat % : "))
        meas_date = date.today()
        updateMeasurement(userId,weight,bodyFat,meas_date)
        mainMenu(userId)
    elif mainChoice == "4":
        activity_id = input("enter the Activity Performed (1.Running/2.cycling/3.WeightLifting/4.Swimming) : ")
        act_date = date.today()
        duration = input("enter duration: ")
        distance = input("enter distance(leave empty for Weightlifting) :")
        addWorkout(userId,activity_id,act_date,duration,distance)
        mainMenu(userId)
    elif mainChoice == "5":
       login()
    elif mainChoice == "7":
        exit(0)
    else:
        invalidChoice()
        mainMenu(userId)


# login
def login():
    menu1 = {
        "1":"new User",
        "2":"Old User"
        }

    try:
        for item, value in menu1.items():
            print(item+". "+ value)
        Choice = input("Choose:")
        if Choice not in menu1.keys():
            invalidChoice()
            login()
            
        elif Choice == "1":
            name = input("enter name: ")
            pswd = input("enter Password: ")
            createUser(name,pswd)
        else:
            userId = int(input("enter user id: "))
            pswd = input("enter Passsword: ")
            loginFlag = userLogin(userId,pswd)
            if loginFlag == 1:
                print("login Successfull \n ")
                mainMenu(userId)
            elif loginFlag == 2:
                print("invalid password try agin!!!")
                exit(0)
            else:
                print("user id is wrong try again")
                exit(0)
    except Exception as e:
        logging.error(str(e))

# main function
def main():
    try:
        createDatabase()
        login()
    except Exception as e:
        logging.error(str(e))
        logging.error(traceback.format_exc())



main()