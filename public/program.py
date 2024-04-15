def scanner(expression):
    tokens = []
    current_token = ''
    column = 1
    stack = []

    for char in expression:
        if char.isdigit():
            current_token += char
            tokens.append(('NUM', int(current_token)))
            current_token = ''

        elif char in '+-*/':
            tokens.append(('SYM', char))


        elif char == '(':
            tokens.append(('LPAREN', char))
            stack.append(len(tokens) - 1)
        elif char == ')':
            if tokens[stack[-1]][0] == 'LPAREN':
                tokens.append(('RPAREN', char))
                stack.pop()
            else:
                print("Syntax error: Unmatched closing parenthesis")
                return []
            

        elif char.isspace():
            column += 1
            continue
        else:
            print(f"Lexical error: Invalid character '{char}' at column {column}")
            return []

        column += 1

    if current_token:
        tokens.append(('NUM', int(current_token)))

    if stack:
        print("Syntax error: Unmatched opening parenthesis")
        return []

    return tokens



def color_syntax_to_html(input_file, output_file):
    with open(input_file, 'r') as f:
        code = f.read()

    tokens = scanner(code)
    print(tokens)
    with open(output_file, 'w') as f:
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<title>Colored Syntax</title>\n')
        f.write('<style>\n')
        f.write('span.blue { color: blue; }\n')
        f.write('span.green { color: green; }\n')
        f.write('span.red { color: red; }\n')
        f.write('span.orange { color: orange; }\n')
        f.write('</style>\n')
        f.write('</head>\n')
        f.write('<body>\n')

        for token in tokens:
            if token[0] == 'NUM':
                f.write(f'<span class="blue">{token[1]}</span>')
            elif token[0] == 'ID':
                f.write(f'<span class="green">{token[1]}</span>')
            elif token[0] == 'SYM':
                f.write(f'<span class="red">{token[1]}</span>')
            elif token[0] == 'LPAREN':
                f.write(f'<span class="orange">{token[1]}</span>')
            elif token[0] == 'RPAREN':
                f.write(f'<span class="orange">{token[1]}</span>')
            else:
                f.write(token[1])

        f.write('\n</body>\n')
        f.write('</html>\n')

input_file = "input.txt"
output_file = "colored_syntax.html"
color_syntax_to_html(input_file, output_file)
print(f"Colored syntax saved to {output_file}")
