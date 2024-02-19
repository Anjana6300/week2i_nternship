def count_words(text):
    """
    Count the number of words in the given text.

    Parameters:
    text (str): The input text.

    Returns:
    int: The word count.
    """

      words = text.split()
      return len(words)


def main():
    try: 
      # User Input
       user_input=input("Enter a sentence or paragraph" )
    
       # Check for empty input
       if not user_input:
           print("Error: Empty input. Please enter a sentence or paragraph.")
      
       else :
      
           # Word Counting Logic

            word_count=count_words(user_input)


          # Output Display
          
          print(f"Word count: {word_count}")
   
    
    except Exception as e:
        print("Error:", str(e))




if __name__ == "__main__":
    main()