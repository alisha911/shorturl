# An URL shortener is a website that reduces the length of your URL. 
# The idea is to minimize the web page address into something that's easier to remember and track.


from flask import *
import requests
from werkzeug.datastructures import Headers

app = Flask(__name__)

@app.route('/')
def index():
    # if(request.cookies.get('short_url')):
    #     cookie =request.cookies.get('short_url')
    # else:
    #     cookie =""
    # return render_template('index.html',cookie=cookie)
    return render_template('index.html')

# @app.route('/status')
# def stat():
#     return render_template('status.html')

@app.route('/public/<path:path>')
def send_js(path):
    return send_from_directory('public',path)




#the code for writen for coonecting bitly website and return short url to index page 
@app.route('/formData',methods=['POST'])
def formData():
    formUrlData = request.form['url']
    # r = requests.get("http://ipinfo.io/json")
    # data = r.json()  
    # # return data['city']
    # return formUrlData
    header = {
    'Authorization': 'Bearer 937129a21d4f9cf747a9f3ca76fa7816f87137c7',
    'Content-Type': 'application/json',
    }
    params={
        "long_url" :  formUrlData
    }
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=header, json=params)
    data = response.json()
    res = make_response(render_template("index.html",datar=data))
    res.set_cookie('short_url', data['link'], max_age=12*60*60*1)
    return res
    

    
    # return data['link']
    
if __name__ == '__main__':
    app.run(debug = True)

