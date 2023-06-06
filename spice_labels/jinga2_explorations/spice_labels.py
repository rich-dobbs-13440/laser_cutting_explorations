from jinja2 import Environment, FileSystemLoader


def populate_3d_array(values, rows, columns):
    total_cells = rows * columns
    num_pages = (len(values) + total_cells - 1) // total_cells

    array_3d = []
    for page in range(num_pages):
        page_values = values[page * total_cells:(page + 1) * total_cells]
        page_array = [[page_values[i * columns + j] if i * columns + j < len(page_values) else None
                       for j in range(columns)]
                      for i in range(rows)]
        array_3d.append(page_array)

    return array_3d


spices = [
    "Allspice",
    "Basil",
    "Cardamom",
    "Cayenne",
    "Chili Powder",
    "Cinnamon",
    "Cloves",
    "Coriander",
    "Cumin",
    "Curry Powder",
    "Dill",
    "Fennel",
    "Garlic Powder",
    "Ginger",
    "Nutmeg",
    "Onion Powder",
    "Oregano",
    "Paprika",
    "Parsley",
    "Red Pepper Flakes",
    "Rosemary",
    "Saffron",
    "Rubbed Sage",
    "Tarragon",
    "Ground Thyme",
    "Thyme Leaves",
    "Turmeric",
    "Vanilla",
    "White Pepper",
    "Black Pepper",
    "Salt",
    "Fennel Seed",
    "Fajita Seasoning",
    "Marjoram",
    "Caraway Seed",
    "Orange Peel",
    "Herbe De Provence",
    "Celery Seed"
]

# Print the list of spices
print_list = False
if print_list :
    for spice in spices:
        print(spice)

rows = 4
columns = 4

spices_array = populate_3d_array(spices, rows, columns)
print_array = False
if print_array:
    for page, page_array in enumerate(spices_array):
        print(f"Page {page + 1}:")
        for row in page_array:
            print(row)
        print()   




# Create the Jinja environment
env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)

# Render the template
page_number = 1  # Replace with the actual page number variable
template = env.get_template('layout.svg')
rendered_svg = template.render(
    container_width=400,
    container_height=300,
    rows=rows,
    columns=columns,
    spice_names_for_page=spices_array[page_number],
    fixed_spacing_width = 50,
    fixed_spacing_height = 10,
)

# Output the rendered SVG
# print(rendered_svg)  



filename = f"spice_labels_page_{page_number}.svg"

with open(filename, "w") as file:
    file.write(rendered_svg)
