from tkinter import *
from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageTk
def url_create(kasutajasisend):
    server=valik.get()
    if server=="EUW":
        url_põhi="https://euw.op.gg/multi/query="
    elif server=="NA":
        url_põhi = "https://na.op.gg/multi/query="
    elif server=="KR":
        url_põhi = "https://www.op.gg/multi/query="
    elif server=="EUNE":
        url_põhi = "https://eune.op.gg/multi/query="
    elif server=="OCE":
        url_põhi = "https://oce.op.gg/multi/query="
    elif server=="RU":
        url_põhi = "https://ru.op.gg/multi/query="
    elif server=="TR":
        url_põhi = "https://tr.op.gg/multi/query="
    elif server=="LAN":
        url_põhi = "https://lan.op.gg/multi/query="
    elif server=="LAS":
        url_põhi = "https://las.op.gg/multi/query="
    elif server=="BR":
        url_põhi = "https://br.op.gg/multi/query="
    else:
        url_põhi = "https://euw.op.gg/multi/query="


# placeholder copypasta
    lobby = kasutajasisend
    # nimed eraldada
    nimekiri=lobby.split(".")
    puhastatud=[]
    for elem in nimekiri:
        try:
            nimi=elem.replace("joined the room", "")
            nimi=nimi.replace("\n","")
            nimi=nimi.strip()
            nimi=nimi.replace(" ","")
            nimi=nimi.lower()
            puhastatud.append(nimi)
        except:
            pass
    puhastatud=puhastatud[0:5]
    #print(puhastatud)
    #print(nimekiri)

    # urli loomine
    muudetud=[]
    for elem in puhastatud:
        elem = elem + "%2C"
        muudetud.append(elem)
    #print(muudetud)
    kasutajanimed_päring="".join(muudetud)
    #print(sõne)
    päringu_url=url_põhi+kasutajanimed_päring
    print(päringu_url)
    return päringu_url

## nimede saamine
def kraapimine(lehe_url):
    headers = {'User-Agent': 'My User Agent 1.0','From': 'youremail@domain.com'}  # This is another valid field

    url = requests.get(lehe_url, headers=headers)
    soup = BeautifulSoup(url.content,'html.parser')

    andmed = soup.find_all('li', class_="multi2__item")
    for elem in andmed:
        try:
            nimi=elem.select_one(".name")
            nimi=nimi.get_text().strip()
            champion_usernames.append(nimi)
        except:
            champion_usernames.append("N/A")
    #print("Nimed:",champion_usernames)

    for elem in andmed:
        try:
            nimi=elem.select_one(".lp")
            nimi=nimi.get_text().strip()
        
            listina=nimi.split(" ")
            rank=listina[0]

            if rank=="Level":
                pildinimi="ikoonid\\unranked.png"
                pildid.append(pildinimi)
            elif rank=="Iron":
                pildinimi="ikoonid\\iron.png"
                pildid.append(pildinimi)
            elif rank=="Bronze":
                pildinimi="ikoonid\\bronze.png"
                pildid.append(pildinimi)
            elif rank=="Silver":
                pildinimi="ikoonid\\silver.png"
                pildid.append(pildinimi)
            elif rank=="Gold":
                pildinimi="ikoonid\\gold.png"
                pildid.append(pildinimi)
            elif rank=="Platinum":
                pildinimi="ikoonid\\platinum.png"
                pildid.append(pildinimi)
            elif rank=="Diamond":
                pildinimi="ikoonid\\diamond.png"
                pildid.append(pildinimi)
            elif rank=="Master":
                pildinimi="ikoonid\\master.png"
                pildid.append(pildinimi)
            elif rank=="Grandmaster":
                pildinimi="ikoonid\\grandmaster.png"
                pildid.append(pildinimi)
            elif rank=="Challenger":
                pildinimi="ikoonid\\challenger.png"
                pildid.append(pildinimi)
            else:
                pildinimi = "ikoonid\\unranked.png"
                pildid.append(pildinimi)
        except Exception:
            pass
        champion_ranks.append(nimi)
    #print("Pildid:",pildid)
    #print("Rankid:",champion_ranks)
    
    
    for elem in andmed:
        nimi=elem.select(".most-position > i")
        try:
            nimi=str(nimi[0])
            nimi=nimi.lstrip("""<i class="most-position__icon most-position__icon""").rstrip(""""></i>""")
        except :
            nimi="-"
        
        champion_positions.append(nimi)
    #print("Mainroled:",champion_positions)
    
    for elem in andmed:
        try:
            nimi=elem.select_one(".winratio")
            nimi=nimi.get_text().strip()
        except:
            nimi="-"
        
        champion_winratios.append(nimi)
    #print("Winratio:", champion_winratios)
    for elem in andmed:
        try:
            try:
                nimi = elem.find('div', class_="win-streak win-streak--wins")
                nimi = nimi.get_text().strip()
            except:
                nimi = elem.find('div', class_="win-streak win-streak--losses")
                nimi = nimi.get_text().strip()
        except:
            nimi = "-"

        champion_streaks.append(nimi)
    #print("Winstreakid:", champion_streaks)
    
