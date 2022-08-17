import os
import markdown
import jinja2


def markdown_to_html(file_name: str) -> str:
    with open(file_name, "r") as file_pointer:
        return markdown.markdown(file_pointer.read())


def get_template(file_name: str) -> jinja2.Template:
    return jinja2.Template(open(file_name).read())


def a_link(name: str, link: str):
    return f'<a id="menu-item" href="{link}">{name}</a>'


def create_directories_for_path(path: str):
    split_path = path.split("/")

    split_path.pop()

    os.makedirs(os.path.join(*split_path), exist_ok=True)


def generate_pages(
    markdown_files: list[dict[str, str]],
    base_template: str,
    css_file: str,
    links: list[dict[str, str]],
    output_folder: str,
):
    os.makedirs(output_folder, exist_ok=True)
    template = get_template(base_template)

    menu_elements = [f'<p>{a_link(link["name"], link["url"])}</p>' for link in links]
    menu = f'<div id="menu">{"".join(menu_elements)}</div>'

    for md_file in markdown_files:
        html_file_path = os.path.join(output_folder, md_file["html_file"])
        create_directories_for_path(html_file_path)

        with open(html_file_path, "w+") as html_file_pointer:
            html_file_pointer.write(
                template.render(
                    page_title=md_file["name"],
                    menu=menu,
                    body=markdown_to_html(md_file["md_file"]),
                )
                + f"\n<style>\n{open(css_file).read()}\n</style>\n"
            )
