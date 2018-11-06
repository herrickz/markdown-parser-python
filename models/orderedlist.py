
class OrderedList:

    def __init__(self, value):
        self.list_item_list = value.split('\n')

    def to_html(self):
        list_item_string = ''

        for item in self.list_item_list:
            list_item_string += f'<li>{item.strip()}</li>'

        return f'<ul>{list_item_string}</ul>'