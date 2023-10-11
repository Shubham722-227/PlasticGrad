import os
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_tsv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter='\t')
        return [row for row in reader]

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'degraders_list.tsv')
degraders_list = read_tsv_file(file_path)

@app.route('/', methods=['GET', 'POST'])
def display_degraders():
    if request.method == 'POST':
        search_option = request.form['search_option']
        search_value = request.form['search_value'].strip()
        if search_value:
            parts_table = [row for row in degraders_list if row[search_option].lower().startswith(search_value.lower())]
        else:
            parts_table = []
    else:
        parts_table = []

    return render_template('degraders.html', parts_table=parts_table)

if __name__ == "__main__":
    app.run(debug=True)
