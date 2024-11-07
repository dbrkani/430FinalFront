import mysql.connector
import bcrypt

from flask import jsonify

# =======================GLOBAL VARS=======================
ERROR_EMAIL_NOTFOUND = f"EMAIL %s NOT FOUND IN OUR SYSTEM. PLEASE REGISTER OR USE A DIFFERENT EMAIL"


# =======================SQL ACTIONS=======================

mydb = mysql.connector.connect(#could potentially make this configurable with global vars
    host = "localhost",
    user = "root",
    password = "1234",
    database = "csc430"
)
cursor = mydb.cursor()

#call to close connection to db
def close_conn_2_db():
    cursor.close()
    mydb.close() 

def pull_product_list():
    QUERY = "select * from product"
    cursor.execute(QUERY)
    result = cursor.fetchall()
    print(result) #debug , comment when finished
    return jsonify(result)


    
# ======================= Cart Functions ==========================
#assign user to cart table, try NOT to thread this with other existing carts
def assign_to_cart(users_id):
    
    QUERY = f"insert into cart ({users_id})"
    SEL_QUERY = f"select users_email from users where users_id = {users_id}" #match user email to passed id
    
    users_email = cursor.execute(SEL_QUERY)

    cursor.execute(QUERY)#insert user_id of passed u_id into cart table

    mydb.commit()

#updates the current cart to be the most recently created cart
def current_cart_db_update(users_email):
    
    MOST_RECENT_CART_QUERY = f"""update users
    set current_cart_id = (select max(cart_id) from cart where cart.users_id = users.users_id)
    where users_email = {users_email}
    """

    cursor.execute(MOST_RECENT_CART_QUERY)

# ======================= User & Account Functions ==========================

def hash_password(password):
    salt = bcrypt.gensalt()#generates a salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)# Hashs the password with the salt after converting it into binary
    return hashed_password #returns the now hased password

def create_user(input_name,input_email,input_password):
    input_password = hash_password(input_password) #hash our example password
    users_data = (input_name,input_email,input_password)
    #list of sql queries to commit new user info to db
    q1 = f"""insert into users (users_name,users_email,users_password) values ({input_name},{input_email},{input_password});
            select users_id from users where users_email = {input_email};"""
    q2 = f"""insert into cart (users_id) values (%s);
            update users set current_cart_id = (select max(cart_id) from cart where cart.users_id = users.users_id) where users_id = %s;"""
    try:
        cursor.execute("start transaction;")
        cursor.execute(q1)
    except:
        print("Account creation failed: EMAIL IN USE . Please login")

    result = cursor.fetchall() #should always return only 1 row
    for row in result:
        current_users_id = row[0] #user id to store in session (will be returned by function if we want to automatically log someone in to the account they created.)
    cursor.execute(q2)
    mydb.commit()

    return current_users_id

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)#turns the password into binary and then compares it with the hashed password

def u_login(email,password, hashed_password):
    EMAIL_QUERY = f"select users_email from users where users_email = {email} ;"

    try:
        cursor.execute(EMAIL_QUERY)
    except:
        return jsonify(ERROR_EMAIL_NOTFOUND)