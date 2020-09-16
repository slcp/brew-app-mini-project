def read_lines(path):
    data = []
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                # Check if empty - bail/stop/valdiate as early as possible
                if not line:
                    continue
                # Trim newline/whitespace
                # Add to data
                data.append(line.strip())
    except FileNotFoundError as e:
        print(f'File "{path}" cannot be found with error: {str(e)} - exiting')
    return data
