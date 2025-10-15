from flask import Flask, render_template,request
import requests
from config import NEWS_API_KEY
app=Flask(__name__)

@app.route("/")
def home():
    query=request.args.get('query','latest')
    url=f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response=requests.get(url)
    data=response.json()
    Articles=data.get("articles",[])
    return render_template("index.html",articles=Articles)
    
if __name__=="__main__":
    app.run('0.0.0.0',debug=True)
    
    
app.config["TEMPLATES_AUTO_RELOAD"] = True