class Üleminerida(Frame):
    def __init__(self, master, nimi, pilt, rank, position, winratio, streak):
        Frame.__init__(self, master, bd=5, relief='raised')
        Label(self, text=nimi, width=17, anchor='e', padx=10, pady=10, font=("Arial",16 , "bold"),background="#b1fcf9").grid(row=0,column=0, rowspan=2)

        Label(self, text=pilt).grid(row=0,column=2)
        
        Label(self, text=rank,font=("Arial",14 , "bold"), width=19).grid(row=0, column=3)
        Label(self, text=position,font=("Arial",14 , "bold"), width=13).grid(row=0, column=4)
        Label(self, text=winratio,font=("Helvetica",14 , "bold"), width=9).grid(row=0, column=5)
        Label(self, text=streak,font=("Helvetica",14 , "bold"), width=19).grid(row=0, column=6)


class Tabelisisu(Frame):
    def __init__(self, master, nimi,pilt, rank, position, winratio, streak):
        Frame.__init__(self, master, bd=5, relief='raised')
        Label(self, text=nimi, width=17, anchor='c',font=("Arial",16 , "bold"), padx=10,background="#b1fcf9", pady=10)\
            .grid(row=0, column=0,rowspan=2)
        ikoon = Image.open(pilt)
        rankiikoon = ImageTk.PhotoImage(ikoon)

        label = Label(self, image=rankiikoon)
        label.ikoon = rankiikoon
        label.grid(row=0, column=2)

        Label(self, text=rank, width=18,font=("Helvetica",13)).grid(row=0, column=3)
        Label(self, text=position,font=("Helvetica",16,"bold"),foreground="black", width=12).grid(row=0, column=4)

        try:
            if int(winratio[:(len(winratio)-1)])<=49:
                Label(self, text=(winratio,"!"), font=("Arial",17,"bold"),foreground="#de4646",width=7).grid(row=0, column=5)
            elif 50<=int(winratio[:(len(winratio)-1)])<=59:
                Label(self, text=winratio, font=("Arial", 17, "bold"), foreground="#a9a9a9", width=7).grid(row=0,column=5)
            elif 69>=int(winratio[:(len(winratio)-1)])>=60:
                Label(self, text=winratio, font=("Arial", 17, "bold"), foreground="#77e098", width=7).grid(row=0, column=5)
            elif (int(winratio[:(len(winratio)-1)]))>=70:
                Label(self, text=winratio, font=("Arial", 17, "bold"), foreground="#f0ae58", width=7).grid(row=0, column=5)
            else:
                Label(self, text=winratio, font=("Arial", 17, "bold"), foreground="#a9a9a9", width=7).grid(row=0, column=5)
        except:
            Label(self, text=winratio, font=("Arial", 14, "bold"), foreground="#a9a9a9", width=7).grid(row=0, column=5)

        try:
            streak=streak.strip().split(" ")
            if streak[2]=="win":
                Label(self, text=streak,foreground="#77e098", font=("Helvetica", 16 ,"bold"),width=19).grid(row=0, column=6)
            elif streak[2]=="loss":
                Label(self, text=streak,foreground="#de4646",font=("Helvetica",16,"bold"), width=19).grid(row=0, column=6)
        except:
            Label(self, text=streak, font=("Arial", 14, "bold"), foreground="#a9a9a9", width=19).grid(row=0, column=6)


