import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from reportlab.pdfgen import canvas
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.geometry("350x500")
root.title("Multi-Page Application")
pdf_counter = 1
total_entry = None  # Declare total_entry as a global variable



# Create a notebook to hold different pages
notebook = ttk.Notebook(root)

# Define two different pages as frames
page1 = ttk.Frame(notebook)
page2 = ttk.Frame(notebook)
page3 = ttk.Frame(notebook)
page4 = ttk.Frame(notebook)
page5 = ttk.Frame(notebook)
page6 = ttk.Frame(notebook)
page7 = ttk.Frame(notebook)
page8 = ttk.Frame(notebook)
page9 = ttk.Frame(notebook)
sum_total = 0
# Add content to each page
label1 = tk.Label(page1, text="Order Here...!!",font=("Arial",25)) 
label1.pack()

background_label = tk.Label(page1, bg="#DCDCDC")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add other widgets on top of the background label
background_label1 = tk.Label(page2, bg="#FAFAD2")
background_label1.place(x=0, y=0, relwidth=1, relheight=1)

image_path = "F:\coke.png"
image = Image.open(image_path)
resized_image = image.resize((260, 280))
photo_image = ImageTk.PhotoImage(resized_image)
image_label = tk.Label(page1, image=photo_image)
image_label.pack()
button1 = tk.Button(page1, text="TOUCH TO START",fg="white",bg="green",font=("Arial",27), command=lambda: switch_page(2))
button1.place(x=0,y=415)

label2 = tk.Label(page2, text="EATING LOCATION",font=("Arial",23))
label2.pack()

image_path1 = "F:\mcd1.png"
image1 = Image.open(image_path1)
resized_image1 = image1.resize((200,200))
photo_image1 = ImageTk.PhotoImage(resized_image1)
image_label1 = tk.Label(page2, image=photo_image1)
image_label1.pack()


background_label2 = tk.Label(page3, bg="#FAEBD7")
background_label2.place(x=0, y=0, relwidth=1, relheight=1)


button2 = tk.Button(page2, text="EAT IN",fg="white",bg="blue",font=("Arial",18), command=lambda: switch_page(3))
button2.place(x=40,y=280)
button3 = tk.Button(page2, text="TAKE OUT",fg="white",bg="green",font=("Arial",18), command=lambda: switch_page(3))
button3.place(x=180,y=280)

label3 = tk.Label(page3, text="Menuu....")
label3.pack()
button4 = tk.Button(page3, text="Burger",fg="white",bg="brown",font=("Arial",18), command=lambda: switch_page(4))
button4.place(x=130,y=60)
button5 = tk.Button(page3, text="Fries and sides",fg="white",bg="brown",font=("Arial",18), command=lambda: switch_page(5))
button5.place(x=90,y=120)
button6 = tk.Button(page3, text="chicken and fish sandwiches",fg="white",bg="brown",font=("Arial",18), command=lambda: switch_page(6))
button6.place(x=10,y=180)
button7 = tk.Button(page3, text="McCafe",fg="white",bg="brown",font=("Arial",18), command=lambda: switch_page(7))
button7.place(x=130,y=240)
button8 = tk.Button(page3, text="Bevarages",fg="white",bg="brown",font=("Arial",18), command=lambda: switch_page(8))
button8.place(x=120,y=300)

button93 = tk.Button(page3, text="Final Bill",fg="white",bg="skyblue",font=("Arial",15), command=lambda: switch_page(9))
button93.place(x=140,y=380)


background_label3 = tk.Label(page4, bg="#FFE4E1")
background_label3.place(x=0, y=0, relwidth=1, relheight=1)



label4 = tk.Label(page4, text="BBBBBB")
label4.pack()

# Initialize variable sum
sum = 0

# Define function to add to sum and switch to 4th page
def update_sum_and_switch(value, page4):
    global sum
    sum += value
    # Update sum in page 4 widget
    page4.sum_entry.delete(0, "end")
    page4.sum_entry.insert(0, str(sum))
    # Switch to page 4
    notebook.select(3)


