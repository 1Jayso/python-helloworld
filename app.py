from flask import Flask, jsonify, json
import logging


app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("You've successfully reached the index of the application, Hurray!!!")
    return "Hello World! There are two endpoints in this app: /metrics and /status"

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Status request successful')


    return response

@app.route("/metric")
def metric():
    return jsonify(data="UserCount: 140, UserCountActive: 23"),200

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Metrics request successful')

    return response




logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG)




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


