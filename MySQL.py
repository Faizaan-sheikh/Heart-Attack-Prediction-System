import mysql.connector
from tkinter import messagebox

def Save_Data_MySql(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R):
    try:
        mydb = mysql.connector.connect(host='localhost', user='root', password='78789898', database='Heart_Data')
        mycursor = mydb.cursor()
        print("Connection established")

        # Insert data into the data table
        command = "INSERT INTO data(Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, Result) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R)
        mycursor.execute(command, values)

        # Commit changes and close connection
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Register", "New User added successfully!")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")

# Example usage of Save_Data_MySql function
Save_Data_MySql("sheela", "31/05/2024", "2001", "44", "2", "1", '233', '233', '0', '1', '233', '1', '1.0', '0', '2', '1', '0')
