from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('scrubbed.csv',low_memory=False)

@app.route('/')
def getRandomEntry():
    df_elements = df.sample(n=1)
    df_dict = df_elements.to_dict(orient='dict')
    df_ret = {}
    for k in df_dict:
        df_ret[k] = list(df_dict[k].values())[0]
    return jsonify(df_ret)

# if __name__ == '__main__':
#     app.run(debug=True)