from flask import Flask
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():

    name = "Ayush Kumar Sinha"  
    username = subprocess.getoutput('whoami')
    server_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput('top -b -n 1 | head -n 20')  # Get top output

    response = f"""
    <pre>
    Name: {name}
    Username: {username}
    Server Time (IST): {server_time}
    Top Output:
    {top_output}
    </pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
