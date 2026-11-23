import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes a single animal into an HTML card."""
    output = ""
    output += '<li class="cards__item">\n'
    output += f'    <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '    <p class="card__text">\n'

    if "diet" in animal_obj["characteristics"]:
        output += (
            f'        <strong>Diet:</strong> '
            f'{animal_obj["characteristics"]["diet"]}<br/>\n'
        )

    if animal_obj["locations"]:
        output += (
            f'        <strong>Location:</strong> '
            f'{animal_obj["locations"][0]}<br/>\n'
        )

    if "type" in animal_obj["characteristics"]:
        output += (
            f'        <strong>Type:</strong> '
            f'{animal_obj["characteristics"]["type"]}<br/>\n'
        )

    output += "    </p>\n"
    output += "</li>\n"

    return output


def main():
    animals_data = load_data("animals_data.json")

    with open("animals_template.html", "r") as handle:
        html_template = handle.read()

    output = ""

    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    html_content = html_template.replace(
        "__REPLACE_ANIMALS_INFO__", output
    )

    with open("animals.html", "w") as handle:
        handle.write(html_content)


if __name__ == "__main__":
    main()