label5 = tk.Label(page4, text="Big Mac - 100/-",font=("Arial",15))
label5.place(x=20,y=30)
button8 = tk.Button(page4, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch(100, page4))
button8.place(x=280,y=30)



label6 = tk.Label(page4, text="cheeseburger - 120/-",font=("Arial",15))
label6.place(x=20,y=60)
button8 = tk.Button(page4, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch(120, page4))
button8.place(x=280,y=60)

label7 = tk.Label(page4, text="Doublecheeseburger - 140/-",font=("Arial",15))
label7.place(x=20,y=90)
button9 = tk.Button(page4, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch(140, page4))
button9.place(x=280,y=90)


label9 = tk.Label(page4, text="McDouble - 90/-",font=("Arial",15))
label9.place(x=20,y=120)
button10 = tk.Button(page4, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch(90, page4))
button10.place(x=280,y=120)

label8 = tk.Label(page4, text="Total amout of burger is: ",font=("Arial",15))
label8.place(x=20,y=200)
page4.sum_entry = tk.Entry(master=page4, width=20,bg="pink",font=("Arial",16))
page4.sum_entry.place(x=60,y=250)

label61 = tk.Label(page4, text="Click here to show final bill",font=("Arial",15))
label61.place(x=20,y=300)

button11=tk.Button(page4, text="Bill",fg="white",bg="skyblue",font=("Arial",13), command=lambda:switch_page(9))
button11.place(x=150,y=330)

label62 = tk.Label(page4, text="Click here to conti. with other order ",font=("Arial",15))
label62.place(x=20,y=370)

b1=tk.Button(page4, text="Back to Main menu",fg="white",bg="skyblue",font=("Arial",15), command=lambda:switch_page(3))
b1.place(x=80,y=410)


background_label4 = tk.Label(page5, bg="#FFE4E1")
background_label4.place(x=0, y=0, relwidth=1, relheight=1)


label9 = tk.Label(page5, text="Fries and sides")
label9.pack()


# Initialize variable sum
sum1 = 0

# Define function to add to sum and switch to 4th page
def update_sum_and_switch1(value1, page5):
    global sum1
    sum1 += value1
    # Update sum in page 4 widget
    page5.sum_entry1.delete(0, "end")
    page5.sum_entry1.insert(0, str(sum1))
    # Switch to page 4
    notebook.select(4)

    



label10 = tk.Label(page5, text="Fries - 90/-",font=("Arial",15))
label10.place(x=20,y=30)
button12 = tk.Button(page5, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch1(90, page5))
button12.place(x=280,y=30)



label11 = tk.Label(page5, text="Apple slices - 100/-",font=("Arial",15))
label11.place(x=20,y=60)
button13 = tk.Button(page5, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch1(100, page5))
button13.place(x=280,y=60)

label12 = tk.Label(page5, text="Mustard pscket - 80/-",font=("Arial",15))
label12.place(x=20,y=90)
button14 = tk.Button(page5, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch1(80, page5))
button14.place(x=280,y=90)


label13 = tk.Label(page5, text="ketchup packet - 75/-",font=("Arial",15))
label13.place(x=20,y=120)
button15 = tk.Button(page5, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch1(75, page5))
button15.place(x=280,y=120)



label14 = tk.Label(page5, text="Total amout of fries and sides : ",font=("Arial",15))
label14.place(x=20,y=200)
page5.sum_entry1 = tk.Entry(master=page5, width=20,bg="pink",font=("Arial",16))
page5.sum_entry1.place(x=60,y=250)

label64 = tk.Label(page5, text="Click here to show final bill : ",font=("Arial",15))
label64.place(x=20,y=300)

