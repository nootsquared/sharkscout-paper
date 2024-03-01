import json

def append_to_json(data, file_path='results.json'):
    with open(file_path, 'r') as f:
        try:
            existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = []

    # Append the new data
    existing_data.append(data)

    # Write everything back to the file
    with open(file_path, 'w') as f:
        f.write('[\n')
        for i, item in enumerate(existing_data):
            f.write(json.dumps(item) + (',' if i < len(existing_data) - 1 else '') + '\n')
        f.write(']\n')
        
def main():
    while True:
        qual_number = input("Enter qual number: ")
        alliance_color = input("Enter alliance color: ")
        team_number = input("Enter team number: ")
        did_they_score = input("Did they score? (Y/N): ")

        data = {
            'qual_number': qual_number,
            'team_number': team_number,
            'alliance_color': alliance_color,
            'did_they_score': did_they_score
        }
        
        print(data)
        append_to_json(data)

if __name__ == '__main__':
    main()