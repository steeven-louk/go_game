import pymongo

url = "mongodb+srv://steevenlouksl:projet_ecole@ecole-projet.wjo1dwf.mongodb.net/"
client = pymongo.MongoClient(url)
db = client['go_game']