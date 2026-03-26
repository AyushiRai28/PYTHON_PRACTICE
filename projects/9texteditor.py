def text_editor():
    print("===== Simple Text Editor =====")
    
    filename = input("Enter file name to open/create: ")
    
    try:
        with open(filename, 'r') as file:
            print("\n--- Existing Content ---")
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("\n A new file will be created.")
        content = ""
    
    print("\n--- Start Editing ---")
    print("Type your text below.")
    print("Type 'SAVE' in a new line to save and exit.\n")
    
    lines = []
    
    while True:
        line = input()
        if line == "SAVE":
            break
        lines.append(line)
    
    new_content = "\n".join(lines)
    
    with open(filename, 'a') as file:
        file.write(new_content)
    
    print("\n✅ File saved successfully!")

# Run the editor
text_editor()
