from publication import Book, Magazine

def main():
    donald_duck_magazine = Magazine("Donald Duck", "Aki Hyyppä")
    compartment_no_6_book = Book("Compartment No. 6", "Rosa Liksom", 192)

    donald_duck_magazine.print_information()
    print()
    compartment_no_6_book.print_information()

if __name__ == "__main__":
    main()