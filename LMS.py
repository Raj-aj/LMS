import os,logzero,keyboard,time
import mysql.connector as mc
from getpass import getpass
from winsound import Beep
from pyttsx3 import speak
import winsound


def beep(n):
    for i in range(n):
        Beep(4000,400)







#Best Configuration for terminal
def terminal_look():
    os.system('title [ Library Management System ] [ Aj_Indudstires ]')
    os.system('color 07')
    keyboard.press_and_release('alt+enter');time.sleep(1)     #Enter Full Screen  #to focus on work only 
    welcome_msg();time.sleep(2);os.system('cls')
    
    print('\n'+'─'*os.get_terminal_size()[0])   #this raise [ValueError: bad file descriptor] in python shell
    print('Library Management System'.center(os.get_terminal_size()[0],' '))
    print('─'*os.get_terminal_size()[0])
    # speak('Welcome, To Library Mangement System. You will be shown a list of commands you can use in the program.')       #Assistant
    #do you want an assistant [Yes] or [No]






def welcome_msg():
    
    lms_title='''



                                 ,,                                                                  
    `7MMF'     A     `7MF'     `7MM                                                MMP""MM""YMM      
      `MA     ,MA     ,V         MM                                                P'   MM   `7      
       VM:   ,VVM:   ,V .gP"Ya   MM  ,p6"bo   ,pW"Wq.`7MMpMMMb.pMMMb.  .gP"Ya           MM  ,pW"Wq.  
        MM.  M' MM.  M',M'   Yb  MM 6M'  OO  6W'   `Wb MM    MM    MM ,M'   Yb          MM 6W'   `Wb 
        `MM A'  `MM A' 8M""""""  MM 8M       8M     M8 MM    MM    MM 8M""""""          MM 8M     M8 
         :MM;    :MM;  YM.    ,  MM YM.    , YA.   ,A9 MM    MM    MM YM.    ,          MM YA.   ,A9 
          VF      VF    `Mbmmd'.JMML.YMbmd'   `Ybmd9'.JMML  JMML  JMML.`Mbmmd'        .JMML.`Ybmd9'  
                                                                                                     
                                                                                                     
                                                                                             
                    mmmmm                                               mmmmm 
                    MM                                                     MM         
                    MM        `7MMF'      `7MMM.     ,MMF' .M"""bgd        MM 
                    MM          MM          MMMb    dPMM  ,MI    "Y        MM 
                    MM          MM          M YM   ,M MM  `MMb.            MM 
                    MM          MM          M  Mb  M' MM    `YMMNq.        MM 
                    MM          MM      ,   M  YM.P'  MM  .     `MM        MM 
                    MM          MM     ,M   M  `YM'   MM  Mb     dM        MM 
                    MM        .JMMmmmmMMM .JML. `'  .JMML.P"Ybmmd"         MM 
                    MM                                                     MM 
                    MMmmm                                               mmmMM 

    _   ____ _____________   _   _  ______  ______________  ______  ____   _____   _____________  _ 
    |   ||__]|__/|__||__/ \_/    |\/||__||\ ||__|| __|___|\/||___|\ | |    [__  \_/ [__  | |___|\/| 
    |___||__]|  \|  ||  \  |     |  ||  || \||  ||__]|___|  ||___| \| |    ___]  |  ___] | |___|  | 
            

'''
    print(lms_title)