button16=tk.Button(page5, text="Bill",fg="white",bg="skyblue",font=("Arial",13), command=lambda:switch_page(9))
button16.place(x=150,y=330)

label65=tk.Label(page5, text="Click here to conti. with other order",font=("Arial",15))
label65.place(x=20,y=370)

b2=tk.Button(page5, text="Back to Main menu",fg="white",bg="skyblue",font=("Arial",15), command=lambda:switch_page(3))
b2.place(x=80,y=410)


background_label4 = tk.Label(page6, bg="#FFE4E1")
background_label4.place(x=0, y=0, relwidth=1, relheight=1)


l15 = tk.Label(page6, text="chicken and fish sandwiches")
l15.pack()

# Initialize variable sum
sum2 = 0

# Define function to add to sum and switch to 4th page
def update_sum_and_switch2(value2, page6):
    global sum2
    sum2 += value2
    # Update sum in page 4 widget
    page6.sum_entry2.delete(0, "end")
    page6.sum_entry2.insert(0, str(sum2))
    # Switch to page 4
    notebook.select(5)


l16 = tk.Label(page6, text="McCrispy - 60/-",font=("Arial",15))
l16.place(x=20,y=30)
b17 = tk.Button(page6, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch2(60, page6))
b17.place(x=280,y=30)



l17 = tk.Label(page6, text="Filet-o-Fish - 100/-",font=("Arial",15))
l17.place(x=20,y=60)
b18 = tk.Button(page6, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch2(100, page6))
b18.place(x=280,y=60)

l18 = tk.Label(page6, text="McChicen - 120/-",font=("Arial",15))
l18.place(x=20,y=90)
b19 = tk.Button(page6, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch2(120, page6))
b19.place(x=280,y=90)


l19 = tk.Label(page6, text="Deluxe McCrispy - 150/-",font=("Arial",15))
l19.place(x=20,y=120)
b20 = tk.Button(page6, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch2(90, page6))
b20.place(x=280,y=120)

l20 = tk.Label(page6, text="Total amout of chicken and fish sandwiches is : ",font=("Arial",12))
l20.place(x=0,y=200)
page6.sum_entry2 = tk.Entry(master=page6, width=20,bg="pink",font=("Arial",16))
page6.sum_entry2.place(x=60,y=250)

l66 = tk.Label(page6, text="Click here to show final bill : ",font=("Arial",15))
l66.place(x=20,y=300)

b81=tk.Button(page6, text="Bill",fg="white",bg="skyblue",font=("Arial",13), command=lambda:switch_page(9))
b81.place(x=150,y=330)

l67 = tk.Label(page6, text="Click here to conti. with other order",font=("Arial",15))
l67.place(x=20,y=370)

b91=tk.Button(page6, text="Back to Main menu",fg="white",bg="skyblue",font=("Arial",15), command=lambda:switch_page(3))
b91.place(x=80,y=410)


background_label8 = tk.Label(page7, bg="#FFE4E1")
background_label8.place(x=0, y=0, relwidth=1, relheight=1)



l26 = tk.Label(page7, text="Mcafe")
l26.pack()

# Initialize variable sum
sum3 = 0

# Define function to add to sum and switch to 4th page
def update_sum_and_switch3(value3, page7):
    global sum3
    sum3 += value3
    # Update sum in page 4 widget
    page7.sum_entry3.delete(0, "end")
    page7.sum_entry3.insert(0, str(sum3))
    # Switch to page 4
    notebook.select(6)





l21 = tk.Label(page7, text="Cappuccino - 100/-",font=("Arial",15))
l21.place(x=20,y=30)
b22 = tk.Button(page7, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch3(100, page7))
b22.place(x=280,y=30)



l22 = tk.Label(page7, text="Mocha Latte - 120/-",font=("Arial",15))
l22.place(x=20,y=60)
b23 = tk.Button(page7, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch3(120, page7))
b23.place(x=280,y=60)

