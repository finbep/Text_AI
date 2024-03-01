# Function to tokenize a conversation from a text file
def tokenize_conversation(file_path):
    # Read the conversation from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        conversation = file.read()
    
    # Splitting the conversation into lines
    lines = conversation.strip().split('\n')
    
    # Tokenizing each line into words
    # Assuming each line is in the format "Speaker: speech"
    tokenized_conversation = [line.split(': ')[1].split() for line in lines if ': ' in line]
    
    return tokenized_conversation

# Example usage
file_path = 'conversation.txt'  # Make sure to use the correct path to your text file
tokenized_conversation = tokenize_conversation(file_path)

# Print the tokenized conversation to verify
for line in tokenized_conversation:
    print(line)
