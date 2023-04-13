import json
from json import JSONDecodeError
import random
import string
# Register:
"""
[{
    "name": "Krishna",
    "user_id": 123,
    "password": "password",
    "age": 24,
    "mail_id": "abc@gmail.com",
    "phone": 1234567890,
    "location": "India",
    "booked_shows": []
},{},{},...]
"""
def register(user_json, user_id, name, password, age, mail_id, phone, location):
    """
    Register the user based on the param values provided.
    
    return value:
        it returns true on successful registration
        it returns false on unsuccessful registration
    """
    d = {
        "user_id": user_id,
        "name": name,
        "password": password,
        "age": age,
        "mail id": mail_id,
        "phone": phone,
        "location": location,
        "booked shows": []
    }
    f = open(user_json, "r+")
    try:
        content = json.load(f)
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content, f)
            f.close()
            return True
    except JSONDecodeError as err:
        l = []
        l.append(d)
        json.dump(l, f)
        return True
    f.close()
    return False

# Add show
"""
[{
"movie_id": "12548",
"movie_name": "Taare Zameen Par",
"seating": "25",
"price": "25$",
"booked_seats": []
}]

Seating arrangement:
  A  B  C  D  E
1 A1 B1 C1 D1 E1
2 A2 B2 C2 D2 E2
3 A3 B3 C3 D3 E3
4 A4 B4 C4 D4 E4
5 A5 B5 C5 D5 E5
"""
def add_show(show_json, show_id, show_name, duration, price):
    """
    adding the show unit
    
    return values:
        return True if show unit was added
        return False if show unit already existed
    """
    d1 = {
        "movie id": show_id,
        "movie name": show_name,
        "seating": 25,
        "price": price,
        "booked_seats": []
    }
    f = open(show_json, "r+")
    try:
        content = json.load(f)
        if d1 in content:
            print("Show already available!!")
            return False
        content.append(d1)
        f.seek(0)
        f.truncate()
        json.dump(content, f)
    except JSONDecodeError:
        l = []
        l.append(d1)
        json.dump(l, f)
    f.close()
    return True

def book_ticket(show_json, user_json, usr_id, tkt_id, no_of_booking, preferred_seat = []):
    """
    [{
    "movie_id": "123548",
    "movie name": "interstellar",
    }]
    """
    number_of_seat = 25
    # open the user json
    f1 = open(user_json, "r+")
    content1 = json.load(f1)
    count = 0
    for i in range(len(content1)):
        if content1[i]["user_id"] == usr_id:
            user = content1[i]
            count+=1
    if count == 0:
        return False
    
    # open the show json
    f = open(show_json, "r+")
    content = json.load(f)
    count = 0
    for i in range(len(content)):
        if content[i]["movie id"] == tkt_id:
            movie_show = content[i]
            seat_av = len(movie_show["booked_seats"])
            number_of_seat = 25 - seat_av
            count+=1
    if count == 0:
        return False
    if number_of_seat == 0:
        print("House Full!!")
        return False
    
    #   A  B  C  D  E
    # 1 A1 B1 C1 D1 E1
    # 2 A2 B2 C2 D2 E2
    # 3 A3 B3 C3 D3 E3
    # 4 A4 B4 C4 D4 E4
    # 5 A5 B5 C5 D5 E5
    
    # Recollect the available seats
    seats = []
    for col in range(1, 6):
        for row in range(ord("A"), ord("E")+1):
            if chr(row)+str(col) not in movie_show["booked_seats"]:
                seats.append(chr(row)+str(col))
    # Booking Process
    if number_of_seat >= no_of_booking:
        for i in preferred_seat:
            if i not in seats:
                return False
        if preferred_seat:
            movie_show["booked_seats"].extend(preferred_seat)
            user["booked shows"].append(tkt_id)
        else:
            movie_show["booked_seats"].extend(seats[:no_of_booking])
            user["booked shows"].append(tkt_id)
    else:
        return False
    
    # update the values in user_json
    for i in range(len(content1)):
        if content1[i]["user_id"] ==usr_id:
            content1[i]["booked shows"] = user["booked shows"]
            f1.seek(0)
            f1.truncate()
            json.dump(content1, f1)
            f1.close()
    
    # update the value for the show_json
    for i in range(len(content)):
        if content[i]["movie id"] == tkt_id:
            content[i]["booked_seats"] = movie_show["booked_seats"]
            f.seek(0)
            f.truncate()
            json.dump(content, f)
            f.close()
    return True