log_in_chance=3
def connect_to_DB():  #Connecting the database to the python program
    global mydb,log_in_chance,cur
    while log_in_chance>0:
        try:
            print('\n█Your mysql details are required')
            print()
            user_=input(  '        ┌──User_Name : ').strip() ;print('        ▓')
            pass_=getpass('        └───Password : ').strip()
            mydb=mc.connect(host='localhost',user=user_,password=pass_,) 
        
            os.system('color 27');os.system('cls');print('\n'*10)
            print('You are most welcome'.title().center(os.get_terminal_size()[0],' '));time.sleep(0.5)
            winsound.PlaySound("LMS.wav", winsound.SND_ASYNC)
            cur=mydb.cursor(buffered=True)

            databses_structure=open("final.sql").read()  #multi=True this contains
            # print(databses_structure)
            # os.system('pause')
            # cur.execute(databses_structure)
            # cur.execute(databses_structure,multi=True)
            cur.execute('use _a;') #name of the database


            # cur.execute(r'\source "all.sql"') #create required database and tables
            # cur.execute('use _a')
            
            
            
            
            os.system('cls')
            log_in_chance=0
        except:  #wrong details 
            #take a picture by running another script in background
            try:
                # os.system('echo off & python capture.pyw')
                pass
            except:
                print(os.getcwd())
                print('Capture could not be done')
                os.system('pause')


            log_in_chance-=1
            if log_in_chance==0:
                os.system('cls')
                for i in range(5):
                    os.system('color 47')
                    beep(1);print('\n\n')
                    print('You are not a valid user'.title().center(os.get_terminal_size()[0])) #10 times beep at full volume
                time.sleep(1);quit()
            else:
                os.system('cls & color 17')
                for i in range(2):
                    beep(1);print('\n\n')
                    print('Incorrect User_Name and Password. Try again !'.center(os.get_terminal_size()[0],' '))
            
            time.sleep(1)
            os.system('cls & color 07')
            connect_to_DB()




print()
def command_lists():            #Command list
    
    print('''
        +--C֍MMANDS------------------------------------+
        | »[C] : See these commands again              |
        +----------------------------------------------+
        |   [S] : Search Books                         |
        |   [1] : Issue/Lend Books                     |
        |   [2] : Submit/Receive Books                 |
        |   [3] : Add Books     [A]                    |
        |   [4] : Update Books  [U]                    |
        |   [5] : Delete Books  [D]                    |
        |   [F] : Fine Details  [F]                    |
        |   [T] : Total no. of books                   |
        |   [X] : Close the Program [ CTRL+C ]         |
        | [CLS] : Clear Screen [clear]                 |
        | [ALL] : List of all books in library         |
        +----------------------------------------------+
        | Online_Book | Art | Devs | Kuch  | Help | Aj |
        +----------------------------------------------+
    ''')
    




def search_book():
    print('''
    +------------------------------+
    |   Search and Filter Books    |
    +------------------------------+
    ''')

    def sql_search_query(column):
        print()
        cur.execute(f'select Book_name,book_id,available from books where {column} like "%{search}%"')
        slno=1
        for i in cur:
            if i[2]=='yes':
                print('   ',str(slno).rjust(2,' ')+'. '+i[0].title().ljust(30,'.'),'Book ID :',(i[1]),', Avialable' ) #showing the list of similar books
            else:
                print('\033[1;31;40m   ',str(slno).rjust(2,' ')+'. '+i[0].title().ljust(30,'.'),'Book ID :',(i[1]),', Not Available \033[0;37;40m')
            slno+=1

        if slno==1:
            print('\033[1;31;40mNo Book Found!\033[0;37;40m')
        
        print()
        print('-'*(os.get_terminal_size()[0]))

    while True:
        search=input('\nSearch Books : ').strip().lower()
        search=' '.join(search.split())
        

        if search=='':                          #cancel book search
            print('Searching Book(s) Canceled')
            break #run_command()
        elif search.isdigit():                  #book search by Book ID
            sql_search_query(column='book_id')
        # elif search.isalpha():                  #book search by Book Name
        #     sql_search_query(column='book_name')
        elif search.startswith('author'):
            search=search.split('-')[-1]
            sql_search_query(column='author')
        elif search.startswith('publisher'):
            search=search.split('-')[-1]
            sql_search_query(column='publisher')
        elif search.startswith('subject') or search.startswith('sub'):
            search=search.split('-')[-1]
            sql_search_query(column='subject')
        elif search.startswith('class'):
            search=search.split('-')[-1]
            sql_search_query(column='class')
        elif search.startswith('language') or search.startswith('lang'):
            search=search.split('-')[-1]
            sql_search_query(column='language')
        else:
            sql_search_query(column='book_name')


