from flask import Flask,request,jsonify,make_response
import util
app=Flask(__name__)
@app.route("/")
def home():
    return "Welcome to Annadata"

@app.route("/suggest",methods=["POST"])
def suggest():
    N=int (request.form['N'])
    P=int(request.form['P'])
    K=int(request.form['K'])
    temp=int(request.form['temp'])
    humi=int(request.form['humi'])
    ph=int(request.form['ph'])
    rainfall=int(request.form['rainfall'])
    if(int(N)<10 or int(P)<10 or int(K)<10 or int(temp)<10 or int(humi)<10 or int(ph)>14 or int(rainfall)<10):
        response=jsonify({
            "suggestion":None,
            "error":"Enter proper values"
        })
        response=make_response(response)
        response.status_code=404
        response.headers.add("Access-Control-Allow-Origin","*")
        return response
    response=jsonify({
        "suggestion":util.suggest(N,P,K,temp,humi,ph,rainfall)
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    
    return response




































if __name__=="__main__":
    app.run(debug=True)