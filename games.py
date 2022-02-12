import pandas as pd
import time
import matplotlib.pyplot as plt
df = pd.read_csv('android-games.csv')

mycolors=['#17A589','#F5B7B1','#D7BDE2','#A9CCE3','#A3E4D7','#FAD7A0','#AEB6BF']
while True:
    print("\n> > > > > > > > > > > > ANDROID GAMES < < < < < < < < < < < <  ")
    print("1. Overview ")
    print("2. Year wise data")
    print("3. Paid/Free games")
    print("4. Year wise ranking")
    print("5. Game category")
    print("6. Number of installs")
    print("7. Stars provided ")
    print("8. Exit the menu")
    choice = int(input("\nEnter your choice : "))

    if(choice==1):
        print("------------------------------------------------------")
        print("The dataset have" ,len(df) , "number of datas")
        print("It contains data from", min(df['year']),"to", max(df['year']))
        print("From each year top", max(df['rank']), "games have been taken")
        print("------------------------------------------------------")
        print(df)

    if(choice==2):
        input_year= int(input("\nEnter the year for which data you want(2005-2021) : "))
        df1 = df[(df.year== input_year)]
        print(df1)

    if(choice==3):
        overall=len(df)
        paid = len(df[(df['price']>0)])
        free = len(df[(df['price']==0)])
        paid_value=(paid/overall)*100
        paid_value_format="{:.2f}".format(paid_value)
        unpaid_value=(free/overall)*100
        unpaid_value_format="{:.2f}".format(unpaid_value)
        print("------------------------------------------------------")
        print("The dataset have", len(df), "number of datas")
        print("Of which",paid, ",which is",paid_value_format,"% is PAID")
        print("And", free,"which is",unpaid_value_format,"% is UNPAID")
        p=int(input("\nPRESS 1 TO PLOT THE PIE CHART FOR THE SAME : "))
        print("------------------------------------------------------")
        if(p==1):
            df['price'].value_counts().plot.pie(label="FREE")
            plt.legend()
            plt.show()

    if(choice==4):
        print("1. Rank according to year")
        print("2. Growth according to year and rank")

        choice1=int(input("Enter the choice : "))

        if(choice1==1):
            print("------------------------------------------------------")
            print("We have 2005-2021 data \nAnd in that period all the games have different ranks")
            rank=int(input("\nEnter which rank(1-100) you want to see : "))
            print("------------------------------------------------------")
            print("\nBELOW IS THE LIST OF GAMES OF RANK: ",rank)
            df1=df[df['rank']==rank]
            print(df1[['title','year']])

        if(choice1==2):
            rank=int(input("\nEnter the rank(1-100) : "))
            year=int(input("Enter the year(2005-2021) : "))
            df1=df[df['rank']==rank]
            df2= df1[df1['year'] == year]
            df3=df2[['growth (30 days)','growth (60 days)']]
            df3.plot.bar()
            plt.show()
            
    if (choice==5):
        print("------------------------------------------------------")
        print("Below is the list of Categories in which game is divided :\n")
        print(df['category'].value_counts())
        time.sleep(3)
        df['category'].value_counts().plot.pie()
        plt.show()
        

    if(choice==6):
        print("------------------------------------------------------")
        print("Below is the Number of Installs :\n")
        print(df['installs'].value_counts())
        df['installs'].value_counts().plot.barh(color=mycolors)
        plt.show()

    if(choice==7):
        rank=int(input("\nEnter the rank(1-100) : "))
        year=int(input("Enter the year(2005-2021) : "))
        df1=df[df['rank']==rank]
        df2= df1[df1['year'] == year]
        df3=df2[['5 star ratings','4 star ratings','3 star ratings','2 star ratings','1 star ratings']]
        print("------------------------------------------------------")
        print("For each game numbers of peoples have given stars to them\n")
        print(df3)
        df3.plot.bar(color=mycolors)
        plt.show()
        
    if(choice == 8):
        print("----------------------THANK YOU !-----------------------")
        break;