def book_update():
    print('''
    +---------------------+
    |   Updating Books    |
    +---------------------+
    ''')
    while True:
        update=input('\nEnter Book ID : ')
        if update=='':         # exit from this book updating section
            print('Updating Book(s) Canceled');break
        elif update.isdigit(): # continue if the input is in digit(s)
            
            column='Book_Name Class Subject Language Publisher Author'.split()
            cur.execute(f'select book_id,book_name,class,subject,language,publisher,author from books')
            global current_data
            current_data=[] #if book_id is vaild its data will be stored here
            
            book_found=False
            for detail in cur:
                if int(update)==detail[0]:  #check if book id exists
                    cur.execute(f'select book_name,class,subject,language,publisher,author from books where Book_ID="{update}"')
                    for i in cur:
                        current_data.extend(i) #storing the book details in a list
                        book_found=True;break  #book is found and break the loop
                else:
                    pass
            if book_found: #if the book_found is true this block will run
                print('                                            Enter New Details')
                print('                                            ─────────────────')
                new_record=[]
                #this below block is for better appereance while update the records
                for i in range(len(column)):
                    if len(str(current_data[i]))<18:
                        change=input(f'█ {i+1}.{column[i]} '.ljust(15,'-')+f' ["{current_data[i]}"] : '.rjust(29,'-')).strip().title()
                        
                        if change=='':
                            new_record.append(current_data[i]) #storing old data when no input is given
                        else:
                            new_record.append(change) #storing new data
                    
                    else:
                        change=input(f'█ {i+1}.{column[i]} '.ljust(15,'-')+f' ["{current_data[i][0:18]}..."] : '.rjust(29,'-')).strip().title()
                        if change=='':
                            new_record.append(current_data[i]) #storing old data when no input is given
                        else:
                            new_record.append(change) #storing new data
                        
                print()
                
                if current_data!=new_record: #asking for the confirmation to update the book details
                    if str(new_record[1]).isdigit(): #Class and Quantity field should be digit(s)
                        commit=input('\nSure about the changes? [y/n] : ').lower()
                        
                        if commit in 'y yes'.lower().split():
                            update_query=f"update books set \
                                        book_name='{new_record[0]}',class={new_record[1]},subject='{new_record[2]}',language='{new_record[3]}',\
                                        publisher='{new_record[4]}',author='{new_record[5]}',Last_Update_On =CURRENT_TIMESTAMP \
                                        where Book_ID={int(update)}"
                            
                            cur.execute(update_query)
                            cur.execute('commit')
                            print('Changes Saved, Sucessfully!')  #run the sql update and commit 
                            
                        elif commit in 'n no'.lower().split():
                            print('Changes Not Saved')
                        else:
                            print('Changes Not Saved')
                    else:
                        print('Changes Not Saved\nPlease enter only numeric value in the Class field.')
                    
                else:
                    print('No Changes Made')

                print() #space

            else:
                print('There is no book with your given Book ID')
            
        else:
            print('\t\t\t\t\033[1;31;40m*Enter the digits only*\033[0;37;40m')
            pass





def t():
    #colorful details
    cur.execute('select count(distinct(Book_Name)) from books')
    total_books=''
    for i in cur:
        total_books=i[0]
        cur.execute('select count(*) from books')
        for j in cur:
            different_type=j[0]
        
            print(f' \033[0;37;41m Total Books \033[0;37;40m\033[0;30;47m {total_books} \033[0;37;40m  \033[0;37;41m Total Quantity \033[0;30;47m {different_type} \033[0;37;40m')
    

def current_borrowers():
    cur.execute('update book_borrowers set total_days=datediff(CURRENT_TIMESTAMP,borrowed_date)   where `submit_date`=0;')
    cur.execute('select borrower_no,Borrowed_book_id,name,datediff(CURRENT_TIMESTAMP,borrowed_date) from book_borrowers where submit_date=0;')
    
    slno=1
    print('Slno'.rjust(8,' '),'Borrower_No'.rjust(15,' '),'Book_ID'.rjust(15,' '),'Borrower\'s Name'.rjust(19,' '),'Total Days'.rjust(24,' '),'Late Fine'.rjust(13,' '))
    print(' ','-'*100)
    for i in cur:
        print((str(slno)+'.').rjust(8,' '),str(i[0]).rjust(14,' '),str(i[1]).rjust(15,' '),' '*5,(str(i[2]).ljust(28,' '))[:28],str(i[3]).rjust(9,' '),str(i[3]*2).rjust(13,' '))
        print(' ','-'*100)
        slno+=1



