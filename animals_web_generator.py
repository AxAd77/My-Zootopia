import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    animals_data = load_data("animals_data.json")

    with open("animals_template.html", "r") as handle:
        html_template = handle.read()

    output = ""

    for animal in animals_data:
        output += '<li class="cards__item">\n'
        output += f"Name: {animal['name']}<br/>\n"

        if "diet" in animal["characteristics"]:
            output += f"Diet: {animal['characteristics']['diet']}<br/>\n"

        if animal["locations"]:
            output += f"Location: {animal['locations'][0]}<br/>\n"

        if "type" in animal["characteristics"]:
            output += f"Type: {animal['characteristics']['type']}<br/>\n"

        output += "</li>\n"

    html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as handle:
        handle.write(html_content)


if __name__ == "__main__":
    main()
