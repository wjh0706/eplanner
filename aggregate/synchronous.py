# integrationservice.py

from flask import Flask, jsonify
import requests
import json
import logging
logging.basicConfig(filename='fetch_urls_synchronous.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
app = Flask(__name__)


urls={"auth":"http://18.206.88.110.nip.io/api/auth/user"
      ,
      "user":"http://ec2-18-118-30-126.us-east-2.compute.amazonaws.com:8012/",
      "event":"https://eplanner-event-mircro.wl.r.appspot.com/"}

def fetch_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Content of {url}: {response.text}")
        else:
            logging.error(f"Failed to fetch {url}. Status code: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")




if __name__ == '__main__':
    for each in urls:
        print(urls[each])
        fetch_url(urls[each])