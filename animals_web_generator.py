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
    output += '    <div class="card__text">\n'
    output += '        <ul class="card__details">\n'

    taxonomy = animal_obj.get("taxonomy", {})
    characteristics = animal_obj.get("characteristics", {})

    if "scientific_name" in taxonomy:
        output += (
            f'            <li class="card__detail">'
            f'<strong>Scientific name:</strong> '
            f'{taxonomy["scientific_name"]}</li>\n'
        )

    if "diet" in characteristics:
        output += (
            f'            <li class="card__detail">'
            f'<strong>Diet:</strong> '
            f'{characteristics["diet"]}</li>\n'
        )

    if animal_obj["locations"]:
        locations = ", ".join(animal_obj["locations"])
        output += (
            f'            <li class="card__detail">'
            f'<strong>Location:</strong> '
            f'{locations}</li>\n'
        )

    if "type" in characteristics:
        output += (
            f'            <li class="card__detail">'
            f'<strong>Type:</strong> '
            f'{characteristics["type"]}</li>\n'
        )

    if "habitat" in characteristics:
        output += (
            f'            <li class="card__detail">'
            f'<strong>Habitat:</strong> '
            f'{characteristics["habitat"]}</li>\n'
        )

    if "lifespan" in characteristics:
        output += (
            f'            <li class="card__detail">'
            f'<strong>Lifespan:</strong> '
            f'{characteristics["lifespan"]}</li>\n'
        )

    if "weight" in characteristics:
        output += (
            f'            <li class="card__detail">'
            f'<strong>Weight:</strong> '
            f'{characteristics["weight"]}</li>\n'
        )

    if "height" in characteristics:
        output += (
            f'            <li class="card__detail">'
            f'<strong>Height:</strong> '
            f'{characteristics["height"]}</li>\n'
        )

    if "length" in characteristics:
        output += (
            f'            <li class="card__detail">'
            f'<strong>Length:</strong> '
            f'{characteristics["length"]}</li>\n'
        )

    if "color" in characteristics:
        output += (
            f'            <li class="card__detail">'
            f'<strong>Color:</strong> '
            f'{characteristics["color"]}</li>\n'
        )

    if "skin_type" in characteristics:
        output += (
            f'            <li class="card__detail">'
            f'<strong>Skin type:</strong> '
            f'{characteristics["skin_type"]}</li>\n'
        )

    if "top_speed" in characteristics:
        output += (
            f'            <li class="card__detail">'
            f'<strong>Top speed:</strong> '
            f'{characteristics["top_speed"]}</li>\n'
        )

    output += "        </ul>\n"
    output += "    </div>\n"
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
