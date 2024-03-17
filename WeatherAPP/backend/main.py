# main.py
from fastapi import FastAPI, HTTPException
import sqlite3
import requests
from datetime import datetime

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Ensure database table exists
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
        city TEXT PRIMARY KEY,
        pressure INTEGER,
        current_time TEXT
    )''')
    conn.commit()
    conn.close()


@app.get("/2426803/api")
async def get_weather_for_warrington():
    # Fetch pressure data and current time from SQLite database for Warrington
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute("SELECT pressure, current_time FROM weather WHERE city=?", ('Warrington',))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Pressure data for Warrington not found")

    pressure, current_time = row
    return {"pressure": pressure, "current_time": current_time}