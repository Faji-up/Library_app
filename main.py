import io
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
WINDOW_WIDTH = 800
WINDOW_HEIGTH = 600
BACKGROUND_COLOR = "white"
ACTIVE_USER_ID = 0
current_date = datetime.now().date().today()
current_date = current_date.strftime("%m/%d/%y")
images_list = {
    "menu": "my_images/categories.png",
    "bg": "my_images/bg1.png",
    "bg2": "my_images/abundant-collection-antique-books.jpg",
    "bg3": "my_images/download_blur.png",
    "back1": "my_images/back-arrow.png",
    "lg": "my_images/logout.png",
    'start': "my_images/get.png",
    'start2':"my_images/get_started2.png",

    'log_1': "my_images/login.png",
    'log_2':"my_images/login1.png",
    "cre_1": "my_images/create.png",
    "cre_2":"my_images/create2.png",
    "book": "my_images/book.png",
    "book2":"my_images/open-book.png",
    "book3":"my_images/open-book (2).png",
    "book4":"my_images/book (1).png",
    "prof": "my_images/user (1).png",

    #Books page images
    #======Background
    "background1":"my_images/istockphoto-1187066410-612x612.jpg",
    "background3":"my_images/bg1000.jpg",
    "sidebg":"my_images/crop-0.webp",
    "entrep_bg":"my_images/entrep_bg1.jpeg",
    "komo_bg":"my_images/komuni_bg.jpg",
    "philo_bg":"my_images/philo_bg.jpeg",
    #==== book cover
    "entrep_cov":"my_images/images (39).jpeg",
    "komo_cov":"my_images/komunikasyon-cover.jpg",
    "philo_cov":"my_images/philo_cover.jpeg",
    #=== container image
    "con":"my_images/con_bg.jpeg",
    #=== buttons
    "rev":"my_images/reserve1.png",
    "rev1":"my_images/reserve.png",
    #== reserve bg
    "rev_bg":"my_images/reserved_bg.jpg",
    # admin button
    "admin":"my_images/setting.png",
    "users": "my_images/multiple-users-silhouette (2).png",
    "books": "my_images/book.png",
    "barrow": "my_images/borrow.png"
}

def get_image(image):
    return images_list.get(image)


def create_img(width, heigth, path):
    img = Image.open(path)
    img = img.resize((width, heigth))
    img = ImageTk.PhotoImage(img)
    return img


class Account:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.books = []

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def add_book(self, book):
        self.books.append(book)


class Book():
    def __init__(self,type, title, author,description):
        self.type = type
        self.title = title
        self.author = author
        self.description = description
    def get_type(self):
        return self.type
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_des(self):
        return self.description