l23 = tk.Label(page7, text="Iced Mocha - 120/-",font=("Arial",15))
l23.place(x=20,y=90)
b24 = tk.Button(page7, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch3(120, page7))
b24.place(x=280,y=90)


l24 = tk.Label(page7, text="Iced Coffee - 110/-",font=("Arial",15))
l24.place(x=20,y=120)
b25 = tk.Button(page7, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch3(110, page7))
b25.place(x=280,y=120)

l25 = tk.Label(page7, text="Total amout of McCafe is : ",font=("Arial",15))
l25.place(x=20,y=200)
page7.sum_entry3 = tk.Entry(master=page7, width=20,bg="pink",font=("Arial",16))
page7.sum_entry3.place(x=60,y=250)

l67 = tk.Label(page7, text="Click here to show final bill : ",font=("Arial",15))
l67.place(x=20,y=300)

b71=tk.Button(page7, text="Bill",fg="white",bg="skyblue",font=("Arial",13), command=lambda:switch_page(9))
b71.place(x=150,y=330)

l68 = tk.Label(page7, text="Click here to conti. with other order",font=("Arial",15))
l68.place(x=20,y=370)

b72=tk.Button(page7, text="Back to Main menu",fg="white",bg="skyblue",font=("Arial",15), command=lambda:switch_page(3))
b72.place(x=80,y=410)




background_label9 = tk.Label(page8, bg="#FFE4E1")
background_label9.place(x=0, y=0, relwidth=1, relheight=1)



l27 = tk.Label(page8, text="Bevarages")
l27.pack()

# Initialize variable sum
sum4 = 0

# Define function to add to sum and switch to 4th page
def update_sum_and_switch4(value4, page7):
    global sum4
    sum4 += value4
    # Update sum in page 4 widget
    page8.sum_entry4.delete(0, "end")
    page8.sum_entry4.insert(0, str(sum4))
    # Switch to page 4
    notebook.select(7)



l28 = tk.Label(page8, text="Coca  cola - 80/-",font=("Arial",15))
l28.place(x=20,y=30)
b27 = tk.Button(page8, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch4(80, page8))
b27.place(x=280,y=30)



l29 = tk.Label(page8, text="Dr Pepper - 110/-",font=("Arial",15))
l29.place(x=20,y=60)
b28 = tk.Button(page8, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch4(110, page8))
b28.place(x=280,y=60)

l30 = tk.Label(page8, text="Fanta - 100/-",font=("Arial",15))
l30.place(x=20,y=90)
b29 = tk.Button(page8, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch4(100, page8))
b29.place(x=280,y=90)


l31 = tk.Label(page8, text="Lemonade - 110/-",font=("Arial",15))
l31.place(x=20,y=120)
b30 = tk.Button(page8, text="Add",fg="white",bg="blue",font=("Arial",10), command=lambda: update_sum_and_switch4(110, page8))
b30.place(x=280,y=120)

l32 = tk.Label(page8, text="Total amout of Bevarages is : ",font=("Arial",15))
l32.place(x=20,y=200)
page8.sum_entry4 = tk.Entry(master=page8, width=20,bg="pink",font=("Arial",16))
page8.sum_entry4.place(x=60,y=250)

l69 = tk.Label(page8, text="Click here to show final bill : ",font=("Arial",15))
l69.place(x=20,y=300)

b74=tk.Button(page8, text="Bill",fg="white",bg="skyblue",font=("Arial",13), command=lambda:switch_page(9))
b74.place(x=150,y=330)

l68 = tk.Label(page8, text="Click here to conti. with other order",font=("Arial",15))
l68.place(x=20,y=370)

b75=tk.Button(page8, text="Back to Main menu",fg="white",bg="skyblue",font=("Arial",15), command=lambda:switch_page(3))
b75.place(x=80,y=410)


background_label11 = tk.Label(page9, bg="#FFE4E1")
background_label11.place(x=0, y=0, relwidth=1, relheight=1)



