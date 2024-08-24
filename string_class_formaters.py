class Book:

    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author

    def __format__(self, format_spec):
        match format_spec:
            case 'title':
                return self.title.upper()
            case 'author':
                return self.author
            case 'time':
                return f'{self.pages / 60:.2f}h'
            case _:
                return ValueError(f'Wrong choice')


def main():
    b1 = Book("The Switch", 350, "Anthony Horowitz")
    
    print(f'{b1:title}')
    print(f'{b1:author}')
    print(f'{b1:time}')


if '__main__' == __name__:
    main()
 
