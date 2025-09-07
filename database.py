# This library lets python talk to postgresql database
import psycopg2

def get_connection():  
    #Connects to the postgresql database and returns connection object
    #Call this function when ever you need to interact with the database
    
    return psycopg2.connect(         #opens connection to postgresql
        dbname="expense_tracker",    #database name 
        user="postgres",             #databaase username
        password="123qweasdzxc",     #database password
        host="localhost",            #server (localhost means your own pc)
        port="5432"                  #postgresql port (default is 5432)
    )




