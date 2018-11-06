import unittest
from models.codeblock import CodeBlock

class CodeBlockTest(unittest.TestCase):

    def test_parse_parses_code_block_body_correctly(self):
        codeblock_string = '''```
            Hello World
        ```'''

        codeblock = CodeBlock(codeblock_string, '1')

        self.assertEqual(codeblock.code.strip(), 'Hello World')

    def test_to_html_returns_code_wrapped_in_code_tags(self):
        codeblock_string = '''```
            This is some code
            yes it is
        ```'''

        codeblock = CodeBlock(codeblock_string, '1')

        expected_codeblock_to_html = '''
        <div class="row">
            <div class="col s12 m5">
                <div class="card">
                    <div id="codeblock-1"></div>
                </div>
            </div>
        </div>
        '''

        self.assertEqual(codeblock.to_html(), expected_codeblock_to_html)

    def test_parse_with_javascript_language_tag_sets_mode_to_javascript(self):
        
        code = '''```javascript
            let i = 0;

            for(i = 0; i < 10; i++) {
                console.log(i);
            }
        ```'''

        codeblock = CodeBlock(code, '1')
        
        self.assertEqual(codeblock.mode, 'javascript')

    def test_parse_with_javascript_language_tag_and_trailing_space_sets_mode_to_javascript(self):
        
        code = '''```javascript 
            let i = 0;

            for(i = 0; i < 10; i++) {
                console.log(i);
            }
        ```'''

        codeblock = CodeBlock(code, '1')
        
        self.assertEqual(codeblock.mode, 'javascript')