def show_seats(show_json, tkt_id):
    """
    this function will show the available seats to user
    """
    f = open(show_json, "r+")
    content = json.load(f)
    count = 0
    for i in range(len(content)):
        if content[i]["movie id"] == tkt_id:
            movie_show = content[i]
            seat_av = len(movie_show["booked_seats"])
            number_of_seat = 25 - seat_av
            count+=1
    if count == 0:
        return False
    
    for col in range(1,6):
        for row in range(ord("A"), ord("E")+1):
            if chr(row)+str(col) not in movie_show["booked_seats"]:
                print(chr(row)+str(col), end=" ")
            else:
                print("B", end="  ")
        print()
    f.close()

def login(user_json, user_id, password):
    """
    Login Process 
    """
    f = open(user_json, "r+")
    try:
        content=json.load(f)
    except JSONDecodeError:
        return False
    f.close()
    d = 0
    for i in range(len(content)):
        if content[i]["mail id"] == user_id and content[i]["password"] == password:
            d = 1
            break
    if d == 1:
        return True
    else:
        return False
enter = True
while enter:
    print("Menu: ")
    print("1) Login:")
    print("2) Sign up:")
    print("3) Quit:))")
    val = input("Enter you choice: ")
    if val == "3":
        print("See you around!")
        break
    elif val == "1":
        email = input("Enter you email address")
        pswd = input("Enter you password")
        loginstatus = True#login("user.json", email, pswd)
        if loginstatus == False:
            print("Invalid Credentials!!")
            break
        print("Heyy Logged in!!")
        while loginstatus:
            # activities
            print("Menu: ")
            print("1) Book ticket")
            print("2) show booked ticket history")
            print("3) Show Seats Available!!")
            print("4) Logout")
            val = input("Enter your choice: ")
            if val == "4":
                print("Logging out!!!")
                break
            elif val == "1":
                #book_ticket(show_json, user_json, usr_id, tkt_id, no_of_booking, preferred_seat = [])
                user_id = input("Enter your user ID: ")
                tkt_id = input("Enter movie ID: ")
                no_of_booking = int(input("Enter the number of booking you want: "))
                if_seat = input("Do you have any preferred Seat! y/n")
                prfd_seat = []
                if if_seat == "y":
                    prfd_seat = input("Enter your preferred seat number with comma seperated").split(",")
#                     for i in range(no_of_booking):
#                         s = input("Enter your preferred seat number")
                book_ticket("movie.json", "user.json", tkt_id, no_of_booking, prfd_seat)
                print("Ticket Booked!!")
            elif val == "2":
                print("Show ticket history!!")
            elif val == "3":
                tkt_id = input("Enter the ticket id")
                show_seats("movie.json", tkt_id)
            else:
                print("Enter valid option between 1-3")
    elif val == "2":
        print("Registering in progress!!") #user_json, user_id, name, password, age, mail_id, phone, location
        name = input("Enter your Name!!")
        password = input("Enter your Password!!")
        phn = input("Enter your Phone Number!!")
        age = input("Enter your age!!")
        mail_id = input("Enter your email address!!")
        location = input("Enter your Location!!")
        user_id = name+''.join(random.choices(string.ascii_lowercase+string.digits, k=4))
        register("user.json", user_id, name, password, age, mail_id, phn, location)
    else:
        print("Wrong Input!!\nEnter valid option between 1-3")