def lend_book(): #admission no./mobile no. and book id
    print('''
    +---------------------+
    |   Issueing Books    |
    +---------------------+
    ''')
    while True:
        #asking for [Book ID] and [Admission no. or Mobile no.]
        global available
        available=False
        found=False
        while True: #taking book id and looking for it in database
            global id
            id  = input('\n\tBook ID : ').strip()
            if id=='':
                print('\tIssueing book(s) exit')
                break
            elif id.isdigit():
                if int(id)>0:
                    id=int(id)

                    #check for book validation here
                    cur.execute('select book_id from books')
                    for book_id in cur:     #iteration of book ids
                        if id in book_id:   #checking for book id
                            found=True
                            break           #this breaks for loop
                    
                    if not found:
                        print('\t\t\t\t\033[1;31;40mNo book found with given ID \033[0;37;40m')
                        available=False
                        break
                    else:
                        #checking if the book is available
                        
                        cur.execute(f'select Available from books where book_id={id}')
                        for avail in cur:
                            if avail[0]=='no':
                                found=False
                                # global available
                                available=False
                                print('\t\t\t\t\033[1;31;40mThe book isn\'t available at the moment\033[0;37;40m')
                                # break                   #breaking of while loop
                            else:
                                available=True
                        break
                    
                else:
                    print('\t\t\t\t\033[1;31;40m*Invalid Input*\033[0;37;40m')
                    pass
            else:
                print('\t\t\t\t\033[1;31;40m*Enter the digits only*\033[0;37;40m')
                pass

        if id=='':break

        if found:
            while found: #taking admission no. or mobile no. and looking for it in database
                global adm_mob
                adm_mob  = input('\tAdm no. : ').strip() #input('\t[Adm no./ Mobile no.] : ').strip()
                if adm_mob=='':
                    # print('\nIssueing book exit')
                    break
                elif adm_mob.isdigit():
                    if int(adm_mob)>0:
                        adm_mob=int(adm_mob)
                        if len(str(adm_mob))==10:
                            #check for mobile number validation here
                            print('\n\t\t\t\tMobile no: ',adm_mob,'is being issued book "________"\n')
                        else:
                            #check for admission validation here
                            global adm_found
                            adm_found=False
                            cur.execute('select Adm_no from students')
                            for Adm_no in cur:          #iteration of book ids
                                if adm_mob in Adm_no:   #checking for book id
                                    adm_found=True
                                    break
                            if adm_found:
                                break                   #breaking of while loop
                            else:
                                print('\t\t\t\tNo such admission number found')
                                pass
                            
                    else:
                        print('\t\t\t\t\033[1;31;40m*Invalid Input*\033[0;37;40m')
                        pass
                else:
                    print('\t\t\t\t\033[1;31;40m*Enter the digits only*\033[0;37;40m')
                    pass
        else:
            pass #break

        if available:
            try:
                cur.execute(f'select book_name from books where book_id ={id}')
                for bname in cur:
                    book=bname[0]
                            
                cur.execute(f'select name from students where adm_no ={adm_mob}')
                for sname in cur:
                    student=sname[0]

                #students table
                cur.execute(f'select adm_no,name,email_id,phone_no from students where adm_no={adm_mob}')
                for i in cur:
                #     print(i)

                    #book_borrowers table
                    cur.execute(f'insert into book_borrowers (adm_no,name,email_id,phone_no,Borrowed_book_id) values {i+(id,)}')
                    # print('\nAdding to book borrowers table')
                    cur.execute('select * from book_borrowers')
                    for i in cur:
                        # print(i)
                        borrower_on=i[6]
                        borrower_no=i[0]

                #books table
                cur.execute(f'update books set available="no" where book_id={id}')
                # print('\nUpdated available column')
                # cur.execute('select * from books')
                # for i in cur:
                #     print(i)

                cur.execute('commit')
                cur.execute('select max(borrower_no) from book_borrowers')
                for i in cur:

                    print('\n\t\b\033[1;32;40m"'+book+'" book is given to "'+student+'" with Borrower Number :',i[0],'\033[0;37;40m')

            except:
                pass;#print('Error during updating book_borrowers')
            #         # print('Error in showing book name and student name | when any of book id or admission is not given')
        else:
            pass
        print()
        print('-'*(os.get_terminal_size()[0]))





