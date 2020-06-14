import psycopg2

# num of 3D files per each part
num_3dFiles = 5

num_faces = 500 # max: num_3dFiles^4
num_hairs = 500
num_enemies = 1000
num_citizens = 1000 
num_npcs = num_citizens + num_enemies
num_players = 1500
num_regions = 50
num_coords = 1000
num_objects = 1000
num_exchanges = 1000
num_attacks = 1000
num_relatives = 500

skinColors = ["ffdbac", "f1c27d", "e0ac69", "c68642", "8d5524"]
weatherOptions = ["sunny", "cloudy", "windy", "rainy", "snowy", "foggy"]


# psql ahto
dbname = 'est_e8026580'
user = 'est_e8026580'
host = 'ahto.epsevg.upc.es'
password = 'dbe8026580'

# localhost
dbname = 'proj'
user = 'postgres'
host = 'localhost'
password = '1234'

# conn = psycopg2.connect("dbname='proj' user='postgres' host='localhost' password='1234'")
conn = psycopg2.connect(f"dbname='{dbname}' user='{user}' host='{host}' password='{password}'")
c = conn.cursor()
# c.execute("SET search_path TO practica")

