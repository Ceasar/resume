import json

from staticjinja import make_renderer


def get_data(filename):
    with open(filename) as f:
        return json.loads(f.read())


def index_context():
    return {
        "education": get_data("data/education.json"),
        "identity": get_data("data/identity.json"),
        "projects": get_data("data/projects.json"),
        "positions": get_data("data/positions.json"),
        "languages": get_data("data/languages.json"),
        "technologies": get_data("data/technologies.json"),
    }


if __name__ == "__main__":
    renderer = make_renderer(
        contexts=[
            ('index.html', index_context),
        ],
    )
    renderer.run()
