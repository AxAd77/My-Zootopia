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

    taxonomy = animal_obj.get("taxonomy", {})
    characteristics = animal_obj.get("characteristics", {})

    if "scientific_name" in taxonomy:
        output += (
            f'        <strong>Scientific name:</strong> '
            f'{taxonomy["scientific_name"]}<br/>\n'
        )

    if "diet" in characteristics:
        output += (
            f'        <strong>Diet:</strong> '
            f'{characteristics["diet"]}<br/>\n'
        )

    if animal_obj["locations"]:
        locations = ", ".join(animal_obj["locations"])
        output += (
            f'        <strong>Location:</strong> '
            f'{locations}<br/>\n'
        )

    if "type" in characteristics:
        output += (
            f'        <strong>Type:</strong> '
            f'{characteristics["type"]}<br/>\n'
        )

    if "habitat" in characteristics:
        output += (
            f'        <strong>Habitat:</strong> '
            f'{characteristics["habitat"]}<br/>\n'
        )

    if "lifespan" in characteristics:
        output += (
            f'        <strong>Lifespan:</strong> '
            f'{characteristics["lifespan"]}<br/>\n'
        )

    if "weight" in characteristics:
        output += (
            f'        <strong>Weight:</strong> '
            f'{characteristics["weight"]}<br/>\n'
        )

    if "height" in characteristics:
        output += (
            f'        <strong>Height:</strong> '
            f'{characteristics["height"]}<br/>\n'
        )

    if "length" in characteristics:
        output += (
            f'        <strong>Length:</strong> '
            f'{characteristics["length"]}<br/>\n'
        )

    if "color" in characteristics:
        output += (
            f'        <strong>Color:</strong> '
            f'{characteristics["color"]}<br/>\n'
        )

    if "skin_type" in characteristics:
        output += (
            f'        <strong>Skin type:</strong> '
            f'{characteristics["skin_type"]}<br/>\n'
        )

    if "top_speed" in characteristics:
        output += (
            f'        <strong>Top speed:</strong> '
            f'{characteristics["top_speed"]}<br/>\n'
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
