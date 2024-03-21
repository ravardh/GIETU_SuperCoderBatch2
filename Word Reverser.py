def reverse_words(string):
    # Split the string into words
    words = string.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Join the reversed words into a new string
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

def main():
    # Simulate receiving banners with strings of words
    banners = [
        "Colorful banners express stories",
        "Diverse narratives enrich the city",
        "Community shares tales in the marketplace"
    ]
    
    # Reverse the words on each banner
    for banner in banners:
        reversed_banner = reverse_words(banner)
        print("Original: ", banner)
        print("Reversed: ", reversed_banner)
        print()

if __name__ == "__main__":
    main()
