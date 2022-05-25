from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for,current_app
from joblib import load
from get_tweets import get_related_tweets

pipeline = load("text_classification.joblib")


def requestResults(name):
    tweets = get_related_tweets(name)
    tweets['prediction'] = pipeline.predict(tweets['tweet_text'])
    # data = str(tweets.prediction.value_counts()) + '\n\n'
    return tweets


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/home')
def home_page():
    return render_template('home.html')
    


@app.route('/<about>')
def about(about):
    return render_template('about.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    # print(current_app.root_path)
    if request.method == 'POST':
        user = request.form['search']
        # redirectString = "https://twitter-hate.herokuapp.com/"+"success/"+user
        # return redirect(redirectString)
        return redirect(url_for('success', name=user ))

        # if(request.url_root == "http://localhost:5000/--"):
        #     return redirect(url_for('success', name=user ,_external=True))
        # else:
        #     redirectString = "https://twitter-hate.herokuapp.com/"+"success/"+user
        #     return redirect(redirectString)  
@app.route('/success/<name>')
def success(name):
    res = requestResults(name)
    pred = res['prediction'].tolist()
    data = res['tweet_text'].tolist()
    tweet_id = res['tweet_id'].tolist()
    n = len(data)
    return render_template('result.html', pred=pred, data=data, key = name, n = n, tweet_id = tweet_id)

if __name__ == '__main__' :
    app.run()