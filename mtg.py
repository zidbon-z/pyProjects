
from tkinter import *
#from PIL import ImageTk,Image
import sqlite3

############## Tutorial #23 ##############################

root = Tk()
root.title('Magic the Gathering Card Catalog')
root.geometry("400x200")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('card_catalog.db')

# Create cursor
c = conn.cursor()

#Create table
'''
c.execute("""CREATE TABLE catalog (
    card_name text,
    card_type text,
    card_race text,
    card_class text,
    card_color text,
    card_manacost integer,
    card_power integer,
    card_toughness integer,
    card_oracle text,
    card_deck text,
    card_deck_quantity integer
    )""")
'''
# Create a window that lists all cards in catalog
def list_cards():
    list_cards_w = Tk()
    list_cards_w.title('All Cards in Catalog')
    list_cards_w.geometry('400x800')

    
    c_title_id_label = Label(list_cards_w, text="ID", width=20)
    c_title_id_label.grid(row=1, column=0, ipady=10)
    c_title_name_label = Label(list_cards_w, text="Card Name ", width=30)
    c_title_name_label.grid(row=1, column=1, ipady=10)

    # Create a database or connect to one
    conn = sqlite3.connect('card_catalog.db')
    # Create cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT *, oid FROM catalog")
    show_cards = c.fetchall()
    #print(show_cards)

    # Loop Thru Results
    print_cards = ''
    print_cards_id = ''
    print_cards_name = ''
    for card in show_cards:

        # Format the query output
        print_cards_id += str(card[11]) + "\n"
        query_label = Label(list_cards_w, text=print_cards_id)
        query_label.grid(row=2, column=0)

        print_cards_name += str(card[0]) + "\n"
        query_label2 = Label(list_cards_w, text=print_cards_name)
        query_label2.grid(row=2, column=1)

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


# Create a Window to Add a Card
def add_card():
    add_card_w = Tk()
    add_card_w.title('Add a Card to Catalog')
    add_card_w.geometry("400x500")

    # Create Global Variables for Text Box Names
    global c_name
    global c_type
    global c_race
    global c_class
    global c_color
    global c_manacost
    global c_power
    global c_toughness
    global c_oracle
    global c_deck
    global c_deck_quantity


    # Create Text Boxes 
    c_name = Entry(add_card_w, width=30)
    c_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    c_type = Entry(add_card_w, width=30)
    c_type.grid(row=1, column=1,)
    c_race = Entry(add_card_w, width=30)
    c_race.grid(row=2, column=1,)
    c_class = Entry(add_card_w, width=30)
    c_class.grid(row=3, column=1,)
    c_color = Entry(add_card_w, width=30)
    c_color.grid(row=4, column=1,)
    c_manacost = Entry(add_card_w, width=30)
    c_manacost.grid(row=5, column=1,)
    c_power = Entry(add_card_w, width=30)
    c_power.grid(row=6, column=1,)
    c_toughness = Entry(add_card_w, width=30)
    c_toughness.grid(row=7, column=1,)
    c_oracle = Entry(add_card_w, width=30)
    c_oracle.grid(row=8, column=1,)
    c_deck = Entry(add_card_w, width=30)
    c_deck.grid(row=9, column=1,)
    c_deck_quantity = Entry(add_card_w, width=30)
    c_deck_quantity.grid(row=10, column=1)

    # Create Text Box Lables
    c_name_label = Label(add_card_w, text="Card Name")
    c_name_label.grid(row=0, column=0, pady=(10, 0))
    c_type_label = Label(add_card_w, text="Card Type")
    c_type_label.grid(row=1, column=0)
    c_race_label = Label(add_card_w, text="Card Race")
    c_race_label.grid(row=2, column=0)
    c_class_label = Label(add_card_w, text="Card Class")
    c_class_label.grid(row=3, column=0)
    c_color_label = Label(add_card_w, text="Card Color")
    c_color_label.grid(row=4, column=0)
    c_manacost_label = Label(add_card_w, text="Card Mana Cost")
    c_manacost_label.grid(row=5, column=0)
    c_power_label = Label(add_card_w, text="Card Power")
    c_power_label.grid(row=6, column=0)
    c_toughness_label = Label(add_card_w, text="Card Toughness")
    c_toughness_label.grid(row=7, column=0)
    c_oracle_label = Label(add_card_w, text="Card Oracle")
    c_oracle_label.grid(row=8, column=0)
    c_deck_label = Label(add_card_w, text="Deck")
    c_deck_label.grid(row=9, column=0)
    c_deck_quantity_label = Label(add_card_w, text="Quantity in Deck")
    c_deck_quantity_label.grid(row=10, column=0)

    # Create a Button to Save a Card in the Add Card Window
    add_btn = Button(add_card_w, text="Save", command=submit)
    add_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=50)



