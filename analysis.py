from arangoclient import client

def get_taxi_analysis():
    

    db = client.db("test-db", username="root", password="1234")

    if not db.has_collection("article"):
        return {}
    cursor = db.aql.execute('''for a in article
                               LET taxi_count = LENGTH(REGEX_SPLIT(a.content, " taxi ", true))-1
                               LET link = a.url
                               return { link , taxi_count}
    ''')
    result = [document for document in cursor]
    return result    
