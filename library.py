#-------------------functions-----------------------
def add_member(num, member):
    for i in range(num):
        while True:
            membership_num = int(input("enter your membership number: "))
            if membership_num in members_dic:
                print("this number is used, enter another number.")
            else:
                name = input("enter your name")
                last_name = input("enter your last name")
                code_melli = int(input("enter your code melli"))
                birth_date = input("enter your birthday")
                address = input("enter your address")

                member = {}
                member["name"] = name
                member["last_name"] = last_name
                member["code_melli"] = code_melli
                member["birthday"] = birth_date
                member["address"] = address

                members_dic[membership_num] = member
                break
            
    return members_dic



def show_members():

    for x, y in members_dic.items():
        print(x,y)
        print(f"membership number:{x} - name: {y['name']} - last name: {y['last_name']} - code melli: {y['code_melli']} - birthday: {y['birthday']} - address: {y['address']}")


def add_book(num, book):
    for i in range(num):
        while True:
            book_num = int(input("enter your book number: "))
            if book_num in books_dic:
                print("this number is used, enter another number.")
            else:
                book_name = input("enter the books name")
                author_name = input("enter the authors name")
                publication_year = int(input("enter the year of publication"))
                genre = input("enter the genre")
                book = {}
                book["books_name"] = book_name
                book["authors_name"] = author_name
                book["publication"] = publication_year
                book["genre"] = genre
                book["borrow"] = True
                books_dic[book_num] = book
                break
            
    return books_dic



def show_books():
    for book_num, y in books_dic.items():
        print(f"book number:{book_num} - books name: {y['books_name']} - authors name: {y['authors_name']} - year of publication: {y['publication']} - genre: {y['genre']}")
        
def remove_member():
    while True:
        member_num = int(input("enter the members number that you wanna remove: "))
        if member_num not in members_dic.keys():
            print("could not find this member number!")
        else:
            del(members_dic[member_num])
            print("removed succesfully!")
            break

def remove_book():
    while True:
        book_num = int(input("enter the book number that you wanna remove: "))
        if book_num not in books_dic.keys():
            print("could not find this book number!")

        else:
            del(books_dic[book_num])
            print("removed succesfully!")
            break

def edit_member(member):
    member_num = int(input("enter the members number that you wanna edit: "))
    while True:
        if member_num not in members_dic.keys():
            print("could not find this member number!")
        else:
            choise = input("which information you wanna edit: ")
            if choise == "name":
                member['name'] = input("enter a new name: ")
            elif choise == "last name":
                member['last_name'] = input("enter a new last name: ")
            elif choise == "code melli":
                member['code_melli'] = input("enter a new code melli: ")
            elif choise == "birthday":
                member['birthday'] = input("enter a new birthday: ")
            elif choise == "address":
                member['address'] = input("enter a new address: ")
            break

def edit_book(book):
    book_num = int(input("enter the book number that you wanna edit: "))
    while True:
        if book_num not in books_dic.keys():
            print("could not find this book number!")
        else:
            choise = input("which information you wanna edit: ")
            if choise == "name":
                book['books_name'] = input("enter a new name: ")
            elif choise == "authors name":
                book['authors_name'] = input("enter a new authors name: ")
            elif choise == "publication":
                book['publication'] = int(input("enter a new year: "))
            elif choise == "genre":
                book['genre'] = input("enter a new genre: ")
                break

def av_books():
    #book_num = int(input("enter the number of the book that you wanna borrow: "))
    #a = members_dic.get(book_num)
    pass


def unav_books():
    pass

def search(books_dic, book):
    s_method = input("in what way you wanna search? ")
    if s_method == "name":
        name = input("enter the books name: ")
        for i in books_dic.values():
            if name in i["books_name"]:
                print("yes")
            else:
                print("no")
    elif s_method == "genre":
        g_books = []
        genre1 = input("enter the genre: ")
        for i in books_dic.items():
            if book['genre'] == genre1:
                g_books.append(book['books_name'])
        print(g_books)
    else:
        print("not defined!")

def borrow():
    pass




#-------------------main------------------------------
members_dic = {}
books_dic = {}
member = {}
book = {}
while True:
    user = int(input("enter an action number:\n 1.Add Member\n 2.Add Book\n 3.Show Member\n 4.Show Book\n 5.Edit Member\n 6.Edit Book\n 7.Remove Member\n 8.Remove Book\n 9.Available Books\n 10.Unavailable Books\n 11.Search\n 12.Borrow Book\n 13.Help\n 14.Exit"))
    if user == 1:
        num = int(input(" how many members you wanna add? "))
        add_member(num, member)
    elif user == 2:
        num = int(input("how many books you wanna add?"))
        add_book(num, book)
    elif user == 3:
        show_members()
    elif user == 4:
        show_books()
    elif user == 5:
        edit_member(member)
    elif user == 6:
        edit_book(book)
    elif user == 7:
        remove_member()
    elif user == 8:
        remove_book()
    elif user == 9:
        #av_books()
        pass
    elif user == 10:
        pass
    elif user == 11:
        search(books_dic, book)
    elif user == 12:
        pass
    elif user == 13:
        print("you can add, edit and remove members and books by entering their command numbers\n you can search for a speacial book by its name and you can also search for books in a speasial genre\n you can search for available and unavailable books\n you can borrow books\n ")
    elif user == 14:
        break
        




















                         