# Create a window to delete a card
def delete_window():
    delete_w = Tk()
    delete_w.title('Delete a Card')
    delete_w.geometry("400x400")

    # Create Text Box Labels in the Delete Window
    c_delete_label = Label(delete_w, text="ID of Card to Delete")
    c_delete_label.grid(row=0, column=0)

    # Create Text Box in the Delete Window
    c_delete = Entry(delete_w, width=30)
    c_delete.grid(row=0, column=1)
    
    # Create Delete Button
    delete_btn = Button(delete_w, text="Delete Card", command=delete)
    delete_btn.grid(row=1, column=1, pady=10, padx=10, ipadx=50)


    
# Create Delete Function
def delete():

    # Create a database or connect to one
    conn = sqlite3.connect('card_catalog.db')
    # Create cursor
    c = conn.cursor()

    # Delete a Card
    c.execute("DELETE from catalog WHERE oid = " + c_delete.get())

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear the Delete ID Box
    c_delete.delete(0, END)




# Create a Window to Edit a card
def edit():
    editor = Tk()
    editor.title('Edit a Card')
    editor.geometry("400x400")
    



    # Create Text Box Lables in the Editor Window
    editor_c_name_label = Label(editor, text="Card Name")
    editor_c_name_label.grid(row=0, column=0, pady=(10, 0))
    editor_c_type_label = Label(editor, text="Card Type")
    editor_c_type_label.grid(row=1, column=0)
    editor_c_race_label = Label(editor, text="Card Race")
    editor_c_race_label.grid(row=2, column=0)
    editor_c_class_label = Label(editor, text="Card Class")
    editor_c_class_label.grid(row=3, column=0)
    editor_c_color_label = Label(editor, text="Card Color")
    editor_c_color_label.grid(row=4, column=0)
    editor_c_manacost_label = Label(editor, text="Card Mana Cost")
    editor_c_manacost_label.grid(row=5, column=0)
    editor_c_power_label = Label(editor, text="Card Power")
    editor_c_power_label.grid(row=6, column=0)
    editor_c_toughness_label = Label(editor, text="Card Toughness")
    editor_c_toughness_label.grid(row=7, column=0)
    editor_c_oracle_label = Label(editor, text="Card Oracle")
    editor_c_oracle_label.grid(row=8, column=0)
    editor_c_deck_label = Label(editor, text="Deck")
    editor_c_deck_label.grid(row=9, column=0)
    editor_c_deck_quantity_label = Label(editor, text="Quantity in Deck")
    editor_c_deck_quantity_label.grid(row=10, column=0)
   
    # Create Text Boxes in the Editor Window 
    editor_c_name = Entry(editor, width=30)
    editor_c_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    editor_c_type = Entry(editor, width=30)
    editor_c_type.grid(row=1, column=1,)
    editor_c_race = Entry(editor, width=30)
    editor_c_race.grid(row=2, column=1,)
    editor_c_class = Entry(editor, width=30)
    editor_c_class.grid(row=3, column=1,)
    editor_c_color = Entry(editor, width=30)
    editor_c_color.grid(row=4, column=1,)
    editor_c_manacost = Entry(editor, width=30)
    editor_c_manacost.grid(row=5, column=1,)
    editor_c_power = Entry(editor, width=30)
    editor_c_power.grid(row=6, column=1,)
    editor_c_toughness = Entry(editor, width=30)
    editor_c_toughness.grid(row=7, column=1,)
    editor_c_oracle = Entry(editor, width=30)
    editor_c_oracle.grid(row=8, column=1,)
    editor_c_deck = Entry(editor, width=30)
    editor_c_deck.grid(row=9, column=1,)
    editor_c_deck_quantity = Entry(editor, width=30)
    editor_c_deck_quantity.grid(row=10, column=1)

    # Create a database or connect to one
    conn = sqlite3.connect('card_catalog.db')
    # Create cursor
    c = conn.cursor()

    
    card_id = c_delete.get()
    
    # Query the Database
    c.execute("SELECT * FROM catalog WHERE oid = " + card_id)
    show_cards = c.fetchall()
    for card in show_cards:
        editor_c_name.insert(0, card[0])
        editor_c_type.insert(0, card[1])
        editor_c_race.insert(0, card[2])
        editor_c_class.insert(0, card[3])
        editor_c_color.insert(0, card[4])
        editor_c_manacost.insert(0, card[5])
        editor_c_power.insert(0, card[6])
        editor_c_toughness.insert(0, card[7])
        editor_c_oracle.insert(0, card[8])
        editor_c_deck.insert(0, card[9])
        editor_c_deck_quantity.insert(0, card[10])
    
    # Create a Save Button
    save_btn = Button(editor, text="Save")
    save_btn.grid(row=11, column=0, columnspan=2, padx=5, pady=10, ipadx=100)
  

