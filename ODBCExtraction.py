'''
Version:      1.1
date:         17 Oct 2023
filename:     ODBCExtraction.py
created by:   Kaustav Purakayastha - kaustav.purakayastha@pwc.com
purpose:      This file will extract data from a Sage 50 ODBC connection into tables that 
              can be ingested by DMS.
Next Steps:
1) Write code for creating ODBC connection directly by chosing the data folder 
2) Create a TB file.

'''
import pyodbc
import csv
import time
import customtkinter
import datetime
import os
from tkinter import messagebox
# import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("650x350")
root.iconbitmap(default="icon.ico")
root.title("Sage 50 (UK) ODBC Extractor System")


def Execute():
    # DSNVariable = entry1.get()#comment this to avoid putting in password
    # userName = entry2.get()
    # passWord = entry3.get()

    # DSNVariable = "SMHTGolive" #remove comments to avoid putting in password
    # userName = "Manager"
    # passWord = "dog4you"
    DSNVariable = "OIEGSHKuat2" #remove comments to avoid putting in password
    userName = "manager"
    passWord = "Grosvenor21"
    # DSNVariable = "DemoData231006" #remove comments to avoid putting in password
    # userName = "Manager"
    # passWord = ""

    odbc_connection_string = "DSN="+ DSNVariable + ";UID=" + userName + ";PWD=" + passWord
    sageTables = ["NOMINAL_LEDGER","BANK","PURCHASE_LEDGER","PURCHASE_ORDER","SALES_LEDGER","SALES_ORDER","STOCK","STOCK_TRAN","PROJECT","PROJECT_TRAN","AUDIT_HEADER","AUDIT_JOURNAL"]

    try:
        # Establish the ODBC connection
        connection = pyodbc.connect(odbc_connection_string)
        tableCounter = 0
        timer = 0
        summaryFileName = DSNVariable+"-"+"ExtractionSummary.txt"
        fileToDelete = open(summaryFileName,'w') #these two line clears the data in the summary file.
        fileToDelete.close()
        messagebox.showinfo("Connected","Executing! Please press OK and wait for confimation...")
        # label  = customtkinter.CTkLabel(master=frame, text="Extracting... please wait", font=("Roboto",24))
        # label.place(relx=0, rely=0, anchor=tkinter.CENTER)


        with open(summaryFileName, mode='a') as summary_file: 
            ct = str(datetime.datetime.now())
            summary_file.write("Summary of extraction: \n\nODBC Used: "+DSNVariable+"\n@ "+ct[0:19]+"hrs\n"+"========================")
                                  
            # Create a while loop for all tables required here
            while(tableCounter<len(sageTables)):
                # Create a cursor to execute SQL queries
                cursor = connection.cursor()
                # SQL query
                cursor.execute("SELECT * FROM " + sageTables[tableCounter])
                columns = [column[0] for column in cursor.description]
                rowCounter = 0
                tic = time.perf_counter()
                
                # Fetch and write results
                with open(DSNVariable+"-"+sageTables[tableCounter]+".csv", mode='w') as table_file:                
                    print(f"Executing: {sageTables[tableCounter]}") 

                    table_writer = csv.writer(table_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    # Write the table headers
                    table_writer.writerow(columns)
                    # Write all the rows of data
                    for row in cursor.fetchall():
                        table_writer.writerow(row)
                        rowCounter+=1
                
                # Print number of rows & timings
                toc = time.perf_counter()
                extractInfo = (f"{rowCounter} rows extracted in {toc - tic:0.4f} seconds")
                summary_file.write("\n"+sageTables[tableCounter]+": "+extractInfo)
                timer += (toc - tic)
                tableCounter+=1
                # Close the cursor and connection when done
                cursor.close()
            connection.close()
            print(f"\n\nTotal Time required: {timer:0.5f} seconds")
            summary_file.write(f"\n\nTotal Time required: {timer:0.5f} seconds\n------------------------------------\nEnjoy the rest of your migration :)")
        os.startfile(summaryFileName)# Launch summary file.
        messagebox.showinfo("Success","All files have been created")
        root.quit()

    except pyodbc.Error as e:
        messagebox.showinfo("Error",e)
        print("ODBC Error:", e)

# Initialise input dialog box
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
label  = customtkinter.CTkLabel(master=frame, text="Sage 50 (UK) ODBC Extractor System", font=("Roboto",24))
label.pack(pady=12,padx=5) 
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="ODBC Name")
entry1.pack(pady=12, padx=10)
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry2.pack(pady=12, padx=10)
entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry3.pack(pady=12, padx=10)
button = customtkinter.CTkButton(master=frame, text="Execute", command=Execute)
button.pack(pady=12, padx=10)
label  = customtkinter.CTkLabel(master=frame, text="by Kaustav Purakayastha (2023)", font=("Roboto", 12), text_color="lightblue", anchor="w")
label.pack() 
root.mainloop()