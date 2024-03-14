import subprocess

def check_answer(answer, word):
    '''
        Determine if the user's answer is correct.
    '''
    word = word.strip().lower()
    answer = answer.strip().lower()    
    
    return translate_word(word) == answer

def translate_word(word):
    command = f"trans -l spanish -t english '{word}' -b"

    # Run the command and capture the output
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    # Extract the stdout and stderr
    stdout = str(result.stdout).strip().lower()
    stderr = result.stderr

    # Check for errors
    if result.returncode != 0:
        print("Error:", stderr) 
        stdout = ''
    return stdout