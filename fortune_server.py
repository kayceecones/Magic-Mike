from __future__ import annotations

import importlib.util
import random
from pathlib import Path

from flask import Flask, jsonify, render_template
from flask_cors import CORS

from fortune_list import FORTUNES_LIST


def _load_legacy_app() -> Flask | None:
    """Load app from legacy nested layout if present.

    Some deploys still have the application under ``Mikes_Python/fortune_server.py``.
    This compatibility loader lets ``gunicorn fortune_server:app`` keep working.
    """

    legacy_path = Path(__file__).resolve().parent / "Mikes_Python" / "fortune_server.py"
    if not legacy_path.exists():
        return None

    spec = importlib.util.spec_from_file_location("legacy_fortune_server", legacy_path)
    if spec is None or spec.loader is None:
        return None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    legacy_app = getattr(module, "app", None)
    if isinstance(legacy_app, Flask):
        return legacy_app

    return None


app = _load_legacy_app()

if app is None:
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def home():
        return render_template("magic_mike.html")

    @app.route("/fortune")
    def get_fortune():
        return jsonify({"fortune": random.choice(FORTUNES_LIST)})


if __name__ == "__main__":
    app.run(debug=True)
