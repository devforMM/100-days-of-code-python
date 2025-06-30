with open("./day24/names/invited_names.txt")as file_names:
    names=file_names.readlines()
    
with open("./day24/letters/starting_letter.txt")as letter_file:
    content=letter_file.read()
    

placeholder="[name]"

for name in names:
    with open(f"./day24/ready_to_send/letter to {name.strip()}.txt","w")as f:
            content=content.replace(placeholder,name.strip())
            f.write(content)
    
    
    
            