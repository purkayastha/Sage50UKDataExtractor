# import module
from tkinter import *
from tkinter import messagebox


# configure 
ws = Tk()
ws.title("Login Page")
ws.geometry("300x250")

# functions
def checkCred():
    email = email_tf.get()
    pwd = pwd_tf.get()
    print(email, pwd)
    if email == "python" and pwd == "guides":
        return messagebox.showinfo("Login", "Login Sucessfully!")
    else:
        return messagebox.showerror("Login", "Login Failed!")
def success_msg():
    return messagebox.showinfo("Signup", "Sign-up Successfully")
    
def register():
    ws = Tk()
    ws.title("Register")
    ws.geometry("300x250")

    Label(ws, text="Enter Name").place(x=50, y=20, anchor="center")
    nTf =Entry(ws).place(x=170, y=20, anchor=CENTER)
    Label(ws, text="Enter Email").place(x=50, y=60, anchor=CENTER)
    eTf = Entry(ws).place(x=170, y=60, anchor=CENTER)
    Label(ws, text="Password").place(x=50, y=100, anchor=CENTER)
    pTf = Entry(ws).place(x=170, y=100, anchor=CENTER)
    Label(ws, text="re-enter Password").place(x=50, y=140, anchor=CENTER)
    rpTf = Entry(ws).place(x=170, y=140, anchor=CENTER)
    Button(ws, text="Register", command=success_msg).place(x=100, y=180, anchor=CENTER)

    
# write code
email_lb = Label(ws,text="Enter Email")
email_tf = Entry(ws)
pwd_lb = Label(ws,text="Enter Password")
pwd_tf = Entry(ws)
login_btn = Button(ws, text="Login", command=checkCred)
reg_btn = Button(ws, text="Register", command=register)


# placeholders
email_lb.place(x=50, y=40, anchor=CENTER)
email_tf.place(x=170, y=40, anchor=CENTER)
pwd_lb.place(x=50, y=80, anchor=CENTER)
pwd_tf.place(x=170, y=80, anchor=CENTER)
login_btn.place(x=100, y=120, anchor=CENTER)
reg_btn.place(x=180, y=120, anchor=CENTER)


# infinite loop
ws.mainloop()




# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("green")
# root = customtkinter.CTk()
# root.geometry("650x400")
# root.iconbitmap(default="icon.ico")
# root.title("Sage 50 (UK) ODBC Extractor System")


# def Execute():
#     DSNVariable = "SMHTGolive"
#     userName = "Manager"
#     passWord = "dog4you"
#     #root.quit() # do we need to do this here????
    
#     odbc_connection_string = "DSN="+ DSNVariable + ";UID=" + userName + ";PWD=" + passWord
#     sageTables = ["NOMINAL_LEDGER","BANK","PURCHASE_LEDGER"]#,"PURCHASE_ORDER","SALES_LEDGER","SALES_ORDER","STOCK","STOCK_TRAN","PROJECT","PROJECT_TRAN","AUDIT_HEADER","AUDIT_JOURNAL"]

#     try:
#         # Establish the ODBC connection
#         connection = pyodbc.connect(odbc_connection_string)
#         tableCounter = 0
#         timer = 0
#         summaryFileName = DSNVariable+"-"+"ExtractionSummary.txt"
#         #these two line clears the data in the summary file.
#         fileToDelete = open(summaryFileName,'w') 
#         fileToDelete.close()

#         frame2 = customtkinter.CTkFrame(master=frame)
#         frame2.pack(pady=20, padx=60, fill="both", expand=True)
#         root.lift()
#         label1  = customtkinter.CTkLabel(master=frame2, text="Extraction progress", font=("Roboto",24))
#         label1.pack(pady=12,padx=5) 
        
#         with open(summaryFileName, mode='a') as summary_file: 
#             ct = str(datetime.datetime.now())
#             summary_file.write("Summary of extraction: \n\nODBC Used: "+DSNVariable+"\n@ "+ct[0:19]+"hrs\n"+"========================")                                  
#             # Create a while loop for all tables required here
#             while(tableCounter<len(sageTables)):
#                 # Create a cursor to execute SQL queries
#                 cursor = connection.cursor()
#                 # SQL query
#                 cursor.execute("SELECT * FROM " + sageTables[tableCounter])
#                 columns = [column[0] for column in cursor.description]
#                 rowCounter = 0
#                 tic = time.perf_counter()
                
#                 # Fetch and write results
#                 with open(DSNVariable+"-"+sageTables[tableCounter]+".csv", mode='w') as table_file:                
#                     print(f"Executing: {sageTables[tableCounter]}") 

#                     table_writer = csv.writer(table_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#                     # Write the table headers
#                     table_writer.writerow(columns)
#                     # Write all the rows of data
#                     for row in cursor.fetchall():
#                         table_writer.writerow(row)
#                         rowCounter+=1
                
#                 # Print number of rows & timings
#                 toc = time.perf_counter()
#                 extractInfo = (f"{rowCounter} rows extracted in {toc - tic:0.4f} seconds")
#                 summary_file.write("\n"+sageTables[tableCounter]+": "+extractInfo)
#                 timer += (toc - tic)
#                 tableCounter+=1
#                 # Close the cursor and connection when done
#                 cursor.close()
#             connection.close()
#             print(f"\n\nTotal Time required: {timer:0.5f} seconds")
#             summary_file.write(f"\n\nTotal Time required: {timer:0.5f} seconds\n------------------------------------\nEnjoy the rest of your migration :)")
#         os.startfile(summaryFileName)# Launch summary file.
#         #root.quit()

#     except pyodbc.Error as e:
#         print("ODBC Error:", e)

# # Initialise input dialog box
# frame = customtkinter.CTkFrame(master=root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)
# label  = customtkinter.CTkLabel(master=frame, text="Sage 50 (UK) ODBC Extractor System", font=("Roboto",24))
# label.pack(pady=12,padx=5) 
# entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="ODBC Name")
# entry1.pack(pady=12, padx=10)
# entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
# entry2.pack(pady=12, padx=10)
# entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
# entry3.pack(pady=12, padx=10)
# button = customtkinter.CTkButton(master=frame, text="Execute", command=Execute)
# button.pack(pady=12, padx=10)
# label  = customtkinter.CTkLabel(master=frame, text="by Kaustav Purakayastha (2023)", font=("Roboto",12 ), text_color="lightblue", anchor="w")
# label.pack(pady=40,padx=5) 
# root.mainloop()