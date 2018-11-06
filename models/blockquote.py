
class BlockQuote:

    def __init__(self, value):
        self.value = self.parse(value)

    def get_level_count_and_character_remove_count(self, line):

        level_count = 0
        character_remove_count = 0

        for character in line:
            if character == '>':
                level_count += 1
                character_remove_count += 1
            elif character == ' ':
                character_remove_count += 1
                continue
            else:
                break
        
        return (level_count, character_remove_count)

    def does_line_have_equal_or_greater_block_quote_level(self, line, block_quote_level):
        level_count, temp = self.get_level_count_and_character_remove_count(line)

        return level_count >= block_quote_level

    def parse(self, value):

        line_list = value.split('\n')
        line_list_stripped = []

        block_quote_level = 1
        block_quote_pushes = 0

        line_list_length = len(line_list)

        for index in range(line_list_length):

            line = line_list[index]

            level_count, character_remove_count = self.get_level_count_and_character_remove_count(line)

            if level_count > block_quote_level:
                block_quote_level = level_count
                line_list_stripped.append('<blockquote>')
                block_quote_pushes += 1

            stripped_line = line[character_remove_count:].strip()
            line_list_stripped.append(stripped_line)

            is_not_last_line = index != (line_list_length - 1)
            next_line_has_equal_or_greater_block_quote_level = is_not_last_line and self.does_line_have_equal_or_greater_block_quote_level(line_list[index + 1], block_quote_level)

            if level_count == 0 and is_not_last_line and next_line_has_equal_or_greater_block_quote_level:
                line_list_stripped.append('</blockquote><blockquote>')

        if block_quote_pushes > 0:
            line_list_stripped.append('</blockquote>' * block_quote_pushes)

        return_str = ''

        for item in line_list_stripped:
            if item == '<blockquote>' or item == '</blockquote>':
                return_str += item
            else:
                return_str += f'{item} '

        return return_str

    def to_html(self):
        return f'<blockquote>{self.value}</blockquote>'

    def __str__(self):
        return self.to_html()

    def __repr__(self):
        return self.to_html()