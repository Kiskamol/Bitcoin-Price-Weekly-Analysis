import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import tkinter as tk
from pandas import *
from statistics import *
import datetime 
from forex_python.bitcoin import BtcConverter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser


b = BtcConverter()
Mainwindow = Tk()

###Timedates###
today = datetime.date.today()
today_withtime = datetime.datetime.today()
lastweek = today - datetime.timedelta(weeks=1)
two_weeks_ago = lastweek - datetime.timedelta(weeks=1)
three_weeks_ago = two_weeks_ago - datetime.timedelta(weeks=1)
four_weeks_ago = three_weeks_ago - datetime.timedelta(weeks=1)
five_weeks_ago = four_weeks_ago - datetime.timedelta(weeks=1)

###Btc Price previous time###
today_btc_price = b.get_latest_price('USD')
today_btc_price_2 = round(today_btc_price,2)
lastweek_btc_price = b.get_previous_price('USD',lastweek)
lastweek_btc_price_2 = round(lastweek_btc_price ,2)
twoweeksago_btc_price = b.get_previous_price('USD',two_weeks_ago)
twoweeksago_btc_price_2 = round(twoweeksago_btc_price,2)
threeweeksago_btc_price = b.get_previous_price('USD',three_weeks_ago)
threeweeksago_btc_price_2 = round(threeweeksago_btc_price,2)
fourweeksago_btc_price = b.get_previous_price('USD',four_weeks_ago)
fourweeksago_btc_price_2 = round(fourweeksago_btc_price,2)
fiveweeksago_btc_price = b.get_previous_price('USD',five_weeks_ago)

###Btc Price now in main menu###
change = ((today_btc_price - lastweek_btc_price)/today_btc_price)*100
percen = round(change,2)
if change >0  :
    text = ' ▲ '+str(percen)+"%"
elif change <0 :
    text = ' ▼ '+str(percen)+"%"
else :
    text = 'N/A'


def Btc_Price ():
    change_2 = ((lastweek_btc_price - twoweeksago_btc_price)/lastweek_btc_price)*100
    percent = round(change_2,2)
    if change_2 >0  :
        text_2 = ' ▲ '+str(percent)+"%"
    elif change_2 <0 :
        text_2 = ' ▼ '+str(percent)+"%"
    else :
        text_2 = 'N/A'
    change = (( twoweeksago_btc_price - threeweeksago_btc_price)/twoweeksago_btc_price)*100
    percent = round(change,2)
    if change >0  :
        text_3 = ' ▲ '+str(percent)+"%"
    elif change <0 :
        text_3 = ' ▼ '+str(percent)+"%"
    else :
        text_3 = 'N/A'
    change = (( threeweeksago_btc_price - fourweeksago_btc_price)/threeweeksago_btc_price)*100
    percent = round(change,2)
    if change >0  :
        text_4 = ' ▲ '+str(percent)+"%"
    elif change <0 :
        text_4 = ' ▼ '+str(percent)+"%"
    else :
        text_4 = 'N/A'
    change_5 = (( fourweeksago_btc_price - fiveweeksago_btc_price)/fourweeksago_btc_price)*100
    percent = round(change,2)
    if change_5 >0  :
        text_5 = ' ▲ '+str(percent)+"%"
    elif change_5 <0 :
        text_5 = ' ▼ '+str(percent)+"%"
    else :
        text_5 = 'N/A'
    btc_price = "• ₿ Price Now ("+ str(today)+") : "+str(today_btc_price_2 )+' $'+text+"\n"+"• ₿ Price Lastweek ("+ str(lastweek)+") : "+str(lastweek_btc_price_2)+' $'+text_2+'\n'+"• ₿ Price Last 2 week ("+ str(two_weeks_ago)+") : "+str(twoweeksago_btc_price_2)+' $'+text_3+'\n'+"• ₿ Price Last 3 week ("+ str(three_weeks_ago)+") : "+str(threeweeksago_btc_price_2)+' $'+text_4
    label11 = tk.Label(Mainwindow, text= btc_price,font=('helvetica', 10))
    canvas1.create_window(180, 235, window=label11)

def Avg_BtcPrice():
    Btc_Price = (lastweek_btc_price,twoweeksago_btc_price,threeweeksago_btc_price,today_btc_price)
    Avg_BtcPrice = mean(Btc_Price)
    Avg_BtcPrice_2 = round(Avg_BtcPrice,2)
    text = "• Average Bitcoin (₿) Prices in Month "+str(Avg_BtcPrice_2)+' $'
    label1 = tk.Label(Mainwindow, text= text , font=('helvetica', 10))
    canvas1.create_window(150, 340, window=label1)
    
def Min_Max_BtcPrice():
    Btc_Price = (lastweek_btc_price,twoweeksago_btc_price,threeweeksago_btc_price,today_btc_price)
    Max_BtcPrice = max(Btc_Price)
    Max_BtcPrice_2 = round(Max_BtcPrice,2)
    Min_BtcPrice = min(Btc_Price)
    Min_BtcPrice_2 = round(Min_BtcPrice,2)
    Diff = ((Max_BtcPrice - Min_BtcPrice)/Min_BtcPrice)*100
    Diff_2 = round(Diff,2)
    text = " (▲"+str(Diff_2)+" %)"
    text_show = "• Maximum Bitcoin (₿) Price in Month "+str(Max_BtcPrice_2)+' $'+text+"\n"+"• Minimum Bitcoin (₿) Price in Month "+str(Min_BtcPrice_2)+' $'
    label1 = tk.Label(Mainwindow, text= text_show,font=('helvetica', 10))
    canvas1.create_window(180, 430, window=label1)
    
