
def main():
    from argparse import ArgumentParser
    
    parser = ArgumentParser()
    parser.add_argument('-t', '--temperature', type=float, default=.333, help='Softmax sampling frequency')
    arguments = parser.parse_args()

    from gui import main
    main(arguments)

if __name__ == "__main__":
    main()
