# Frequency-of-repeating-the-word-taxi-in-Wikipedia-pages-for-the-largest-transportation-companies
- Extracting the word taxi from largest transportation companies pages from wekipedia, and store them in arangodb 


### This project is a demo to showcase how we can use a simple python server that has 4 endpoints

### I stored the ingested data in arangodb an open source MultiModel database (No SQL & Graph)

### Prerequisites
- Docker
- Docker Compose


#### To build the project simple run <code> docker compose up -d </code>

- After running project, Go to browser and type `localhost:8529`
- You will open the *arangodb* NoSQL DB.
- Write username: root
- Write password: 1234
- Choose Database: free-now


**The Endpoints:**

`/alive`:

- Description
> This endpoint aims to check if the server is up or not.

> curl request:

- <code> curl --location --request GET 'http://localhost:5001/alive' </code>


`/ingest_demo`:
- Description
> This endpoint aims to ingest the already written websites links into the *free-now* db.

> curl request:

- <code> curl --location --request GET 'http://localhost:5001/ingest_demo' </code>


**The already written websites which you will ingest them in to the db:**
- Uber
- Careem
- Free Now
- InDriver
- Gett
- Lyft
- Grab_
- Bolt_
- Via_Transportation
- Gojek
- Cabify



`/ingest`:
- Description
> This endpoint aims to test the server by adding any link you want to count the number of occurance of the word `taxi` in it if the database contains this link, it will not be added.

> curl reuquest:

> <code> curl --location --request POST 'http://localhost:5001/ingest' --header 'Content-Type: application/json' --data-raw '{"url":"https://en.wikipedia.org/wiki/Crazy_Taxi"}' </code>



`/analyze_taxi`:
- Description
> This endpoint aims to return the number of occurance of the word `taxi` in it alongside the link of the website if the database contains at least one link.

> curl reuquest:

> <code> curl --location --request GET 'http://localhost:5001/analyze_taxi'</code>