# ============================================================================= Library App
class Library_app:
    def __init__(self, root):
        self.main_frame = root
        self.accounts_list = []
        self.books_list = []
        self.active_frame = None
        # top config
        self.top_frame = None
        self.top_text = StringVar()
        self.menu_frame_id = None
        self.menu_frame = None
        self.menu_btn = None
        # bottom config
        self.bottom_bar = None

        # ==== images
        self.start_img = create_img(130, 60, get_image("start"))
        self.start_img2 = create_img(130, 60, get_image("start2"))

        self.background_image = create_img(WINDOW_WIDTH, WINDOW_HEIGTH, get_image("bg"))
        self.background_image2 = create_img(WINDOW_WIDTH, WINDOW_HEIGTH, get_image("bg2"))
        self.container_bg = create_img(WINDOW_WIDTH, WINDOW_HEIGTH, get_image("bg2"))
        self.container_bg_b = create_img(WINDOW_WIDTH, WINDOW_HEIGTH, get_image("bg3"))
        # log and create button
        self.log_in_btn = create_img(100, 55, get_image("log_1"))
        self.log_in_btn2 = create_img(100,55,get_image("log_2"))
        self.create_btn = create_img(100, 55, get_image("cre_1"))
        self.create_btn2 = create_img(100, 55, get_image("cre_2"))

        # ===== bottom bar icons
        self.book_img = create_img(23, 24, get_image("book"))
        self.book_img2 = create_img(24, 25, get_image("book4"))
        self.barrowed_imd = create_img(23, 24, get_image("book2"))
        self.barrowed_imd2 = create_img(24, 25, get_image("book3"))

        # ===== menu image
        self.menu_img = create_img(20, 21, get_image("menu"))
        self.profile_img = create_img(23, 24, get_image("prof"))
        self.back_image = create_img(23, 24, get_image("back1"))
        self.logout_img = create_img(22, 23, get_image("lg"))
        self.users_img = create_img(22,23,get_image("users"))
        self.books_img = create_img(22,23,get_image("books"))
        self.barrow_img = create_img(22,23,get_image("barrow"))
        #=========== books home bg image
        self.home_bg = create_img(WINDOW_WIDTH,WINDOW_HEIGTH,get_image("background1"))
        self.sidebg = create_img(150,WINDOW_HEIGTH,get_image("sidebg"))
        self.barrow_img2 = create_img(WINDOW_WIDTH,WINDOW_HEIGTH,get_image("background3"))
        #=========== book cover
        self.entrep_cov = create_img(WINDOW_WIDTH-40, 220, get_image("entrep_cov"))
        self.kamo_cov = create_img(WINDOW_WIDTH - 40, 220, get_image("komo_cov"))
        self.philo_cov = create_img(WINDOW_WIDTH - 40, 220, get_image("philo_cov"))
        #========== book bg
        self.entrep_bg = create_img(WINDOW_WIDTH,WINDOW_HEIGTH,get_image("entrep_bg"))
        self.komo_bg = create_img(WINDOW_WIDTH,WINDOW_HEIGTH,get_image("komo_bg"))
        self.philo_bg = create_img(WINDOW_WIDTH,WINDOW_HEIGTH,get_image("philo_bg"))
        # book container image
        self.con_img = create_img(WINDOW_WIDTH-20,400,get_image("con"))
        # ==== check variables
        self.name = StringVar()
        self.username_val = StringVar()
        self.password_val = StringVar()
        self.confirm_pass_val = StringVar()
        # ========== restore
        self.restore_acc()
        self.restore_book()
        # reserve button
        self.rev1 = create_img(120,70,get_image("rev"))
        self.rev2 = create_img(120, 70, get_image("rev1"))
        # reserve bg
        self.rev_bg = create_img(600,400,get_image('rev_bg'))
        # admin button image
        self.admin_img = create_img(20,20,get_image("admin"))

    # ==================================== functions

    def top_bar_window(self):
        self.menu_img = create_img(20, 21, get_image("menu"))
        self.top_frame = Canvas(self.main_frame, height=40, bg="white")
        self.top_frame.pack(side=TOP, fill=X)
        self.menu_btn = Button(self.top_frame,
                               image=self.menu_img,
                               command=self.show_menu,
                               bg="white",
                               relief="flat")
        self.menu_btn.image = self.menu_img
        self.menu_btn.pack(side=LEFT)


        self.menu_frame_id = self.main_frame.create_window(75, (WINDOW_HEIGTH // 2) + 30, window=self.menu_frame,
                                                           height=WINDOW_HEIGTH, width=150)

        self.top_frame.create_text((WINDOW_WIDTH//2),13,text=self.top_text.get(),font=("Times",13,"bold"))
    def unshow_bars(self):
        self.top_frame.pack_forget()
        self.bottom_bar.pack_forget()

    def bottom_bar_window(self):
        self.bottom_bar = Canvas(self.main_frame, height=5)

        books = Button(self.bottom_bar, image=self.book_img, width=(WINDOW_WIDTH // 2), relief="flat",
                       command=self.home_window,bg="#E7E7E7")
        books.pack(side=LEFT)
        books.bind("<Enter>", lambda event: (books.config(image=self.book_img2,bg="white",highlightcolor="black",highlightbackground="black",highlightthickness=1)))
        books.bind("<Leave>", lambda event: (books.config(image=self.book_img,highlightthickness=0,bg="#E7E7E7")))

        barrow = Button(self.bottom_bar, image=self.barrowed_imd, width=(WINDOW_WIDTH // 2), relief="flat",
                         command=self.barrow_book_window,bg="#E7E7E7")
        barrow.pack(side=LEFT)
        barrow.bind("<Enter>",lambda event: (barrow.config(image=self.barrowed_imd2,bg="white",highlightcolor="black",highlightbackground="black",highlightthickness=1)))
        barrow.bind("<Leave>", lambda event: (barrow.config(image=self.barrowed_imd,highlightthickness=0,bg='#E7E7E7')))

        self.bottom_bar.pack(side=BOTTOM, fill=X)

    def show_menu(self):
        self.menu_frame = Canvas(self.main_frame, bg=BACKGROUND_COLOR)

        logout = Button(self.menu_frame, image=self.logout_img, text="          Log out", compound=LEFT, relief=FLAT, bg="white",
               font=("Times", 10, "bold"),command=self.start_window)
        logout.pack(side=TOP, fill=X)
        logout.bind("<Enter>", lambda event: (
            logout.config(image=self.logout_img, bg="grey", highlightcolor="black", highlightbackground="black",
                         highlightthickness=1)))
        logout.bind("<Leave>", lambda event: (logout.config(image=self.logout_img, highlightthickness=0, bg="white")))
        logout.pack(side=TOP, fill=X)

        self.menu_frame_id = self.main_frame.create_window(75, (WINDOW_HEIGTH // 2)+30, window=self.menu_frame,
                                                             height=WINDOW_HEIGTH, width=150)

        # barrow table button
        barrow = Button(self.menu_frame, image=self.barrow_img, text="          Barrows", compound=LEFT, relief=FLAT,
                        bg="white",
                        font=("Times", 10, "bold"), command=self.barrow_book_window)
        barrow.pack(side=TOP, fill=X)
        barrow.bind("<Enter>", lambda event: (
            barrow.config(image=self.barrow_img, bg="grey", highlightcolor="black", highlightbackground="black",
                          highlightthickness=1)))
        barrow.bind("<Leave>", lambda event: (barrow.config(image=self.barrow_img, highlightthickness=0, bg="white")))

        # books button
        books = Button(self.menu_frame, image=self.book_img, text="          Books", compound=LEFT, relief=FLAT,
                       bg="white",
                       font=("Times", 10, "bold"), command=self.home_window)
        books.pack(side=TOP, fill=X)
        books.bind("<Enter>", lambda event: (
            books.config(image=self.book_img, bg="grey", highlightcolor="black", highlightbackground="black",
                         highlightthickness=1)))
        books.bind("<Leave>", lambda event: (books.config(image=self.books_img, highlightthickness=0, bg="white")))

        self.menu_btn.config(command=self.unshow_menu, image=self.back_image)
        self.menu_btn.image = self.back_image

    def unshow_menu(self):
        self.main_frame.delete(self.menu_frame_id)
        self.menu_btn.config(command=self.show_menu, image=self.menu_img)

    def set_background(self, bg):
        if bg == 1:
            self.active_frame.create_image((WINDOW_WIDTH // 2), (WINDOW_HEIGTH // 2), image=self.background_image)
        elif bg == 2:
            self.active_frame.create_image((WINDOW_WIDTH // 2), (WINDOW_HEIGTH // 2), image=self.background_image2)

    def start_window(self):
        if self.top_frame:
            self.top_frame.pack_forget()
        self.close_active_frame()
        self.active_frame = Canvas(self.main_frame, bg="red")
        self.set_background(1)
        start_btn = self.active_frame.create_image((WINDOW_WIDTH // 2), 550, image=self.start_img)
        self.active_frame.tag_bind(start_btn, "<Button>", self.log_in_window)
        self.active_frame.tag_bind(start_btn, "<Enter>",lambda event:self.active_frame.itemconfig(start_btn, image=self.start_img2))
        self.active_frame.tag_bind(start_btn, "<Leave>",
                                   lambda event: self.active_frame.itemconfig(start_btn, image=self.start_img))

        self.active_frame.pack(expand=True, fill=BOTH)

    def create_account(self, name, username, password):
        conn = sqlite3.connect("Accounts.db")
        c = conn.cursor()
        if self.create_validation():
            acc = [name, username, password]
            account = Account(name, username, password)
            self.accounts_list.append(account)
            c.executemany("INSERT INTO accounts (name,username,password) VALUES (?,?,?)", (acc,))
            print("done")
            messagebox.showinfo("Sign up","Account successfully registered")
            conn.commit()
            conn.close()
        conn.close()

    def create_validation(self):
        if self.isExist_account():
            if self.password_val.get() == self.confirm_pass_val.get() and self.username_val.get() != "" and self.password_val.get() != "":
                print("yes")
                return True
            else:
                messagebox.showerror("Sign up error","Theres a problem by creating this account please\n 'Fill all required datas' ")
                return False

    def isExist_account(self):
        isExist = True
        conn = sqlite3.connect("Accounts.db")
        c = conn.cursor()
        c.execute("SELECT * FROM accounts")
        for acc in c.fetchall():
            if self.name.get() == acc[1]:
                isExist = False
                messagebox.showerror("Name already used please choose another name")
                break
            else:
                pass
        print("yesss")
        conn.commit()
        conn.close()
        return isExist

    def active_user(self):
        return self.accounts_list[ACTIVE_USER_ID]

    def close_active_frame(self):
        if self.active_frame:
            self.active_frame.destroy()
        if self.top_frame and self.bottom_bar:
            self.unshow_bars()

    def restore_book(self):
        conn = sqlite3.connect("Books.db")
        c = conn.cursor()
        c.execute("SELECT * FROM books")
        for books in c.fetchall():
            book = Book(books[1], books[2], books[3],books[4])
            self.books_list.append(book)
        conn.commit()
        conn.close()

    def restore_acc(self):
        conn = sqlite3.connect("Accounts.db")
        c = conn.cursor()
        c.execute("SELECT * FROM accounts")
        for acc in c.fetchall():
            book = Account(acc[1], acc[2], acc[3])
            self.accounts_list.append(book)
        conn.commit()
        conn.close()
    def login_validation(self):
        if self.check_account():
            self.home_window()
        elif self.username_val.get() == "admin" and self.password_val.get() == "admin":
            self.books_window()
        else:
            messagebox.showerror("Validation Error", "Account doesnt exist")

    def check_account(self):
        global ACTIVE_USER_ID
        isExists = False
        for acc in range(len(self.accounts_list)):
            if self.accounts_list[acc].get_username() == self.username_val.get() and self.accounts_list[
                acc].get_password() == self.password_val.get():
                ACTIVE_USER_ID = acc
                isExists = True

                break

        return isExists

    def log_in_window(self, event):
        self.close_active_frame()
        self.active_frame = Canvas(self.main_frame)

        self.set_background(2)
        log_in_con = Canvas(self.active_frame, relief="flat", highlightthickness=1, highlightbackground="white",
                            highlightcolor="white")

        log_in_con.create_image((WINDOW_WIDTH // 2) - 210, (WINDOW_HEIGTH // 2) - 167, image=self.container_bg_b)

        log_in_con.create_text(195, 35, text="Log in", fill="white", font=("Times", 25, "bold"))

        log_in_con.create_text(129, 110, text="Username", fill="white", font=("Times", 11))
        username = Entry(log_in_con, textvariable=self.username_val, font=("Justify", 15), relief="flat")
        log_in_con.create_window(195, 140, window=username, width=200)

        password = Entry(log_in_con, textvariable=self.password_val, show='*', font=("Justify", 15), relief="flat")
        log_in_con.create_text(129, 165, text="Password", fill="white", font=("Times", 11))
        log_in_con.create_window(195, 190, window=password, width=200)

        login_btn = log_in_con.create_image(195, 260, image=self.log_in_btn)
        log_in_con.tag_bind(login_btn, "<Button>", lambda event: self.login_validation())
        log_in_con.tag_bind(login_btn, "<Enter>",
                             lambda event: log_in_con.itemconfig(login_btn, image=self.log_in_btn2))
        log_in_con.tag_bind(login_btn, "<Leave>",
                             lambda event: log_in_con.itemconfig(login_btn, image=self.log_in_btn))

        log_in_con.create_text(195, 300, text="Don't have an account?", fill="white", font=("Times", 10, "bold"))
        create = log_in_con.create_text(195, 320, text="Create account", fill="#F5F5F5",
                                        font=("Times", 10, "underline"))
        log_in_con.tag_bind(create, "<Button>", lambda event: self.create_account_window())

        self.active_frame.create_window((WINDOW_WIDTH // 2), (WINDOW_HEIGTH // 2), window=log_in_con, height=370)
        self.active_frame.pack(expand=True, fill=BOTH)

    def create_account_window(self):
        self.close_active_frame()
        self.active_frame = Canvas(self.main_frame)
        self.username_val.set("")
        self.password_val.set("")

        self.set_background(2)
        sign_up_con = Canvas(self.active_frame, relief="flat", highlightthickness=1, highlightbackground="white",
                             highlightcolor="white")

        sign_up_con.create_image((WINDOW_WIDTH // 2) - 210, (WINDOW_HEIGTH // 2) - 167, image=self.container_bg_b)

        sign_up_con.create_text(195, 35, text="Sign up", fill="white", font=("Times", 25, "bold"))

        sign_up_con.create_text(118, 118, text="Name", fill="white", font=("Times", 11))
        name = Entry(sign_up_con, textvariable=self.name, font=("Justify", 15), relief="flat")
        sign_up_con.create_window(195, 140, window=name, width=200)

        sign_up_con.create_text(129, 167, text="Username", fill="white", font=("Times", 11))
        username = Entry(sign_up_con, textvariable=self.username_val, font=("Justify", 15), relief="flat")
        sign_up_con.create_window(195, 190, window=username, width=200)

        password = Entry(sign_up_con, textvariable=self.password_val, show='*', font=("Justify", 15), relief="flat")
        sign_up_con.create_text(129, 218, text="Password", fill="white", font=("Times", 11))
        sign_up_con.create_window(195, 240, window=password, width=200)

        confirm_password = Entry(sign_up_con, textvariable=self.confirm_pass_val, show='*', font=("Justify", 15),
                                 relief="flat")
        sign_up_con.create_text(153, 267, text="Confirm password", fill="white", font=("Times", 11))
        sign_up_con.create_window(195, 290, window=confirm_password, width=200)

        signin_btn = sign_up_con.create_image(197, 340, image=self.create_btn)
        sign_up_con.tag_bind(signin_btn, "<Button>",
                             lambda event: self.create_account(self.name.get(), self.username_val.get(),
                                                               self.password_val.get()))
        sign_up_con.tag_bind(signin_btn,"<Enter>",lambda event:sign_up_con.itemconfig(signin_btn,image=self.create_btn2))
        sign_up_con.tag_bind(signin_btn, "<Leave>", lambda event:sign_up_con.itemconfig(signin_btn,image=self.create_btn))

        sign_up_con.create_text(195, 375, text="Already have an account?", fill="white", font=("Times", 10, "bold"))
        login = sign_up_con.create_text(195, 390, text="Log in", fill="#F5F5F5", font=("Times", 10, "underline"))
        sign_up_con.tag_bind(login, "<Button>", self.log_in_window)

        self.active_frame.create_window((WINDOW_WIDTH // 2), (WINDOW_HEIGTH // 2), window=sign_up_con, height=420)
        self.active_frame.pack(expand=True, fill=BOTH)

    def insert_reservation(self,libro,humiram,hiniram,sauli):
        print("click")
        conn = sqlite3.connect("Barrow.db")
        c = conn.cursor()
        data = [libro,humiram,hiniram,sauli]
        for datas in data:
            print(datas)
        c.executemany("INSERT INTO barrow (book_title,humiram,hiniram,sauli) VALUES (?,?,?,?)",(data,))
        messagebox.showinfo("Reservation","Reservation successfulyy")
        conn.commit()
        conn.close()
    # =================================== USER

    def home_window(self):
        self.username_val.set("")
        self.password_val.set("")
        self.top_text.set("Home")

        print("home")
        self.close_active_frame()
        self.active_frame = Canvas(self.main_frame,scrollregion=(0,0,500,500))
        background = Label(self.active_frame,image=self.background_image2)
        background.pack(fill=BOTH)
        #self.active_frame.create_image((WINDOW_WIDTH // 2), (WINDOW_HEIGTH // 2), image=self.home_bg)

        entrep_ = Label(self.active_frame,bg="red",image=self.entrep_cov,highlightthickness=2,highlightcolor="black",highlightbackground="black",relief="flat")
        self.active_frame.create_window((WINDOW_WIDTH//2),200,window=entrep_,width=(WINDOW_WIDTH-40),height=220)
        entrep_.bind("<Enter>",lambda event:entrep_.config(highlightcolor="white",highlightbackground="white"))
        entrep_.bind("<Leave>", lambda event: entrep_.config(highlightcolor="black", highlightbackground="black"))
        entrep_.bind("<Button>",lambda event:self.entrep_window())

        komo_ = Label(self.active_frame,image=self.kamo_cov,highlightthickness=2,highlightcolor="black",highlightbackground="black",relief="flat")
        self.active_frame.create_window((WINDOW_WIDTH // 2), 430, window=komo_, width=(WINDOW_WIDTH - 40), height=220)
        komo_.bind("<Enter>", lambda event: komo_.config(highlightcolor="white", highlightbackground="white"))
        komo_.bind("<Leave>", lambda event: komo_.config(highlightcolor="black", highlightbackground="black"))
        komo_.bind("<Button>",lambda event:self.komonikasyon_window())

        philo_ = Label(self.active_frame, image=self.philo_cov,highlightthickness=2,highlightcolor="black",highlightbackground="black",relief="flat")
        self.active_frame.create_window((WINDOW_WIDTH // 2), 660, window=philo_, width=(WINDOW_WIDTH - 40), height=220)
        philo_.bind("<Enter>", lambda event: philo_.config(highlightcolor="white", highlightbackground="white"))
        philo_.bind("<Leave>", lambda event: philo_.config(highlightcolor="black", highlightbackground="black"))
        philo_.bind("<Button>",lambda event:self.philosophy_window())

        background.bind("<Configure>",
                                      lambda e: self.active_frame.configure(
                                          scrollregion=self.active_frame.bbox("all")))
        background.bind_all("<MouseWheel>", lambda event:self.active_frame.yview_scroll(-1 * (event.delta // 120), "units"))

        self.top_bar_window()
        self.bottom_bar_window()

        self.active_frame.pack(expand=True, fill=BOTH)

    def barrow_book_window(self):
        if self.top_frame:
            self.top_frame.pack_forget()
        self.top_text.set("Reserved Books")
        self.close_active_frame()
        self.active_frame = Canvas(self.main_frame)

        # ================================================= table type
        top_label = Label(self.active_frame, pady=0, bd=0, text="Reserved Books")
        top_label.pack(side=TOP, fill=X)
        # ================================================= TOP LEVEL

        top_label = Label(self.active_frame, pady=0, bd=0)
        top_label.pack(side=TOP, fill=X)
        title_L = Label(top_label, width=50, highlightcolor="grey", highlightbackground="grey",
                        highlightthickness=1, text="Book title")
        title_L.pack(side=LEFT, anchor=N, fill=Y)
        user_L = Label(top_label, width=25, highlightcolor="grey", highlightbackground="grey",
                       highlightthickness=1, text="User")
        user_L.pack(side=LEFT, anchor=N, fill=Y)
        date_barrow = Label(top_label, width=18, highlightcolor="grey", highlightbackground="grey",
                            highlightthickness=1, text="Date barrow")
        date_barrow.pack(side=LEFT, anchor=N, fill=Y)
        date_sauli = Label(top_label, width=18, highlightcolor="grey", highlightbackground="grey",
                           highlightthickness=1, text="Date return")
        date_sauli.pack(side=LEFT, anchor=N, fill=Y)
        # ================================================= data Row

        books_window = Canvas(self.active_frame, height=WINDOW_HEIGTH - 60, scrollregion=(0, 0, 500, 500), bg="white")
        books_window.create_image((WINDOW_WIDTH//2),265,image=self.barrow_img2)
        conn = sqlite3.connect("Barrow.db")
        c = conn.cursor()
        c.execute("SELECT * FROM barrow")
        position_Y = 11
        for data in c.fetchall():
            if data[2] == self.active_user().get_name():
                row = Canvas(self.active_frame)
                Label(row, width=49, padx=4,pady=4, highlightcolor="grey", highlightbackground="grey",
                      highlightthickness=1, text=data[1][0:60]).pack(side=LEFT, anchor=N, fill=Y)
                Label(row, width=25,pady=4, highlightcolor="grey", highlightbackground="grey",
                      highlightthickness=1, text=data[2]).pack(side=LEFT, anchor=N, fill=Y)
                Label(row, width=18,pady=4, highlightcolor="grey", highlightbackground="grey",
                      highlightthickness=1, text=data[3]).pack(side=LEFT, anchor=N, fill=Y)
                Label(row, width=18, pady=4,highlightcolor="grey", highlightbackground="grey",
                      highlightthickness=1, text=data[4]).pack(side=LEFT, anchor=N, fill=Y)

                books_window.create_window((WINDOW_WIDTH // 2) - 1, position_Y, window=row, width=WINDOW_WIDTH)
                books_window.bind("<Configure>",
                                  lambda e: row.configure(scrollregion=row.bbox("all")))
                books_window.bind_all("<MouseWheel>",
                                      lambda event: books_window.yview_scroll(-1 * (event.delta // 120), "units"))
                position_Y += 23

        conn.commit()
        conn.close()
        self.top_bar_window()
        self.bottom_bar_window()
        books_window.pack(side="bottom", fill=X, expand=True, anchor=S)
        self.active_frame.pack(expand=True, fill=BOTH)
    def entrep_window(self):
        self.top_text.set("ENTREPRENEURSHIP BOOKS")
        self.close_active_frame()
        self.active_frame = Canvas(self.main_frame,scrollregion=(0,0,1300,1300))
        background = Label(self.active_frame, image=self.entrep_bg)
        background.pack(fill=BOTH)
        self.top_bar_window()
        position_y = 210
        for book in self.books_list:
            if book.get_type() == "ENTREPRENEURSHIP BOOKS":
                self.create_book_window(position_y,book.get_title(),book.get_author(),book.get_des())
                position_y += 410
        self.active_frame.pack(expand=True, fill=BOTH)

    def komonikasyon_window(self):
        self.top_text.set("KOMUNIKASYON SA PANANALIKSIK BOOKS")
        self.close_active_frame()
        self.active_frame = Canvas(self.main_frame,scrollregion=(0,0,1300,1300))
        background = Label(self.active_frame, image=self.komo_bg)
        background.pack(fill=BOTH)
        self.top_bar_window()
        position_y = 210
        for book in self.books_list:
            if book.get_type() == "KOMUNIKASYON SA PANANALIKSIK":
                self.create_book_window(position_y,book.get_title(),book.get_author(),book.get_des())
                position_y += 410
        self.active_frame.pack(expand=True, fill=BOTH)
    #============= PHILOSOPHY
    def philosophy_window(self):
        self.top_text.set("PHILOSOPHY BOOKS")
        self.close_active_frame()
        self.active_frame = Canvas(self.main_frame,scrollregion=(0,0,870,870))
        Label(self.active_frame, image=self.philo_bg).pack(fill=BOTH)
        self.top_bar_window()
        position_y = 210
        for book in self.books_list:
            if book.get_type() == "PHILOSOPHY":
                self.create_book_window(position_y,book.get_title(),book.get_author(),book.get_des())
                position_y+=410
        self.active_frame.pack(expand=True, fill=BOTH)

    def create_book_window(self,y,title,author,des): # create windows of books
        container = Canvas(self.active_frame,highlightthickness=2,highlightcolor="black",highlightbackground="black",relief="flat")#container
        container.create_image((WINDOW_WIDTH//2)-10,200,image=self.con_img)
        new_title = ""
        title_pos = 50
        print(author)
        for index in range(len(title)): # check if title is too long and when it true the text will create a new line
            new_title+=title[index]
            if index == 87:
                new_title += "-\n"
                title_pos = 60
        # title section
        container.create_text((WINDOW_WIDTH//2),30,text="Title",font=("Justify",10,"bold"),fill="white")
        container.create_text((WINDOW_WIDTH//2),title_pos,text=f"{new_title}",font=("Justify",12,"bold"),fill="white")

        # Author section
        container.create_text((WINDOW_WIDTH // 2), 110, text="Author", font=("Justify", 10, "bold"), fill="white")
        container.create_text((WINDOW_WIDTH // 2), 130, text=f"{author}", font=("Justify", 12, "bold"),
                              fill="white")
        # Description section
        new_des_text = ""
        des_pos = 220
        cut = 87
        for index2 in range(len(des)):
            new_des_text += des[index2]
            if index2 == cut:
                cut += 87
                new_des_text += "-\n"
                des_pos += 10
                print("new line")
        container.bind("<Button>",lambda event: self.reserved_window(container,title))
        container.create_text((WINDOW_WIDTH // 2), 190, text="Description", font=("Justify", 10, "bold"), fill="white")
        container.create_text((WINDOW_WIDTH // 2), des_pos, text=f"{new_des_text}", font=("Justify", 12, "bold"),
                              fill="white")
        self.active_frame.create_window((WINDOW_WIDTH//2),y,window=container,height=400,width=(WINDOW_WIDTH-20))# insert container to the window
    def reserved_window(self,con,title):
        res_win = Canvas(con)

        res_win.create_image((WINDOW_WIDTH-20)//2-193,200,image=self.rev_bg) #creating button for reservation

        back_btn = res_win.create_image(20,20,image= self.back_image)

        res_win.create_text((WINDOW_WIDTH-20)//2-193,30,text=f"Reserve",font=("Times",18,"bold"))

        calen = Calendar(res_win,font=("Times",8),bordercolor="black",background="black",foreground="white",disabledbackground="brown",headersbackground='lightblue', selectbackground='skyblue')

        res_win.create_window((WINDOW_WIDTH-20)//2-193,150,window=calen)

        rev_btn = res_win.create_image((WINDOW_WIDTH-20)//2-193,300,image=self.rev1)
        res_win.tag_bind(rev_btn,"<Enter>",lambda event: res_win.itemconfig(rev_btn,image=self.rev2))
        res_win.tag_bind(rev_btn, "<Leave>", lambda event: res_win.itemconfig(rev_btn, image=self.rev1))
        res_win.tag_bind(rev_btn,"<Button>",lambda event: self.insert_reservation(title,self.active_user().get_name(),current_date,calen.get_date()))

        window_id = con.create_window(((WINDOW_WIDTH-20)//2)+193,200,window=res_win,width=(WINDOW_WIDTH-20)//2,height=400)
        res_win.tag_bind(back_btn, "<Button>", lambda event: con.bind("<Button>", con.delete(window_id)))
    # ================================== ADMIN
    def admin_top_bar(self):
        self.menu_img = create_img(20, 21, get_image("menu"))
        self.top_frame = Canvas(self.main_frame, height=40, bg="white")
        self.top_frame.pack(side=TOP, fill=X)
        self.menu_btn = Button(self.top_frame,
                               image=self.menu_img,
                               command=self.show_admin_menu,
                               bg="white",
                               relief="flat")
        self.menu_btn.image = self.menu_img
        self.menu_btn.pack(side=LEFT)
        self.top_frame.create_text((WINDOW_WIDTH // 2), 13, text=self.top_text.get(), font=("Times", 13, "bold"))
    def show_admin_menu(self):
        self.menu_frame = Canvas(self.main_frame, bg="white")
        # log out button
        logout = Button(self.menu_frame, image=self.logout_img, text="          Log out", compound=LEFT, relief=FLAT,
                        bg="white",
                        font=("Times", 10, "bold"), command=self.start_window)
        logout.pack(side=TOP, fill=X)
        logout.bind("<Enter>", lambda event: (
            logout.config(image=self.book_img2, bg="grey", highlightcolor="black", highlightbackground="black",
                          highlightthickness=1)))
        logout.bind("<Leave>", lambda event: (logout.config(image=self.logout_img, highlightthickness=0, bg="white")))
        # barrow table button
        barrow = Button(self.menu_frame, image=self.back_image, text="          Barrows", compound=LEFT, relief=FLAT,
                       bg="white",
                       font=("Times", 10, "bold"), command=self.books_window)
        barrow.pack(side=TOP, fill=X)
        barrow.bind("<Enter>", lambda event: (
            barrow.config(image=self.book_img2, bg="grey", highlightcolor="black", highlightbackground="black",
                         highlightthickness=1)))
        barrow.bind("<Leave>", lambda event: (barrow.config(image=self.logout_img, highlightthickness=0, bg="white")))

        self.menu_frame_id = self.main_frame.create_window(75, (WINDOW_HEIGTH // 2) + 30, window=self.menu_frame,
                                                           height=WINDOW_HEIGTH, width=150)

        # users button
        users = Button(self.menu_frame, image=self.users_img, text="          Users", compound=LEFT, relief=FLAT,
                        bg="white",
                        font=("Times", 10, "bold"), command=self.accounts_window)
        users.pack(side=TOP, fill=X)
        users.bind("<Enter>", lambda event: (
            users.config(image=self.book_img2, bg="grey", highlightcolor="black", highlightbackground="black",
                          highlightthickness=1)))
        users.bind("<Leave>", lambda event: (users.config(image=self.logout_img, highlightthickness=0, bg="white")))

        self.menu_frame_id = self.main_frame.create_window(75, (WINDOW_HEIGTH // 2) + 30, window=self.menu_frame,
                                                           height=WINDOW_HEIGTH, width=150)
        # books button
        books = Button(self.menu_frame, image=self.book_img, text="          Books", compound=LEFT, relief=FLAT,
                        bg="white",
                        font=("Times", 10, "bold"), command=self.activities_window)
        books.pack(side=TOP, fill=X)
        books.bind("<Enter>", lambda event: (
            books.config(image=self.book_img2, bg="grey", highlightcolor="black", highlightbackground="black",
                         highlightthickness=1)))
        books.bind("<Leave>", lambda event: (books.config(image=self.logout_img, highlightthickness=0, bg="white")))

        self.menu_frame_id = self.main_frame.create_window(75, (WINDOW_HEIGTH // 2) + 30, window=self.menu_frame,
                                                           height=WINDOW_HEIGTH, width=150)

        self.menu_btn.config(command=self.unshow_admin_menu, image=self.back_image)
        self.menu_btn.image = self.back_image
    def unshow_admin_menu(self):
        self.main_frame.delete(self.menu_frame_id)
        self.menu_btn.config(command=self.show_admin_menu, image=self.menu_img)

    def books_window(self):
        if self.top_frame:
            self.top_frame.pack_forget()
        self.top_text.set("Admin")
        self.close_active_frame()
        self.active_frame = Canvas(self.main_frame)
        self.admin_top_bar()
        # ================================================= table type
        top_label = Label(self.active_frame, pady=0, bd=0, text="Reserved Books")
        top_label.pack(side=TOP, fill=X)
        #================================================= TOP LEVEL

        top_label = Label(self.active_frame,pady=0,bd=0)
        top_label.pack(side=TOP,fill=X)
        title_L = Label(top_label,width=50,highlightcolor="grey", highlightbackground="grey",
                          highlightthickness=1,text="Book title")
        title_L.pack(side=LEFT,anchor=N,fill=Y)
        user_L = Label(top_label,width=25,highlightcolor="grey", highlightbackground="grey",
                          highlightthickness=1,text="User")
        user_L.pack(side=LEFT,anchor=N,fill=Y)
        date_barrow = Label(top_label,width=18,highlightcolor="grey", highlightbackground="grey",
                          highlightthickness=1,text="Date barrow")
        date_barrow.pack(side=LEFT,anchor=N,fill=Y)
        date_sauli = Label(top_label,width=18,highlightcolor="black", highlightbackground="black",
                          highlightthickness=1,text="Date return")
        date_sauli.pack(side=LEFT,anchor=N,fill=Y)
        # ================================================= data Row

        books_window = Canvas(self.active_frame, height=WINDOW_HEIGTH - 50,scrollregion=(0,0,500,500),bg="white")
        conn = sqlite3.connect("Barrow.db")
        c= conn.cursor()
        c.execute("SELECT * FROM barrow")
        position_Y = 11
        for data in c.fetchall():
            row = Canvas(self.active_frame)
            #row.pack(side=TOP,fill=X)
            Label(row, width=50,pady=4,padx=2, highlightcolor="grey", highlightbackground="grey",
                            highlightthickness=1, text=data[1][0:60]).pack(side=LEFT, anchor=N,fill=Y)
            Label(row, width=25,pady=4, highlightcolor="grey", highlightbackground="grey",
                           highlightthickness=1, text=data[2]).pack(side=LEFT, anchor=N,fill=Y)
            Label(row, width=18,pady=4, highlightcolor="grey", highlightbackground="grey",
                                highlightthickness=1, text=data[3]).pack(side=LEFT, anchor=N,fill=Y)
            Label(row, width=18,pady=4, highlightcolor="grey", highlightbackground="grey",
                               highlightthickness=1, text=data[4]).pack(side=LEFT, anchor=N,fill=Y)

            books_window.create_window((WINDOW_WIDTH//2)-4,position_Y,window=row,width=WINDOW_WIDTH)
            books_window.bind("<Configure>",
                            lambda e: row.configure(scrollregion=row.bbox("all")))
            books_window.bind_all("<MouseWheel>",
                                lambda event: books_window.yview_scroll(-1 * (event.delta // 120), "units"))
            position_Y+=23

        conn.commit()
        conn.close()
        books_window.pack(side="bottom",fill=X,expand=True,anchor=S)
        self.active_frame.pack(expand=True, fill=BOTH)

    def accounts_window(self):
        if self.top_frame:
            self.top_frame.pack_forget()
        self.top_text.set("Admin")
        self.close_active_frame()
        self.active_frame = Canvas(self.main_frame)
        self.admin_top_bar()
        # ================================================= table type
        top_label = Label(self.active_frame, pady=0, bd=0, text="Accounts Table")
        top_label.pack(side=TOP, fill=X)
        # ================================================= TOP LEVEL

        top_label = Label(self.active_frame, pady=0, bd=0)
        top_label.pack(side=TOP, fill=X)
        title_L = Label(top_label, width=38, highlightcolor="grey", highlightbackground="grey",
                        highlightthickness=1, text="Name")
        title_L.pack(side=LEFT, anchor=N, fill=Y)
        user_L = Label(top_label, width=38, highlightcolor="grey", highlightbackground="grey",
                       highlightthickness=1, text="Username")
        user_L.pack(side=LEFT, anchor=N, fill=Y)
        date_barrow = Label(top_label, width=30, highlightcolor="grey", highlightbackground="grey",
                            highlightthickness=1, text="Password")

        date_barrow.pack(side=LEFT, anchor=N, fill=Y)
        dale= Label(top_label, width=8, highlightcolor="grey", highlightbackground="grey",
                            highlightthickness=1, text="stat")

        dale.pack(side=LEFT, anchor=N, fill=Y)

        # ================================================= data Row

        books_window = Canvas(self.active_frame, height=WINDOW_HEIGTH - 50, scrollregion=(0, 0, 500, 500), bg="white")
        conn = sqlite3.connect("Accounts.db")
        c = conn.cursor()
        c.execute("SELECT * FROM accounts")
        position_Y = 11
        for data in c.fetchall():
            row = Canvas(self.active_frame)
            # row.pack(side=TOP,fill=X)
            Label(row, width=38,pady=4, padx=2, highlightcolor="grey", highlightbackground="grey",
                  highlightthickness=1, text=data[1]).pack(side=LEFT, anchor=N, fill=Y)
            Label(row, width=38,pady=4, highlightcolor="grey", highlightbackground="grey",
                  highlightthickness=1, text=data[2]).pack(side=LEFT, anchor=N, fill=Y)
            Label(row, width=30,pady=4, highlightcolor="grey", highlightbackground="grey",
                  highlightthickness=1, text=data[3]).pack(side=LEFT, anchor=N, fill=Y)
            Button(row, width=8, pady=2, highlightcolor="grey", highlightbackground="grey",
                  highlightthickness=2,bg="red",fg="white", text="del",command=lambda : self.delete(data[0],data[1]),relief="flat").pack(side=LEFT, anchor=N, fill=Y)

            books_window.create_window((WINDOW_WIDTH // 2) - 4, position_Y, window=row, width=WINDOW_WIDTH)
            books_window.bind("<Configure>",
                              lambda e: row.configure(scrollregion=row.bbox("all")))
            books_window.bind_all("<MouseWheel>",
                                  lambda event: books_window.yview_scroll(-1 * (event.delta // 120), "units"))


            position_Y += 23

        conn.commit()
        conn.close()
        books_window.pack(side="bottom", fill=X, expand=True, anchor=S)
        self.active_frame.pack(expand=True, fill=BOTH)
    def delete(self,acc_id,humiram):
        ask = messagebox.askyesnocancel("Delete","Do you want to delete this account?")
        if ask:
            print(acc_id,humiram)
            conn = sqlite3.connect("Accounts.db")
            c = conn.cursor()
            delete_acc = f"DELETE FROM accounts WHERE id={acc_id}"
            c.execute(delete_acc)
            conn.commit()
            conn.close()

            messagebox.showinfo("delete","Account successfully deleted")
            self.accounts_window()
        else:
            pass
    def activities_window(self):
        if self.top_frame:
            self.top_frame.pack_forget()
        self.top_text.set("Admin")
        self.close_active_frame()
        self.active_frame = Canvas(self.main_frame)
        self.admin_top_bar()
        # ================================================= table type
        top_label = Label(self.active_frame, pady=0, bd=0, text="Books Table")
        top_label.pack(side=TOP, fill=X)
        # ================================================= TOP LEVEL

        top_label = Label(self.active_frame, pady=0, bd=0)
        top_label.pack(side=TOP, fill=X)
        title_L = Label(top_label, width=28, highlightcolor="grey", highlightbackground="grey",
                        highlightthickness=1, text="Type")
        title_L.pack(side=LEFT, anchor=N, fill=Y)
        user_L = Label(top_label, width=45, highlightcolor="grey", highlightbackground="grey",
                       highlightthickness=1, text="title")
        user_L.pack(side=LEFT, anchor=N, fill=Y)
        date_barrow = Label(top_label, width=38, highlightcolor="grey", highlightbackground="grey",
                            highlightthickness=1, text="Author")
        date_barrow.pack(side=LEFT, anchor=N, fill=Y)
        # ================================================= data Row

        books_window = Canvas(self.active_frame, height=WINDOW_HEIGTH - 50, scrollregion=(0, 0, 0, 0), bg="white")
        conn = sqlite3.connect("Books.db")
        c = conn.cursor()
        c.execute("SELECT * FROM books")
        position_Y = 11
        for data in c.fetchall():
            row = Canvas(self.active_frame)
            # row.pack(side=TOP,fill=X)
            Label(row, width=28,pady=4, highlightcolor="grey", highlightbackground="grey",
                  highlightthickness=1, text=data[1]).pack(side=LEFT, anchor=N, fill=Y)
            Label(row, width=45,pady=4, highlightcolor="grey", highlightbackground="grey",
                  highlightthickness=1, text=data[2][0:55]).pack(side=LEFT, anchor=N, fill=Y)
            Label(row, width=38,pady=4, highlightcolor="grey", highlightbackground="grey",
                  highlightthickness=1, text=data[3]).pack(side=LEFT, anchor=N, fill=Y)
            books_window.create_window((WINDOW_WIDTH // 2) - 2, position_Y, window=row, width=WINDOW_WIDTH)
            position_Y += 23

        conn.commit()
        conn.close()
        books_window.pack(side="bottom", fill=X, expand=True, anchor=S)
        self.active_frame.pack(expand=True, fill=BOTH)

if __name__ == '__main__':
    root = Tk()
    geo = f"{WINDOW_WIDTH}x{WINDOW_HEIGTH}+250+50"
    root.geometry(geo)
    root.title("DR. JUAN A PASTOR MNHS LIBRARY MANAGEMENT SYSTEM")
    icon = create_img(20,20,"my_images/logo.jpg")
    root.iconphoto(True,icon)
    main_frame = Canvas(root,width=WINDOW_WIDTH,height=WINDOW_HEIGTH)
    main_frame.pack(fill=BOTH,expand=True)
    app = Library_app(main_frame)
    app.start_window()
    root.mainloop()