def päring():
    tekst_kastist = sisend.get("1.0",'end-1c')
    link = url_create(tekst_kastist)
    kraapimine(link)    


    newWindow = Toplevel(root)
    newWindow.configure(background="lightblue") 
    newWindow.title("Team")
    newWindow.geometry("1030x520")
    newWindow.resizable(0, 0)
    canvas = Canvas(newWindow, width=1, height=1)
    taustapilt = ImageTk.PhotoImage(Image.open("pildid\\background.jpg"))

    canvas.create_image(0, 0, anchor=NW, image=taustapilt)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    #ikoon
    ikoonipilt = Image.open("pildid\\ikoon.ico")
    ikoonipilt = ImageTk.PhotoImage(ikoonipilt)
    newWindow.iconphoto(False, ikoonipilt)
    #print(champion_usernames)

    Üleminerida(newWindow,pealkirjad[0],pealkirjad[1],pealkirjad[2],pealkirjad[3],pealkirjad[4],pealkirjad[5]).pack(expand=True, fill='x')
    try:
        for i in range(0,5):
            Tabelisisu(newWindow,champion_usernames[i],pildid[i],champion_ranks[i], champion_positions[i], champion_winratios[i], champion_streaks[i]).pack(expand=True, fill='x')
    except:
        pass
    algseis()
def algseis():
    #puhastus()
    global champion_usernames
    global champion_ranks
    global pildid
    global champion_positions
    global champion_winratios
    global champion_streaks


    champion_usernames=[]
    champion_ranks=[]
    pildid=[]
    champion_positions=[]
    champion_winratios=[]
    champion_streaks=[]
    sisend.delete('1.0', END)

#       Järjendid

pealkirjad=["Summoner Name","","Ranked Solo/Duo Rank","Main Position","Winratio","Last games"]
champion_usernames=[]
pildid=[]
champion_ranks=[]
champion_positions=[]
champion_winratios=[]
champion_streaks=[]

################################ 
#             GUI              #
################################

root=Tk()
root.title("Team Checker")
root.geometry("700x400")
root.resizable(0,0)
root.configure(background="lightblue")
root.option_add("*Font", "Arial")

#akna ikoon
ikoonipilt=Image.open("pildid\\ikoon.ico")
ikoonipilt=ImageTk.PhotoImage(ikoonipilt)
root.iconphoto(False,ikoonipilt)

#background
canvas=Canvas(root,width=1,height=1)
taustapilt = ImageTk.PhotoImage(Image.open("pildid\\taustakas2.jpg"))

canvas.create_image(0,0,anchor=NW,image=taustapilt)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

#sisend
sisend = Text(root, width=26, height=5, wrap=WORD, foreground="#7995bf",font=("Arial",12),borderwidth=10,background="#312e41")
sisend.pack(pady=20)

#GUI widgets

valik= StringVar(root)
valik.set("EUW")
menüü=OptionMenu(root,valik,"EUW","EUNE","NA","KR","OCE","RU","TR","LAN","LAS","BR")
menüü.config(width=6,height=1,font=("Helvetica",14,), foreground="#7995bf",background="#312e41",borderwidth=4,highlightthickness=0,padx=0,pady=0)
menüü.pack()

#nupp1
nupupilt1=Image.open("pildid\\searcher.jpg")
nupupilt1=nupupilt1.resize((75,75),Image.ANTIALIAS)
fotonupupilt1=ImageTk.PhotoImage(nupupilt1)

searchbutton = Button(root,fg = '#37d3ff',
                      bg = '#001d26',
                      bd =  10,  image=fotonupupilt1, command = päring,borderwidth=-5)
searchbutton.pack(pady=10)



#resetnupp
nupupilt2=Image.open("pildid\\reset.jpg")
nupupilt2=nupupilt2.resize((40,40),Image.ANTIALIAS)
fotonupupilt2=ImageTk.PhotoImage(nupupilt2)

resetbutton = Button(root,fg = '#37d3ff',
                      bg = '#001d26',
                      bd =  10,  image=fotonupupilt2, command=algseis,borderwidth=0)
resetbutton.pack(pady=10)

root.mainloop()
