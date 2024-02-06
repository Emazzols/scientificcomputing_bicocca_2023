# List of book titles
titles = ["don quixote", 
          "in search of lost time", 
          "ulysses", 
          "the odyssey", 
          "war and peace", 
          "moby dick", 
          "the divine comedy", 
          "hamlet", 
          "the adventures of huckleberry finn", 
          "the great gatsby"]

# Iterate over each title in the list
for title in titles:
    # Split the title into individual words
    words = title.split()
    
    # Capitalize the first letter of each word and join them back
    new_title = ' '.join(word.capitalize() for word in words)
    
    # Print the modified title
    print(new_title)
