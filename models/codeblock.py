
supported_languages = [
    'javascript',
    'json'
]

language_to_mode_dict = {
    'javascript': 'javascript',
    'json': 'application/json'
}

class CodeBlock:
    
    def __init__(self, value, code_block_id):
        self.mode = ''
        self.code = self.parse(value)
        self.code_block_id = f'codeblock-{code_block_id}'

    def parse(self, value):
        code = value.strip('```')
        language = code.split('\n', 1)[0].strip()

        if language in supported_languages:
            self.mode = language_to_mode_dict[language]

        code = code.split('\n', 1)[1]

        return code

    def to_html(self):
        return f'''
        <div class="row">
            <div class="col s12 m5">
                <div class="card">
                    <div id="{self.code_block_id}"></div>
                </div>
            </div>
        </div>
        '''

    def get_script_initializer(self):
        
        initializer_string = f'''
        <script>
            CodeMirror(document.getElementById("{self.code_block_id}"),
            {{
                lineNumbers: true,
                mode: "{self.mode}",
                readOnly: false
            }}
            ).setValue(`{self.code}`);
        </script>
        '''

        return initializer_string

    def __str__(self):
        return self.to_html()

    def __repr__(self):
        return self.to_html()