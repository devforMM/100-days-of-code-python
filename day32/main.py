#-------------------------------- managing date------------------------------------------------#
import datetime as dt



today=dt.datetime.today()
t_jour=today.day
t_mois=today.month
t_annnee=today.year
today=f"{t_jour}-{t_mois}-{t_annnee}"


#------------------------------ sending the  email ---------------------------------#
import smtplib


email="izuna867@gmail.com"
password="vgjkduiidiiykzjv"
def send_email(reciever,content):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=reciever,
            msg=f"Happy birthday letter \n\n{content} "
        )
        

#----------------------------- importing data -----------------------------------------------#
import pandas


data=pandas.read_csv("./day32/birthdasys.csv")
friends=data.to_dict(orient="records")

def get_friend():
 for friend in friends:
    f_birthday=f"{friend["day"]}-{friend["month"]}-{friend["year"]}"
    if today==f_birthday:
        name=friend["name"]
        email=friend["email"]
        return name,email
    
    

#--------------------------- reading letters ----------------------------------------------#


from  random import choice


placeholder="[NAME]"
def choose_letter():
    letters=["l1.txt","l2.txt","l3.txt"]
    lettre=choice(letters)
    return lettre



def whrite_letter(name):
   letter=choose_letter()
   with open(f"./day32/letters/{letter}")as file:
    model=file.read()
    model=model.replace(placeholder,name)
    return model

#-------------------------------------- main -------------------------------------- #

def main():
    
    nom,email=get_friend()
    model=whrite_letter(nom)
    send_email(email,model)
    
main()    