# Create Submit Function
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('card_catalog.db')
    # Create cursor
    c = conn.cursor()

    #Insert Into Table
    c.execute("INSERT INTO catalog VALUES (:c_name, :c_type, :c_race, :c_class, :c_color, :c_manacost, :c_power, :c_toughness, :c_oracle, :c_deck, :c_deck_quantity)",
    {
            'c_name': c_name.get(),
            'c_type': c_type.get(),
            'c_race': c_race.get(),
            'c_class': c_class.get(),
            'c_color': c_color.get(),
            'c_manacost': c_manacost.get(),
            'c_power': c_power.get(),
            'c_toughness': c_toughness.get(),
            'c_oracle': c_oracle.get(),
            'c_deck': c_deck.get(),
            'c_deck_quantity': c_deck_quantity.get()
    })        

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


    #Clear The Text Boxes
    c_name.delete(0, END)
    c_type.delete(0, END)
    c_race.delete(0, END)
    c_class.delete(0, END)
    c_color.delete(0, END)
    c_manacost.delete(0, END)
    c_power.delete(0, END)
    c_toughness.delete(0, END)
    c_oracle.delete(0, END)
    c_deck.delete(0, END)
    c_deck_quantity.delete(0, END)

# Create Query Function

def query():

    # Create a database or connect to one
    conn = sqlite3.connect('card_catalog.db')
    # Create cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT *, oid FROM catalog")
    show_cards = c.fetchall()
    #print(show_cards)

    # Loop Thru Results
    print_cards = ''
    print_cards_id = ''
    print_cards_name = ''
    for card in show_cards:

        # Format the query output
        print_cards_id += str(card[11]) + "\n"
        query_label = Label(root, text=print_cards_id)
        query_label.grid(row=16, column=0)

        print_cards_name += str(card[0]) + "\n"
        query_label2 = Label(root, text=print_cards_name)
        query_label2.grid(row=16, column=1)

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()



# Create Submit Button
submit_btn = Button(root, text="Add Card", command=add_card)
submit_btn.grid(row=11, column=0, pady=10, padx=10, ipadx=50)

# Create Delete Window Button
delete_btn = Button(root, text="Delete Card", command=delete_window)
delete_btn.grid(row=11, column=1, pady=10, padx=10, ipadx=50)


# Create a Query Button
query_btn = Button(root, text="List Cards", command=list_cards)
query_btn.grid(row=1, column=0, columnspan=2, pady=5, padx=10, ipadx=130)

# Create a Button to Edit Cards
edit_btn = Button(root, text="Edit Card", command=edit)
edit_btn.grid(row=13, column=0, pady=10, padx=10, ipadx=50)


# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()