label34 = tk.Label(page9, text="Total Amount:", font=("Arial", 20))
label34.pack()

total_entry = tk.Entry(master=page9, width=20, bg="pink",font=("Arial",16))
total_entry.pack()


label35 = tk.Label(page9, text="THANK YOU..!", font=("Arial", 20),fg="red")
label35.place(x=90,y=230)

label36 = tk.Label(page9, text="VISIT AGAIN!", font=("Arial", 20),fg="red")
label36.place(x=90,y=270)



def update_total():
    global sum_total
    sum_total = 0

    # Add total from each page entry
    try:
        sum_total += int(page4.sum_entry.get())
    except ValueError:
        pass
    try:
        sum_total += int(page5.sum_entry1.get())
    except ValueError:
        pass
    try:
        sum_total += int(page6.sum_entry2.get())
    except ValueError:
        pass
    try:
        sum_total += int(page7.sum_entry3.get())
    except ValueError:
        pass
    try:
        sum_total += int(page8.sum_entry4.get())
    except ValueError:
        pass

    # Update total entry in page 9
    total_entry.delete(0, "end")
    total_entry.insert(0, str(sum_total))




# Update total before switching pages
update_total()

# Switch to page 9
#notebook.select(page9)

# Add pages to the notebook and pack it
notebook.add(page1, text="")
notebook.add(page2, text="")
notebook.add(page3, text="")
notebook.add(page4, text="")
notebook.add(page5, text="")
notebook.add(page6, text="")
notebook.add(page7, text="")
notebook.add(page8, text="")
notebook.add(page9, text="")
notebook.pack(fill="both", expand=True)

# Define function to switch between pages
def switch_page(page_number):
    if page_number == 1:
        notebook.select(page1)
    elif page_number == 2:
        notebook.select(page2)
    elif page_number == 3:
        notebook.select(page3)
    elif page_number == 4:
        notebook.select(page4)
    elif page_number == 5:
        notebook.select(page5)
    elif page_number == 6:
        notebook.select(page6)
    elif page_number == 7:
        notebook.select(page7)
    elif page_number == 8:
        notebook.select(page8)
    elif page_number == 9:
        update_total()
        notebook.select(page9)
    else:
        raise ValueError("Invalid page number")


    # Update total entry in page 9
    total_entry.delete(0, "end")
    total_entry.insert(0, str(sum_total))

# Define function to generate PDF
def generate_pdf():
    global pdf_counter

    # Get the total amount from the entry widget
    try:
        total_amount = int(total_entry.get())
    except ValueError:
        total_amount = 0

    # Create a PDF file
    pdf_filename = f"bill_{pdf_counter}.pdf"
    pdf_counter += 1
    c = canvas.Canvas(pdf_filename)
    
    # Add content to the PDF
    c.drawString(100, 750, "McDonald's Bill")
    c.drawString(100, 730, "-" * 40)

    # Add details from each page
    c.drawString(100, 700, f"Total Burgers: {page4.sum_entry.get()}")
    c.drawString(100, 680, f"Total Fries and Sides: {page5.sum_entry1.get()}")
    c.drawString(100, 660, f"Total Chicken and Fish Sandwiches: {page6.sum_entry2.get()}")
    c.drawString(100, 640, f"Total McCafe: {page7.sum_entry3.get()}")
    c.drawString(100, 620, f"Total Beverages: {page8.sum_entry4.get()}")
    c.drawString(100, 600, "-" * 40)
    c.drawString(100, 580, f"Total Amount: {total_amount}")

    # Save the PDF file
    c.save()








# Add a command to the "Generate PDF" button
generate_pdf_button = tk.Button(page9, text="Generate PDF", fg="white", bg="skyblue", font=("Arial", 15), command=generate_pdf)
generate_pdf_button.place(x=120, y=330)

# Start the main event loop
root.mainloop()

