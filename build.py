import staticjinja
import json


def get_data(filename):
    with open(filename) as f:
        data = json.loads(f.read())
    return data


def index_context():
    return {
        "projects": get_data("data/projects.json"),
        "positions": get_data("data/positions.json"),
    }


if __name__ == "__main__":
    staticjinja.main(
        contexts=[
            ('index.html', index_context),
        ],
    #    autoreload=False
    )
