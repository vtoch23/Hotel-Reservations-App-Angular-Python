from fastapi import FastAPI, Form
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import json


app = FastAPI()


conn = mysql.connector.connect(
    host = "localhost",
    database = "hotel_db",
    user = "root",
    password = "123456789"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:4200", 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def get_reservations():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select * from guests")
    records = cursor.fetchall()
    return records


@app.post('/add_reservation')
def add_reservation(guestName: str =  Form(), guestEmail: str = Form(), checkInDate: str = Form(), checkOutDate: str = Form(), roomNumber: int = Form(), icon: str = Form(),):
    cursor = conn.cursor(dictionary=True)
    checkInDate = json.loads(checkInDate)
    checkOutDate = json.loads(checkOutDate)
    roomNumber = str(roomNumber)
    cursor.execute("insert into guests (guestName, guestEmail, checkInDate, checkOutDate, roomNumber, icon) values (%s, %s, %s, %s, %s, %s)", 
        (guestName, guestEmail, checkInDate, checkOutDate,  roomNumber, icon))
    conn.commit()
    records = cursor.fetchall()
    return "added"

@app.get('/get_reservation/{id}')
def get_reservation(id):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select * from guests where id=%s", (id, ))
    record = cursor.fetchone()
    return record

@app.put('/update_reservation/{id}')
def update_reservation(id, guestName: str =  Form(), guestEmail: str = Form(), checkInDate: str = Form(), checkOutDate: str = Form(), roomNumber: int = Form(), icon: str = Form(),):
    cursor = conn.cursor(dictionary=True)
    checkInDate =  json.loads(checkInDate)
    checkOutDate = json.loads(checkOutDate)
    roomNumber = int(roomNumber)
    cursor.execute("""UPDATE guests SET guestName=%s, guestEmail=%s, checkInDate=%s, checkOutDate=%s, roomNumber=%s, icon=%s WHERE id=%s """, (guestName, guestEmail, checkInDate, checkOutDate, roomNumber, icon, id))
    conn.commit()
    return "updated"

@app.delete("/delete_reservation/{id}")
def delete_reservation(id):
    cursor = conn.cursor()
    cursor.execute("delete from guests where id=%s", (id, ))
    conn.commit()
    return "Reservation Deleted Successfully"
