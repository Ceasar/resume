import json

from staticjinja import make_renderer


def get_data(filename):
    with open(filename) as f:
        return json.loads(f.read())


def index_context():
    return get_data("data/resume.json")


if __name__ == "__main__":
    renderer = make_renderer(
        contexts=[
            ('index.html', index_context),
        ],
    )
    renderer.run()
