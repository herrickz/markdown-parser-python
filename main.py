
import os
from markdownparser import MarkdownParser
from models.codeblock import CodeBlock

markdown_parser = MarkdownParser()

def get_header():

    header_string = ''

    main_script_path = os.path.abspath(__file__)
    main_script_directory = os.path.split(main_script_path)[0]
    head_relative_file_path = 'html/head.html'

    header_file_absolute_path = os.path.join(main_script_directory, head_relative_file_path)

    with open(header_file_absolute_path, 'r') as header_file:
        header_string = header_file.read()

    return header_string

def get_scripts():

    script_string = ""

    main_script_path = os.path.abspath(__file__)
    main_script_directory = os.path.split(main_script_path)[0]
    scripts_relative_file_path = 'html/scripts.html'

    header_file_absolute_path = os.path.join(main_script_directory, scripts_relative_file_path)

    with open(header_file_absolute_path, 'r') as script_file:
        script_string = script_file.read()

    return script_string

code_block_list = []
code_block_length = 0

output_string = '<html>'
output_string += get_header()
output_string += '<body class="container">'

for item in markdown_parser.parse():
    if isinstance(item, CodeBlock):
        output_string += item.to_html()
        code_block_list.append(item)

    else:
        output_string += item.to_html() + '\n'

output_string += get_scripts()

for code_block in code_block_list:
    output_string += code_block.get_script_initializer()

output_string += '</body></html>\n'

with open('output.html', 'w') as output_file:
    output_file.write(output_string)