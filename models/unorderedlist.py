
class UnorderedList:

    def __init__(self, value):
        self.unordered_list_item_list = value.split('\n')

    def to_html(self):
        unordered_list_string = ''

        for item in self.unordered_list_item_list:
            unordered_list_string += f'<li>{self.clean_unordered_list_item(item)}</li>'

        return f'<ul>{unordered_list_string}</ul>'

    def clean_unordered_list_item(self, item):
        return item.replace('-', '', 1).strip()