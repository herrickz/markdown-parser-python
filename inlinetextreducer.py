
import re

class InlineTextReducer:

    def inline_text_reduce_strike(self, string_to_reduce):

        match_italic = re.search(r'((?<!\*)\*[^\s\*].+?[^\s\*]\*)|(\*(\*\*){1,}[^\s].*?[^\s](\*\*){1,}\*)', string_to_reduce)

        while match_italic != None:

            before_match_text = string_to_reduce[:match_italic.start()]
            stripped_italic_inner_text = string_to_reduce[match_italic.start()+1 : match_italic.end()-1]
            after_match_text = string_to_reduce[match_italic.end():]

            italic_text = f'<em>{stripped_italic_inner_text}</em>'

            string_to_reduce = before_match_text + italic_text + after_match_text

            match_italic = re.search(r'((?<!\*)\*[^\s\*].+?[^\s\*]\*)|(\*(\*\*){1,}[^\s].*?[^\s](\*\*){1,}\*)', string_to_reduce)

        match_bold = re.search(r'(\*\*){1,}[^\s\*].*?[^\s\*](\*\*){1,}', string_to_reduce)

        while match_bold != None:

            before_match_text = string_to_reduce[:match_bold.start()]
            stripped_bold_inner_text = string_to_reduce[match_bold.start():match_bold.end()].replace('**', '')
            after_match_text = string_to_reduce[match_bold.end():]

            bold_text = f'<strong>{stripped_bold_inner_text}</strong>'

            string_to_reduce = before_match_text + bold_text + after_match_text

            match_bold = re.search(r'(\*\*){1,}[^\s\*].*?[^\s\*](\*\*){1,}', string_to_reduce)

        return string_to_reduce

    def inline_text_reduce_bold(self, string_to_reduce):

        match_strike = re.search(r'(~~){1,}[^\s~].*?[^\s~](~~){1,}', string_to_reduce)

        while match_strike != None:
            
            before_strike_text = string_to_reduce[:match_strike.start()]
            stripped_strike_inner_text = string_to_reduce[match_strike.start():match_strike.end()].replace('~~', '')
            after_strike_text = string_to_reduce[match_strike.end():]

            strike_text = f'<del>{stripped_strike_inner_text}</del>'

            string_to_reduce = before_strike_text + strike_text + after_strike_text

            match_strike = re.search(r'(~~){1,}[^\s~].*?[^\s~](~~){1,}', string_to_reduce)

        match_italic = re.search(r'(\*[^\s\*].*?[^\s\*]\*)|(\*(\*\*){1,}[^\s\*].+?[^\s\*](\*\*){1,}\*(?!\*))', string_to_reduce)

        while match_italic != None:

            before_italic_text = string_to_reduce[:match_italic.start()]
            stripped_italic_inner_text = string_to_reduce[match_italic.start():match_italic.end()].replace('*', '')
            after_italic_text = string_to_reduce[match_italic.end():]

            italic_text = f'<em>{stripped_italic_inner_text}</em>'
            
            string_to_reduce = before_italic_text + italic_text + after_italic_text

            match_italic = re.search(r'(\*[^\s\*].*?[^\s\*]\*)|(\*(\*\*){1,}[^\s\*].+?[^\s\*](\*\*){1,}\*(?!\*))', string_to_reduce)
            
        return string_to_reduce

    def inline_text_reduce_italic(self, string_to_reduce):

        match_bold = re.search(r'(\*\*){1,}(\*.*?\*|[^\s]).*?(\*.*?\*|[^\s])(\*\*){1,}', string_to_reduce)

        while match_bold != None:
            before_match_text = string_to_reduce[:match_bold.start()]
            stripped_bold_inner_text = string_to_reduce[match_bold.start():match_bold.end()].replace('**', '')
            after_match_text = string_to_reduce[match_bold.end():]

            bold_inner_text = f'<strong>{stripped_bold_inner_text}</strong>'
        
            string_to_reduce = before_match_text + bold_inner_text + after_match_text

            match_bold = re.search(r'(\*\*){1,}(\*.*?\*|[^\s]).*?(\*.*?\*|[^\s])(\*\*){1,}', string_to_reduce)
            
        # TODO: reduce strike through text
        
        return string_to_reduce