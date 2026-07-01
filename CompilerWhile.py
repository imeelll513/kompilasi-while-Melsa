import re

# ===== LEXICAL =====
def lex(source):
    rules = [
        ('WHILE', r'while'), ('NUMBER', r'\d+'), ('ID', r'[A-Za-z_]\w*'),
        ('RELOP', r'<=|>=|==|!=|<|>'), ('ASSIGN', r'='), ('PLUS', r'\+'),
        ('MINUS', r'-'), ('LPAREN', r'\('), ('RPAREN', r'\)'),
        ('LBRACE', r'\{'), ('RBRACE', r'\}'), ('SEMICOLON', r';'), ('SKIP', r'[ \t\n]+')
    ]
    regex = '|'.join(f'(?P<{n}>{p})' for n,p in rules)
    return [(m.lastgroup, m.group()) for m in re.finditer(regex, source) if m.lastgroup != 'SKIP']

# ===== SYNTAX =====
def parse(tokens):
    pos = 0
    
    def current():
        return tokens[pos] if pos < len(tokens) else ('EOF', '')
    
    def eat(expected):
        nonlocal pos
        token = current()
        if token[0] != expected:
            raise SyntaxError(f'Expected {expected}, got {token[0]}')
        pos += 1
        return token  # ← INI YANG HARUSNYA DIKEMBALIKAN!
    
    # while
    eat('WHILE')
    eat('LPAREN')
    
    # condition: ID RELOP NUMBER
    left_token = eat('ID')      # Ambil token lengkap
    left = left_token[1]        # Ambil nilainya
    
    op_token = eat('RELOP')
    op = op_token[1]
    
    right_token = eat('NUMBER')
    right = right_token[1]
    
    eat('RPAREN')
    eat('LBRACE')
    
    # assignment: ID = ID +|- NUMBER ;
    target_token = eat('ID')
    target = target_token[1]
    
    eat('ASSIGN')
    
    left_exp_token = eat('ID')
    left_exp = left_exp_token[1]
    
    # Cek operator
    if current()[0] == 'PLUS':
        operator = '+'
        eat('PLUS')
    elif current()[0] == 'MINUS':
        operator = '-'
        eat('MINUS')
    else:
        raise SyntaxError('Expected + or -')
    
    value_token = eat('NUMBER')
    value = value_token[1]
    
    eat('SEMICOLON')
    eat('RBRACE')
    
    return {
        'type': 'While',
        'condition': {
            'left': left,
            'op': op,
            'right': right
        },
        'body': {
            'target': target,
            'left': left_exp,
            'operator': operator,
            'value': value
        }
    }

# ===== SEMANTIC =====
def sem(ast):
    c = ast['condition']
    b = ast['body']
    
    if c['left'] != b['target']:
        raise Exception(f'Variable mismatch: {c["left"]} vs {b["target"]}')
    
    if b['left'] != b['target']:
        raise Exception('Assignment target must match left operand')
    
    return True

# ===== TAC =====
def tac(ast):
    c = ast['condition']
    b = ast['body']
    
    return [
        'L1:',
        f'if {c["left"]} {c["op"]} {c["right"]} goto L1',
        'goto L2',
        f't1 = {b["left"]} {b["operator"]} {b["value"]}',
        f'{b["target"]} = t1',
        'goto L1',
        'L2:'
    ]

# ===== MAIN =====
if __name__ == '__main__':
    source = """
    while (x < 10) {
        x = x + 1;
    }
    """
    
    print("=" * 50)
    print("SOURCE CODE:")
    print(source.strip())
    print("=" * 50)
    
    # Lexical
    print("\n[LEXICAL ANALYSIS]")
    tokens = lex(source)
    for token in tokens:
        print(token)
    
    # Syntax
    print("\n[SYNTAX ANALYSIS]")
    try:
        ast = parse(tokens)
        print("AST:", ast)
        print("✓ Syntax OK")
    except SyntaxError as e:
        print(f"✗ {e}")
        exit()
    
    # Semantic
    print("\n[SEMANTIC ANALYSIS]")
    try:
        sem(ast)
        print("✓ Semantic OK")
    except Exception as e:
        print(f"✗ {e}")
        exit()
    
    # TAC
    print("\n[THREE-ADDRESS CODE]")
    code = tac(ast)
    for line in code:
        print(line)
    
    print("\n" + "=" * 50)
    print("✓ COMPILATION SUCCESS")
    print("=" * 50)