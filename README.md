# flask-calc
Example project for demonstration flask-restful 


# EXAMPLE

* curl 'http://127.0.0.1:5000/calc/'
    > {
    >     "result": true
    > }


* curl -H "Content-type: application/json" -X POST -d '{"one": 2, "two": 2}' 'http://127.0.0.1:5000/calc/sum'
    > {
    >     "result": 4
    > }

