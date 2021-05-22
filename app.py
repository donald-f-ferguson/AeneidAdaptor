"""
Copyright @Donald F. Ferguson, 2021

This file is part of the application template for W4111, Section 002, Spring 21 HW assignments 3 and 4.

app.py is the 'main program.'

"""
import json

# DFF TODO -- Not critical for W4111, but should switch from print statements to logging framework.
from datetime import datetime

#
# These packages provide functions for deliverying a web application using Flask.
# Students can look online for education resources.
#
from flask import Flask, Response, request


#
# Create the Flask application object.
app = Flask(__name__)



##################################################################################################################

# DFF TODO A real service would have more robust health check methods.
# This path simply echoes to check that the app is working.
# The path is /health and the only method is GETs
@app.route("/health", methods=["GET"])
def health_check():
    rsp_data = {"status": "healthy", "time": str(datetime.now())}
    rsp_str = json.dumps(rsp_data)
    rsp = Response(rsp_str, status=200, content_type="app/json")
    return rsp



if __name__ == '__main__':
    #host, port = ctx.get_host_and_port()

    # DFF TODO We will handle host and SSL certs different in deployments.
    app.run(host="0.0.0.0", port=80)
