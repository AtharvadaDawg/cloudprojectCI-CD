from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World - Google App Engine</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            color: #333;
        }
        .card {
            background: #ffffff;
            padding: 40px 48px;
            border-radius: 16px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.25);
            text-align: center;
            max-width: 520px;
        }
        .gcp-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background-color: #e8f0fe;
            color: #1a73e8;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 20px;
        }
        h1 {
            color: #202124;
            font-size: 32px;
            margin: 0 0 12px;
        }
        p {
            color: #5f6368;
            font-size: 16px;
            line-height: 1.6;
            margin: 0 0 24px;
        }
        .status-pill {
            display: inline-block;
            background-color: #e6f4ea;
            color: #137333;
            padding: 6px 14px;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 500;
        }
        .footer {
            margin-top: 25px;
            font-size: 12px;
            color: #80868b;
            border-top: 1px solid #dadce0;
            padding-top: 15px;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="gcp-badge">
            <span>&#9729;</span> Google Cloud Platform &bull; App Engine
        </div>
        <h1>Hello, World!</h1>
        <p>This web application is successfully developed and hosted using <strong>Google App Engine (GAE)</strong> with the Python Flask framework.</p>
        <div class="status-pill">&#10003; Server Status: Online &amp; Healthy</div>
        <div class="footer">
            Cloud Computing Practical No. 8 &bull; App Engine Demonstration
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def hello_world():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
