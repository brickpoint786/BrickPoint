import os, glob

php_files = glob.glob("/home/user/BrickPoint/wordpress/brickpoint/**/*.php", recursive=True)
print(f"Checking {len(php_files)} PHP files...")

errors = 0
for fpath in php_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Simple tokenizer aware of PHP opening and closing tags
    in_php = False
    curly = 0
    paren = 0
    square = 0
    in_string = False
    str_char = None
    in_line_comment = False
    in_block_comment = False

    i = 0
    n = len(content)
    line = 1

    while i < n:
        if content[i:i+5] == "<?php" and not in_php:
            in_php = True
            i += 5
            continue
        if content[i:i+3] == "<?=" and not in_php:
            in_php = True
            i += 3
            continue
        if content[i:i+2] == "?>" and in_php and not in_string and not in_block_comment:
            in_php = False
            in_line_comment = False
            i += 2
            continue

        if not in_php:
            if content[i] == '\n':
                line += 1
            i += 1
            continue

        c = content[i]
        if c == '\n':
            line += 1
            in_line_comment = False
            i += 1
            continue

        if in_line_comment:
            i += 1
            continue

        if in_block_comment:
            if c == '*' and i + 1 < n and content[i + 1] == '/':
                in_block_comment = False
                i += 2
                continue
            i += 1
            continue

        if in_string:
            if c == '\\':
                i += 2
                continue
            if c == str_char:
                in_string = False
            i += 1
            continue

        if c == '/' and i + 1 < n:
            if content[i + 1] == '/':
                in_line_comment = True
                i += 2
                continue
            if content[i + 1] == '*':
                in_block_comment = True
                i += 2
                continue
        if c == '#':
            in_line_comment = True
            i += 1
            continue

        if c in ("'", '"'):
            in_string = True
            str_char = c
            i += 1
            continue

        if c == '{': curly += 1
        elif c == '}': curly -= 1
        elif c == '(': paren += 1
        elif c == ')': paren -= 1
        elif c == '[': square += 1
        elif c == ']': square -= 1

        if curly < 0:
            print(f"Error in {fpath}:{line}: Unexpected closing brace '}}'")
            errors += 1
            break
        if paren < 0:
            print(f"Error in {fpath}:{line}: Unexpected closing parenthesis ')'")
            errors += 1
            break
        if square < 0:
            print(f"Error in {fpath}:{line}: Unexpected closing bracket ']'")
            errors += 1
            break

        i += 1

    if curly != 0:
        print(f"Error in {fpath}: Unbalanced curly braces in PHP mode (diff = {curly})")
        errors += 1
    if paren != 0:
        print(f"Error in {fpath}: Unbalanced parentheses in PHP mode (diff = {paren})")
        errors += 1
    if square != 0:
        print(f"Error in {fpath}: Unbalanced square brackets in PHP mode (diff = {square})")
        errors += 1

if errors == 0:
    print(f"All {len(php_files)} PHP files passed balanced PHP syntax check cleanly!")
else:
    print(f"Found {errors} syntax issues.")
