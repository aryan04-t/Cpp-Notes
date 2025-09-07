import os

def rename_files():

    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    
    for filename in files:

        splitted_filename = os.path.splitext(filename)

        curr_filename_without_ext = splitted_filename[0]
        curr_file_ext = splitted_filename[1]

        if not curr_file_ext:
            continue
        
        exclude_extensions_from_processing = ['.py']

        if not any(curr_file_ext == ext for ext in exclude_extensions_from_processing):
            space_splitted_filename = curr_filename_without_ext.split(' ')
            
            if len(space_splitted_filename) >= 2:
                first_word = space_splitted_filename[0]
                preferred_text = ["th", "nd", "st", "rd"]

                for text in preferred_text:
                    if text in first_word:
                        num = first_word.split(text)[0]

                        if num.isnumeric():
                            rest = space_splitted_filename[1:]
                            new_name = f"{num}_{' '.join(rest)}{curr_file_ext}"
                            print("new_name", new_name)
                            os.rename(filename, new_name)

rename_files()