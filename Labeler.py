def label_conversation(file_path):
    """
    Reads a conversation from a file and prompts the user to label each message for sentiment.
    
    Args:
    - file_path: Path to the file containing the conversation.
    
    Outputs a 'labels.txt' file with the user-provided labels.
    """
    try:
        # Read the conversation from the file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Open a new file to write the labels
        with open('labels.txt', 'w', encoding='utf-8') as label_file:
            for line in lines:
                # Display each message to the user
                print(f"Message: {line.strip()}")
                # Prompt the user for a label
                label = input("Enter label (1 for positive, 0 for negative, 2 for neutral): ").strip()
                # Write the label to the labels.txt file
                label_file.write(label + '\n')
                
        print("Labeling complete. Labels saved to 'labels.txt'.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'conversation.txt'  # Update this to the path of your conversation file
label_conversation(file_path)
