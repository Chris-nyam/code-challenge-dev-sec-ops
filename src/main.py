import hashlib

from flask import Flask

app = Flask(__name__)


def get_hash(value: str) -> str:
    """Calculates the sha1 hash of a string.

    Args:
        value: the string to use when creating the sha1 hash.

    Returns:
        A sha1 hash of the given value.
    """
    return hashlib.sha1(value.encode("utf-8")).hexdigest()


@app.route("/", methods=["GET"])
def index() -> str:
    return "Hello, World!"


@app.route("/hash/<path:value>", methods=["POST"])
def hast_value(value: str) -> str:
    return get_hash(value)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
