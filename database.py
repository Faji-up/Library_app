import sqlite3

#conn = sqlite3.connect("Books.db")
#conn = sqlite3.connect("Accounts.db")
conn = sqlite3.connect("Barrow.db")
c = conn.cursor()
#c.execute("CREATE TABLE books(id INTEGER PRIMARY KEY,type text, book_name text,author text,description text)")
#c.execute("DROP TABLE books")
#c.execute("CREATE TABLE accounts(id INTEGER PRIMARY KEY,name text,username text,password text)")
#c.execute("DROP TABLE books")
#c.execute("DROP TABLE accounts")
#c.execute("DELETE FROM accounts")
book = ["PHILOSOPHY",
        "40 Arguments to Avoid: Short Logic Lessons for Servant-Leaders. New Day Publishers.",
        "Espiritu, D. L. (2014)",
        "Espiritu's book appears to offer concise logic lessons with practical applications for servant-leaders. It may present common logical fallacies or flawed arguments to avoid, aiming to enhance critical thinking and reasoning skills for individuals in leadership roles."
        ]
#c.executemany("INSERT INTO books (type,book_name,author,description) VALUES (?,?,?,?)",(book,))
#c.execute("CREATE TABLE barrow(id INTEGER PRIMARY KEY,book_title text,humiram text,hiniram DATE,sauli DATE)")
#c.execute("DROP TABLE barrow")
c.execute("DELETE FROM barrow")
#c.execute("DELETE FROM books WHERE id = 5")
conn.commit()
conn.close()