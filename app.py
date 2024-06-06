from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define a route that serves the index.html file
@app.route('/')
def home():
    return render_template('index.html')

# Define a route that serves the index.html file
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Check if the script is run directly (not imported as a module)
@app.route('/education')
def edu():
    return render_template('education.html')

@app.route('/projects')
def port():
    return render_template('Portfolio.html')


if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
