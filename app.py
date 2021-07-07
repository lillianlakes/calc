from flask import Flask, request
import operations

app = Flask(__name__)

@app.route("/")
def root_route():
    """make a simple page for root of the webapp"""
    html = """<html>
                    <body>
                        <h1>hello</h1>
                    </body>
                </html>"""

    return html
    
@app.route("/add")
def add_from_query():
    """takes in two arguments from request queries and adds them."""
    a = request.args.get("a")
    b = request.args.get("b")
    try:
        result = operations.add(int(a),int(b))
        html = f"""<html>
                <body>
                    <h1>{result}</h1>
                </body>
            </html>"""
    except:
        html = """<html>
                <body>
                    <h1>no arguments given</h1>
                </body>
            </html>"""
    # print(test)

                
    return html
    
@app.route("/sub")
def subtract_from_query():
    """takes in two arguments from request queries and subtracts them."""
    a = request.args.get("a")
    b = request.args.get("b")
    try:
        result = operations.sub(int(a),int(b))
        html = f"""<html>
                <body>
                    <h1>{result}</h1>
                </body>
            </html>"""
    except:
        html = """<html>
                <body>
                    <h1>no arguments given</h1>
                </body>
            </html>"""
    # print(test)

                
    return html
    
@app.route("/mult")
def multiply_from_query():
    """takes in two arguments from request queries and multiplies them."""
    a = request.args.get("a")
    b = request.args.get("b")
    try:
        result = operations.mult(int(a),int(b))
        html = f"""<html>
                <body>
                    <h1>{result}</h1>
                </body>
            </html>"""
    except:
        html = """<html>
                <body>
                    <h1>no arguments given</h1>
                </body>
            </html>"""
    # print(test)

                
    return html
    
@app.route("/div")
def divide_from_query():
    """takes in two arguments from request queries and divides them."""
    a = request.args.get("a")
    b = request.args.get("b")
    try:
        result = operations.div(int(a),int(b))
        html = f"""<html>
                <body>
                    <h1>{result}</h1>
                </body>
            </html>"""
    except:
        html = """<html>
                <body>
                    <h1>no arguments given</h1>
                </body>
            </html>"""
    # print(test)
                
    return html