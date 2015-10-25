import ConfigParser, logging, datetime, os

from flask import Flask, render_template, request

import mediacloud

CONFIG_FILE = 'settings.config'
basedir = os.path.dirname(os.path.realpath(__file__))

# load the settings file
config = ConfigParser.ConfigParser()
config.read(os.path.join(basedir, 'settings.config'))

# set up logging
log_file_path = os.path.join(basedir,'logs','mcserver.log')
logging.basicConfig(filename=log_file_path,level=logging.DEBUG)
logging.info("Starting the MediaCloud example Flask app!")

# clean a mediacloud api client
mc = mediacloud.api.MediaCloud( config.get('mediacloud','api_key') )

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("search-form.html")

@app.route("/search",methods=['POST'])
def search_results():
    keywords = request.form['keywords']
    now = datetime.datetime.now()
    results = mc.sentenceCount(keywords,
        solr_filter=[mc.publish_date_query( datetime.date( 2015, 1, 1), 
                                            datetime.date( now.year, now.month, now.day) ),
                     'media_sets_id:1' ])
    return render_template("search-results.html", 
        keywords=keywords, sentenceCount=results['count'] )

if __name__ == "__main__":
    app.debug = True
    app.run()
