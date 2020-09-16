def get_table_width(title, data):
    longest = len(title)
    additional_spacing = 2
    for item in data:
        if len(item) > longest:
            longest = len(item)
    return longest + additional_spacing


def print_table_body(contents):
    for item in contents:
        print(f'| {item}')


def print_divider(length):
    print(f'+{"=" * length}+')


def print_table_header(title, width):
    print_divider(width)
    print(f'| {title.upper()}')
    print_divider(width)


def print_table_footer(width):
    print_divider(width)


def print_table(title, contents):
    width = get_table_width(title, contents)
    print_table_header(title, width)
    print_table_body(contents)
    print_table_footer(width)
