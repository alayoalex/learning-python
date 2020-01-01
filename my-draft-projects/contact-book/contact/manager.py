import contact
import sys, argparse


def parse_cli():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "name",
            nargs="?",
            help="Contact's name and last name"
        )
        parser.add_argument(
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
        )
        parser.add_argument(
            "-s",
            action="store_true",
            help="Automatically save the conctact data."
        )
        parser.add_argument(
            "-u",
            action="store_true",
            help="Automatically update the conctact data."
        )
        parser.add_argument(
            "-d",
            action="store_true",
            help="Automatically delete the data of a given contact or a given contact."
        )
        parser.add_argument(
            "-l",
            action="store_true",
            help="Automatically list all the conctact data."
        )
        parser.add_argument(
            "-g",
            action="store_true",
            help="Get the contact data given the contact."
        )
        parser.add_argument(
            "-o",
            action="store_true",
            help="Sort the contact data in database by a parameter."
        )
        args = parser.parse_args()    
        return args
    except argparse.ArgumentError as err:
        print(str(err))
        sys.exit(2)


def save_contact():
    args = parse_cli()
    c = contact.Contact(args.name, args.phone, args.address, args.email)
    print(args.s)


if __name__ == "__main__":
    save_contact()