def Btc_graph(): 
    data2 = {'Weeks': ['Now',str(lastweek),str(two_weeks_ago),str(three_weeks_ago),str(four_weeks_ago)],'Bitcoins Price': [today_btc_price,lastweek_btc_price,twoweeksago_btc_price,threeweeksago_btc_price,fourweeksago_btc_price] }
    df2 = DataFrame(data2,columns=['Weeks','Bitcoins Price'])
    Mainwindow= tk.Tk()
    figure2 = plt.Figure(figsize=(6,5))
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, Mainwindow)
    line2.get_tk_widget().pack(fill=tk.BOTH)
    df2 = df2[['Weeks','Bitcoins Price']].groupby('Weeks').sum()
    df2.plot(kind='line', ax=ax2, color='blue',marker='o', fontsize=10)
    ax2.set_title('Bitcoin Prices in Month (4 weeks)\n Line Chart')

def open_web_btc():
    new = 1
    url = "https://news.bitcoin.com/"
    webbrowser.open(url,new=new)

def open_web_bitkub():
    new = 1
    url = "https://www.bitkub.com/"
    webbrowser.open(url,new=new)

def show_price():
    eur = b.get_latest_price('EUR')
    thb = b.get_latest_price('THB')
    jpy = b.get_latest_price('JPY')
    krw = b.get_latest_price('KRW')
    text = 'EUR : '+str(eur)+' €'+'\n'+'THB : '+str(thb)+' ฿'+'\n'+'JPY : '+str(jpy)+' ¥'+'\n'+'KRW : '+str(krw)+' ₩'
    label4 = tk.Label(Mainwindow, text= text,font=('helvetica', 10))
    canvas1.create_window(450, 220, window=label4)

canvas1 = tk.Canvas(Mainwindow, width = 600, height = 500)
canvas1.config (bg ='goldenrod')
canvas1.pack()   

btc_price_today = "₿ Prices Now ("+ str(today)+") : "+str(today_btc_price_2)+' $'+text
label1 = tk.Label(Mainwindow, text= btc_price_today,font=('helvetica', 12),fg = 'gold2',bg='black')
canvas1.create_window(300, 110, window=label1)

label1 = tk.Label(Mainwindow, text='BITCOIN (₿) Price Weekly Analysis')
label1.config(font=('helvetica', 16),fg='black',bg='goldenrod')
canvas1.create_window(290, 40, window=label1)

label2 = tk.Label(Mainwindow, text=today_withtime)
label2.config(font=('helvetica', 14),fg='black',bg='goldenrod')
canvas1.create_window(290, 70, window=label2)

label3 = tk.Label(Mainwindow, text='For ₿ Investor ')
label3.config(font=('helvetica', 14),bg = 'white')
canvas1.create_window(450, 340, window=label3)
          
Mainwindow.title("BITCOIN ( ₿ ) Price Weekly Analysis")

button_1 = tk.Button(text='Bitcoin (₿) Prices\n (In the past 4 weeks)',command = Btc_Price ,fg = 'gold2',bg='black', font=('helvetica', 10,'bold'))
canvas1.create_window(130, 170, window=button_1)

button_2 = tk.Button(text='Average Bitcoin (₿) Prices \n (In the past 4 weeks)',command = Avg_BtcPrice,fg = 'gold2',bg='black', font=('helvetica', 10, 'bold'))
canvas1.create_window(130, 300, window=button_2)

button_3 = tk.Button(text='Max & Min Bitcoin (₿) Prices \n (In the past 4 weeks)',command = Min_Max_BtcPrice,fg = 'gold2',bg='black', font=('helvetica', 10, 'bold'))
canvas1.create_window(130, 380, window=button_3)

button_4 = tk.Button(text='Bitcoin (₿) Prices Now in Others Currency ',command = show_price,fg = 'gold2',bg='black', font=('helvetica',10, 'bold'))
canvas1.create_window(450, 160, window=button_4)

button_5 = tk.Button(text='Bitcoin (₿) Prices Line Chart ',command = Btc_graph,fg = 'gold2',bg='black', font=('helvetica',10, 'bold'))
canvas1.create_window(450, 290, window=button_5)

button_6 = tk.Button(text='BITCOIN.COM' , command = open_web_btc , bg='white', fg='DarkGoldenrod4', font=('helvetica', 10, 'bold'))
canvas1.create_window(450, 430, window=button_6)

button_7 = tk.Button(text='BITKUB.COM',command = open_web_bitkub , bg='white', fg='DarkGoldenrod4', font=('helvetica', 10, 'bold'))
canvas1.create_window(450, 390, window=button_7)

button0 = tk.Button(text='Quit',command= Mainwindow.quit, bg='red', fg='black', font=('helvetica', 10, 'bold'))
canvas1.create_window(300, 480, window=button0)
Mainwindow.mainloop()

