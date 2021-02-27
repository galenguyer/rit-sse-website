"""
Primary entry point for the app
"""

from api import APP

if __name__ == "__main__":
    APP.run(host=APP.config["IP"], port=int(APP.config["PORT"]))