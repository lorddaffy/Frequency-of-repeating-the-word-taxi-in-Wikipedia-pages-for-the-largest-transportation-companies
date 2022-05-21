from flask import request, make_response, Flask, Response
import json
from ingestion import ingest_new_article
from arangoclient import setup_db
from analysis import get_taxi_analysis

app = Flask(__name__)


@app.route('/alive', methods=['GET'])
def alive():
    return make_response('server is up and running', 200)

@app.route('/ingest_demo', methods= ['GET'])
def ingest_demo():
    taxi_links=['https://en.wikipedia.org/wiki/Uber','https://en.wikipedia.org/wiki/Careem','https://en.wikipedia.org/wiki/Free_Now_(service)','https://en.wikipedia.org/wiki/InDriver','https://en.wikipedia.org/wiki/Gett','https://en.wikipedia.org/wiki/Lyft','https://en.wikipedia.org/wiki/Grab_(company)','https://en.wikipedia.org/wiki/Bolt_(company)','https://en.wikipedia.org/wiki/Via_Transportation','https://en.wikipedia.org/wiki/Gojek','https://en.wikipedia.org/wiki/Cabify']
    for link in taxi_links:
        if not ingest_new_article(link):
            return make_response("Failed to add new data", 409)

    return make_response("Data inserted Succeessfully", 201)                 

@app.route('/ingest', methods=['POST'])
def ingest():
    json_data = request.get_json()
    wiki_link = json_data["url"]
    if ingest_new_article(wiki_link):
        return make_response("Data inserted Succeessfully", 201)
    else:
        return make_response("Failed to add new data", 500)    

@app.route('/analyze_taxi', methods=['GET'])
def analyze_taxi():
    data = get_taxi_analysis()
    if data == {}:
        return make_response("error occured while performing analysis, 500")
    else:
        resp = Response(json.dumps(data))
        resp.status_code = 200
        return resp


# Create the main driver function
if __name__ == '__main__':
    setup_db()
    app.run(debug=False, host='0.0.0.0', port=5001)