def shelf():                #Showing all Books
    print('''
 +---------------------+
 |     Book Shelf      |
 +---------------------+
    ''')
    cur.execute('select Book_ID,Book_Name,count(*)  from books group by Book_Name;')
    count=1
    for book in cur:
        # print(' ',str(count)+'.',book[1],'- ID :',book[0])    #storing the book in the shelf [list]
        
        print(' ',str(count).rjust(3,' ')+'.',(book[1].ljust(30,'.'))[:30]+'...'+' ID:'+str(book[0]),'| Quantity:'+str(book[2]))
        count+=1
    print()
    #colorful details
    cur.execute('select count(*) from books')
    for i in cur:
        print(f'  \033[0;37;41m Total Quantity \033[0;37;40m\033[0;30;47m {i[0]} \033[0;37;40m ')



def add_books():    #char(20) this is the limit by MySql            #add new book/books to database
    print('''
    +---------------------+
    |   Adding Books      |
    +---------------------+
     ''')

    global Book_Name,Quantity,Class ,Subject ,Language ,Publisher , Author

    while True:
        Book_Name = input('\n\tBook Name : ').strip().title()

        if Book_Name=='':  #No book will be added without Book ID 
            print('\tAdding Book(s) Canceled')
            break
            
        else:

            global Quantity,Class
            while True:
                Quantity  = input('\tQuantity  : ').strip()
                if Quantity=='':
                    pass
                elif Quantity.isdigit():
                    if int(Quantity)>0:
                        Quantity=int(Quantity)
                        break
                    else:
                        print('\t\t\t\t\033[1;31;40m*Quantity should be greater than zero*\033[0;37;40m')
                        pass
                else:
                    print('\t\t\t\t\033[1;31;40m*Enter the digits only*\033[0;37;40m')
                    pass

            while True:
                Class     = input('\tFor Class : ').strip()
                if Class=='':
                    pass
                elif Class.isdigit():
                    if int(Class)>0:
                        Class=int(Class)
                        break
                    else:
                        print('Class should be more than zero'.title())
                        pass
                else:
                    print('\t\t\t\t\033[1;31;40m*Enter the digits only*\033[0;37;40m')
                    pass

            Subject   = input('\tSubject   : ').strip().title()
            Language  = input('\tLanguage  : ').strip().title()
            Publisher = input('\tPublisher : ').strip().title()
            Author    = input('\tAuthor    : ').strip().title()

            add_book = (f"insert into Books (Book_Name,Class,Subject,Language,Publisher,Author,Available) values \
                        ('{Book_Name}',{Class},'{Subject}','{Language}','{Publisher}','{Author}','yes')")

            #Are you sure you want to add the book or cancle
            ask=input('\n\tAdding book confirmation [y/n] : ').strip().lower()

            if ask=='y':  #this section can raise error due to sql datatype limit
                for i in range(Quantity):
                    try:
                        cur.execute(add_book)
                        cur.execute('commit')
                    except:
                        print('\t\t*error due to sql datatype limit(s)*')
                if len(Book_Name)>20:
                    print('\n\t>',str(Quantity)+f' "{Book_Name[0:20]+"..."}" books(s) Added','\n')
                else:
                    print('\n\t>',str(Quantity)+f' "{Book_Name[0:20]}" books(s) Added','\n')
                print('-'*(os.get_terminal_size()[0]))
            else:
                print('\tBook not added')
                pass   



