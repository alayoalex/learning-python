import contact
import sys, argparse
import operations


def parse_cli():
    try:
        parser = argparse.ArgumentParser("App to manage contact book.")
        parser.add_argument(
            "data",
            nargs="*",
            default=[],
            help="Data of the contact"
        )
        '''parser.add_argument(
            "phone",
            nargs="?",
            help="Contact's phone"
        )
        parser.add_argument(
            "address",
            nargs="?",
            help="Contact's address"
        )
        parser.add_argument(
            "email",
            nargs="?",
            help="Contact's email"
        )'''

        group = parser.add_mutually_exclusive_group()
        group.add_argument(
            "-s",
            action="store_true",
            help="Automatically save the conctact data."
        )
        group.add_argument(
            "-u",
            action="store_true",
            help="Automatically update the conctact data."
        )
        group.add_argument(
            "-d",
            action="store_true",
            help="Automatically delete the data of a given contact or a given contact."
        )
        parser.add_argument(
            "-l",
            action="store_true",
            help="Automatically list all the conctact data."
        )
        group.add_argument(
            "-g",
            action="store_true",
            help="Get the contact data given the contact."
        )
        group.add_argument(
            "-o",
            action="store_true",
            help="Sort the contact data in database by a parameter."
        )
        args = parser.parse_args()    
        return args
    except argparse.ArgumentError as err:
        print(str(err))
        sys.exit(2)


def main():
    args = parse_cli()
    if args.s:
        data = args.data
        operations.save(data)
    if args.l:
        results = operations.listing()
        for i in results:
            for j in i:
                print(j, end=" "*5)
            print()

    
if __name__ == "__main__":
    main()