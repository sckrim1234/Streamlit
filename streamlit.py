
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector as sql
import matplotlib.pyplot as plt



#SETTINGS----------------------

details = ["ID","NAME","ADDRESS","CITY","PHONE NUMBER","MAIL"]
months = ["JANUARY",'FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
currency = "₹"
page_title = "Water Management Project"
page_icon = ":potable_water:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

#--------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title )

mycon = sql.connect(host="localhost",port =3306,user='root',passwd='aasma@5464')
cur = mycon.cursor()
cur.execute("create database if not exists CSProject")
cur.execute("use CSProject")

cur.execute("create table if not exists Waterproject(ID varchar(20) Primary Key, NAME varchar(40) NOT NULL, ADDRESS varchar(100) NOT NULL, CITY varchar(100) NOT NULL, PHONE_NUMBER varchar(100) NOT NULL,MAIL varchar(100) NOT NULL,JANUARY int NOT NULL,FEBRUARY int NOT NULL,MARCH int NOT NULL,APRIL int NOT NULL,MAY int NOT NULL,JUNE int NOT NULL,JULY int NOT NULL,AUGUST int NOT NULL,SEPTEMBER int NOT NULL,OCTOBER int NOT NULL,NOVEMBER int NOT NULL,DECEMBER int NOT NULL)")

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization"],
    icons=["pencil-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)
#------------------------

if selected == "Data Entry":
    option = st.sidebar.selectbox("Select an Operation",("Add Data","Update Data","Delete Data"))
    if option == "Add Data" :
        st.subheader("Add Records to the DATABASE")
        id = st.text_input("Enter your ID: ")
        name = st.text_input("Enter your NAME: ")
        address = st.text_input("Enter your ADDRESS: ")
        city = st.text_input("Enter your CITY: ")
        phone = st.text_input("Enter your PHONE NUMBER: ")
        mail = st.text_input("Enter your MAIL ID: ")
        with st.expander("Consumption of Water in Litres(Per Month)"):
            jan = st.number_input("January: ", min_value=0, format="%i", step=10)
            feb = st.number_input("February: ",min_value=0, format="%i", step=10)
            mar = st.number_input("March: ",min_value=0, format="%i", step=10)
            apr = st.number_input("April: ",min_value=0, format="%i", step=10)
            may = st.number_input("May: ",min_value=0, format="%i", step=10)
            jun = st.number_input("June: ",min_value=0, format="%i", step=10)
            jul = st.number_input("July: ",min_value=0, format="%i", step=10)
            aug = st.number_input("August: ",min_value=0, format="%i", step=10)
            sep = st.number_input("September: ",min_value=0, format="%i", step=10)
            oct = st.number_input("October: ",min_value=0, format="%i", step=10)
            nov = st.number_input("November: ",min_value=0, format="%i", step=10)
            dec = st.number_input("December: ",min_value=0, format="%i", step=10)
        if st.button("Add"):
            cur.execute(f"insert into Waterproject values('{id}','{name}','{address}','{city}','{phone}','{mail}',{jan},{feb},{mar},{apr},{may},{jun},{jul},{aug},{sep},{oct},{nov},{dec})")
            mycon.commit()
            st.success("Record Added Successfully !")


    if option == "Update Data" :
        st.subheader("Update Records to the DATABASE")
        id = st.text_input("Enter your ID: ")
        query = "SELECT * FROM waterproject WHERE id = %s"
        cur.execute(query, (id,))
        if cur.fetchone():
            name = st.text_input("Enter your NAME: ")
            address = st.text_input("Enter your ADDRESS: ")
            city = st.text_input("Enter your CITY: ")
            phone = st.text_input("Enter your PHONE NUMBER: ")
            mail = st.text_input("Enter your MAIL ID: ")
            with st.expander("Consumption of Water in Litres(Per Month)"):
                jan = st.number_input("January: ", min_value=0, format="%i", step=10)
                feb = st.number_input("February: ",min_value=0, format="%i", step=10)
                mar = st.number_input("March: ",min_value=0, format="%i", step=10)
                apr = st.number_input("April: ",min_value=0, format="%i", step=10)
                may = st.number_input("May: ",min_value=0, format="%i", step=10)
                jun = st.number_input("June: ",min_value=0, format="%i", step=10)
                jul = st.number_input("July: ",min_value=0, format="%i", step=10)
                aug = st.number_input("August: ",min_value=0, format="%i", step=10)
                sep = st.number_input("September: ",min_value=0, format="%i", step=10)
                oct = st.number_input("October: ",min_value=0, format="%i", step=10)
                nov = st.number_input("November: ",min_value=0, format="%i", step=10)
                dec = st.number_input("December: ",min_value=0, format="%i", step=10)
            if st.button("Update"):
                cur.execute(f"update Waterproject set ID='{id}',NAME='{name}',ADDRESS='{address}',CITY='{city}',PHONE_NUMBER='{phone}',MAIL='{mail}',JANUARY={jan},FEBRUARY={feb},MARCH={mar},APRIL={apr},MAY={may},JUNE={jun},JULY={jul},AUGUST={aug},SEPTEMBER={sep},OCTOBER={oct},NOVEMBER={nov},DECEMBER={dec} where ID='{id}'")
                mycon.commit()
                st.success("Record Updated Successfully !")
        else:
            st.error("This ID does not exist. Please check again.", icon="🚨")

    if option == "Delete Data":
        st.subheader("Delete Records in the DATABASE")
        id = st.text_input("Enter your ID: ")
        query = "SELECT * FROM waterproject WHERE id = %s"
        cur.execute(query, (id,))
        if cur.fetchone():
            cur.execute(f"delete from waterproject where ID='{id}'")
            mycon.commit()
            st.success("Record Deleted Successfully !")
        else:
            st.error("This ID does not exist. Please check again.", icon="🚨")

elif selected == "Data Visualization" :
    option2 = st.sidebar.selectbox("Select an Operation", ("View All Data", "View Total Water Consumption Bill","Plot Graph for Personal Records", "Plot Graph for All Records"))
    if option2 == "View All Data":
        query2 = "SELECT * FROM waterproject"
        cur.execute(query2)
        data = cur.fetchall()
        df = pd.DataFrame(data, columns=[i[0] for i in cur.description])
        st.dataframe(df)

    if option2 == "View Total Water Consumption Bill":
        id = st.text_input("Enter your ID: ")
        query = "SELECT * FROM waterproject WHERE id = %s"
        cur.execute(query, (id,))
        if cur.fetchone():
            sql_query = f"SELECT JANUARY + FEBRUARY + MARCH + APRIL+MAY+JUNE+JULY+AUGUST+SEPTEMBER+OCTOBER+NOVEMBER+DECEMBER FROM waterproject WHERE ID = '{id}'"
            cur.execute(sql_query)
            amt = cur.fetchone()[0] * 20
            st.write(f"Transaction Amount: ₹{amt}")

            if amt < 500:
                cashback = 500 - amt
                st.write(f"** ₹{cashback} will be added to your total as cashback **")
                st.write("Meter Fees: ₹100")
                amt = (amt * 2) - 400
                if amt < 0:
                    st.write(f"Reward: ₹{amt * (-1)}")
                else:
                    st.write(f"Total amount: ₹{((amt * 2) - 400)}")
            elif amt > 1500:
                fine = (amt - 1500) * 4
                amt = amt + fine
                st.write(f"** You have incurred a fine of ₹{fine} **")
                st.write("Meter Fees: ₹100")
                st.write(f"Total amount: ₹{(amt + 100)}")
            else:
                st.write(f"Total amount: ₹{(amt * 2)}")

        else:
            st.error("This ID does not exist. Please check again.", icon="🚨")

    if option2 == "Plot Graph for Personal Records":
        id = st.text_input("Enter your ID: ")
        query = "SELECT * FROM waterproject WHERE id = %s"
        cur.execute(query, (id,))
        record = cur.fetchone()

        if record:
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]
            try :
                s = id + ":" + record[1]
                plt.plot(months,record[6:])
                plt.suptitle(s)
                plt.xlabel("Months")
                plt.xticks(rotation=90, ha="right")
                plt.ylabel("Amount of Water Consumed (in litres)")
                st.pyplot(plt)
            except:
                pass
        else:
            st.error("This ID does not exist. Please check again.", icon="🚨")

    if option2 == "Plot Graph for All Records":
        query = "SELECT * FROM waterproject"
        cur.execute(query)
        records= cur.fetchall()
        names = []
        amounts=[]
        if records:
            for i in records:
                names.append(i[1])
                sum1 = sum(i[6:])
                amounts.append(sum1)
            try:
                color = ["y", "m", "g", "b", "r"]
                plt.bar(names,amounts,width=0.3, color=color)
                plt.xlabel("Names")
                plt.xticks(rotation=90, ha="right")
                plt.ylabel("Total Amount of Water Consumed (in litres)")
                st.pyplot(plt)
            except:
                pass
        else:
            st.error("Database is empty", icon="🚨")