def delete_books():    #deleting  book/books from database, store book details before deleting and before commiting
    print('''
    +---------------------+
    |   Deleting Books    |
    +---------------------+
    ''')
    while True:
        delete=input('\n\tEnter Book ID : ')
        if delete=='':
            break
        elif delete.isdigit():
            #this below code does not throw error
            cur.execute('select Book_ID from books')
            global found_and_deleted
            found_and_deleted=False
            for id in cur:
                
                if int(delete) == id[0]:
                    try:
                        cur.execute(f'delete from books where Book_ID = {id[0]}')
                        cur.execute('commit')
                        found_and_deleted=True
                    except:
                        print(id[0],'From else block')
                        print('\tMySql error!')

            if found_and_deleted:
                print('\tDeleted : "'+id[1]+'"')
            else:
                print('\t\t\t*Book Does Not Exist*')

        # elif delete.isalpha() or delete.isalnum():
        #     print('\t\t*Book Does Not Exist*')
        else:
            print('\t\t\t\t\033[1;31;40m*Enter the digits only*\033[0;37;40m')
            pass
            
            
    
    print('\tDeleting Book(s) Canceled')







def submit_book():
    print('''
    +---------------------+
    |   Receving Books    |
    +---------------------+
    ''')
    while True:
        borrower_no=input('\tBorrower_No: ')
        if borrower_no=='':
            print('\tRecieving Book(s) Canceled')
            break
        elif borrower_no.isalpha():
            print('\t\t\t\t\033[1;31;40m*Enter the digits only*\033[0;37;40m')
            pass
        elif borrower_no.isdigit():
            borrower_no=int(borrower_no)

            # try:
            cur.execute(f'select borrower_no,Borrowed_book_id,submit_date from book_borrowers where borrower_no={borrower_no}')
            
            global found
            found=False
            for i in cur:

                if i[0]==borrower_no and i[2]==None:
                    found=True
                    cur.execute(f'update books set available="yes" where book_id={i[1]}')
                    cur.execute(f'update book_borrowers set `submit_date`=CURRENT_TIMESTAMP  where Borrowed_book_id={i[1]}')
                    # cur.execute(f'update book_borrowers set total_days=datediff(CURRENT_TIMESTAMP,borrowed_date) where borrower_no={}')
                    cur.execute('commit')
                    print('\tBook Submited Sucessfully\n')
                    print('-'*(os.get_terminal_size()[0]),'\n')
            
            if not found:
                print('\t Either Book has been submitted or there is no such borrower ID\n'.title())
        else:
            print('\t\t\t\t\033[1;31;40m*Enter the digits only*\033[0;37;40m')



def art():
    print('''
                    .-~~~~~~~~~-._       _.-~~~~~~~~~-.
                __.'              ~.   .~              `.__
            .'//                  \./                  \\`.
            .'//                     |                     \\`.
        .'// .-~"""""""~~~~-._     |     _,-~~~~"""""""~-. \\`.
        .'//.-"                 `-.  |  .-'                 "-.\\`.
    .'//______.============-..   \ | /   ..-============.______\\`.
    .'______________________________\|/______________________________`.
    ''')






def Ajay_Kisku_Colored(): #looks good only in full screen
    print()
    times=7
    center='.center(os.get_terminal_size()[0])'
    row1=f'\033[0;37;41mAjay \033[0;37;40m\033[0;30;47m Kisku \033[0;37;40m  '*times 
    row2=f'\033[0;37;40m\033[0;30;47mKisku \033[0;37;40m '+f'\033[0;37;41m Ajay \033[0;37;40m\033[0;30;47m Kisku \033[0;37;40m  '*(times-1)+f'\b\033[0;37;41m Ajay \033[0;37;40m'

    for i in range(3):
        # print(' '+row1+'\n\n'+row2+'\n')
        # print(' '+row1+'\n'+row2)
        print(' '+row1+'\n '+row2+'\n')

internet=False
def is_internet():
    import requests
    
    try:
        re=requests.get('https://www.google.com')
        if re.status_code==200:
            # date=re.headers()
            global internet
            internet=True
    except: 
        internet=False
        

