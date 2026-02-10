
from flask import Flask, render_template, jsonify
from data import EVENT_INFO, get_schedule_with_speakers

app = Flask(__name__)

@app.route('/')
def index():
    schedule = get_schedule_with_speakers()
    return render_template('index.html', event=EVENT_INFO, schedule=schedule)

@app.route('/api/search')
def search():
    # Example API endpoint if we wanted client side dynamic fetching, 
    # but we will likely just render everything and filter client-side for simplicity/speed on limited items.
    schedule = get_schedule_with_speakers()
    return jsonify(schedule)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
