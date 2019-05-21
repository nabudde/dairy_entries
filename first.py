#import the flask class
from flask import Flask, jsonify, request
#create an instance of the class
app = Flask(__name__)
#use route() decorator to tell flask which urls trigger our functions
diary = [ {
        "id": 1,
        "Title": "Swimming",
        "Description": "This is so goood",
        "Time": "2:00-3:00"
        },
         {
        "id": 2,
        "Title": "Reading",
        "Description": "goood",
        "Time": "2:00-3:00"
    }
    ]
@app.route('/api/v1/get_data', methods=['GET'])
def getData():
    for activity in diary:
        return jsonify({'diary_entries': activity})
@app.route('/api/v1/entry', methods=['POST'])
def insert():
    entry = {
        "id": diary[-1]["id"]+1,
        "Title": request.json["Title"],
        "Description": request.json["Description"],
        "Time": request.json["Time"]
    }
    diary.append(entry)
    return jsonify({'Activities': diary})
@app.route('/api/v1/entry/<int:entered_id>', methods=['GET'])
def specific(entered_id):
    for entry  in diary:
        if entry["id"]==entered_id:
            return jsonify({"specific_Activity":entry["Time"]})
@app.route('/api/v1/entry/<int:entered_id>', methods=['PUT'])
def update(entered_id):
    for act in diary:
        if act["id"]==entered_id:
            act["Title"]=request.json["Title"]
            act["Description"]=request.json["Description"]
            act["Time"]=request.json["Time"]
            return jsonify({"Task":diary})
            


if __name__ == '__main__':
    app.run(debug=True)