def web():
    #search book online in many sites
    is_internet()
    if internet:
        get=input('  Search on web for book : ').strip().replace(' ','+')
        if get=='':
            pass
        else:
            time.sleep(1)
            import webbrowser as web
            web.open(f'https://www.youtube.com/results?search_query=book+summary+{get}')
            web.open(f'https://www.flipkart.com/search?q=book%20'+get.replace("+","%20")) #flipkart
            web.open(f'https://www.amazon.in/s?k={get}&i=stripbooks&ref=nb_sb_noss_1') #amazon
            web.open(f'https://www.google.com/search?tbm=bks&q={get}') #google books
            web.open(f'https://www.google.com/search?q=filetype:pdf%20{get}')
            web.open(f'https://archive.org/details/books?and%5B%5D={get}')
            web.open( 'https://1lib.in/s/'+get.replace('+','%20'))
            web.open(f'https://www.pdfdrive.com/search?q={get}')
            
            time.sleep(2)
            print('  [I hope you got your book]')
    else:
        print('  No Internet Connection')



def about_devs():
    a='  You will be redirected to developer\'s website...'  #print normal
    b=''
    for i in a:
        b+=i; time.sleep(0.1)
        print(b,end='\r')
    print(a)

    time.sleep(1)
    os.system('start http://rajaj1.000webhostapp.com/')
    time.sleep(1)
    # keyboard.press_and_release('F11')
    print('  [You were on developer site]')





def run_command():               #all the main commands will be given here

    print('─'*(os.get_terminal_size()[0]))
    global lms
    lms=input('\033[0;37;45m Run \033[0;30;46m [COMMAND] \033[0;37;40m > ').strip().lower()
    print('─'*(os.get_terminal_size()[0]))
    # speak('executing '+lms+' command')








def main():              #First function to execute it holds other main function 
    # os.system('mode con: lines=25 cols=88')
    connect_to_DB()
    terminal_look()
    command_lists()

    while True:                      #all the features | function acessed from here
        
        print()
        run_command()
        print()

        if lms=='':                                                 #when user gives no input
            pass
        elif lms in 'x exit quit close'.split():                       #to exit the program
            print('[ Bye! ]          Software by -Ajay Kisku and Rohan Kumar'); time.sleep(1)
            exit()# quit()
        elif lms in 'cls clear'.split():                                 #to clear the screen
            os.system('cls')
        elif lms in 'c cmd cmds command commands'.split():                   #to show the command lists
            command_lists()
        
        elif lms in 's find search'.split():                            #search book in local library 
            search_book()
        elif lms in '1 lend issue l i'.split():                                #Submit book 
            lend_book()
        elif lms in '2 sub submit rec receive '.split():                                #Submit book 
            submit_book()
        elif lms in '3 a add addbook'.split():                                    #to add new books
            add_books()
        elif lms in '4  u update updatebook'.split():                   #update book
            book_update()
        elif lms in '5 d del delete deletebook'.split():                                #delete book record
            delete_books()
        elif lms=='art':                                                #simple book art
            art()
        elif lms in 'shelf allbooks all'.split():                         #to show all books
            shelf()
        elif lms in 'pdf web online more online_book online_books onlinebooks'.split():       #web search for book (pdf)
            web()
        elif lms in 'dev devs devloper aj ajay kisku ajaykisku'.split():   #developer's site
            about_devs()
            Ajay_Kisku_Colored()
        elif lms in 't total'.split():                                            #total books (summary)
            t()
        elif lms in 'f fine'.split():                                            #total books (summary)
            current_borrowers()
        
        elif lms in 'kuch'.split():                                         #add some feature here
            print('\t\t\tAre kuch nahi!')
        elif lms in 'help'.split():                                         #add some feature here
            print('\t\t\t"God help those who help themself"')
        else :                                                             #for invalid input
            print(f'\033[1;31;40m[Invalid Command!]\033[0;37;40m')
            beep(1)


if __name__=='__main__':
    main()
