from flask import Flask
from ipynbsrv.hostapi.http.routes.containers import blueprint as containers
from ipynbsrv.hostapi.http.routes.containers_snapshots import blueprint as snapshots
import sys

'''
'''
def main():
    app = Flask(__name__)
    app.secret_key = "uk1`\x15%\xdcl;\x8b\xa1\x9aK\x85\xa9\xd3@Fs\xdcQku\xf4"

    app.register_blueprint(snapshots)
    app.register_blueprint(containers)

    app.run(debug=True, host='0.0.0.0', port=49160)


if __name__ == "__main__":
    sys.exit(main())
