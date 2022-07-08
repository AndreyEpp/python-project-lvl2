import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    if '-h' in args:
        parser.print_help()
    else:
        result = generate_diff(pars(args.first_file),
                               pars(args.second_file))
        return result


if __name__ == '__main__':
    main()
