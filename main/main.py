import os
from flask import Flask
from google.cloud import storage
import pandas as pd

app = Flask(__name__)

#replace with secret on deploy
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'placeholder'


@app.route('/')
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    return f'Hi, {name}'  # Press ⌘F8 to toggle the breakpoint.


def read_bucket():
    #TODO: parameterise function
    client = storage.Client()

    bucket = client.get_bucket('anthony-source')
    blob = bucket.blob('test.csv')
    df = pd.read_csv(blob.open('rb'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(print_hi('PyCharm'))
    port = int(os.environ.get('PORT', 8080))
    read_bucket()
    app.run(host='0.0.0.0', port=port)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
