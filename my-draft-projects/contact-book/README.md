# Contact Book

## Overview

[Inspired in Real Python Article](https://realpython.com/intermediate-python-project-ideas/#command-line)

We come across lots of people daily. We make acquaintances and friends. We get their contacts to keep in touch later on. Sadly, keeping the received contact details can be hard. One way to do this is to write the contact details down. But this is not secure as the physical book can easily be lost.

This is where the Contact Book project comes in. A contact book is a tool for saving a contact’s details, such as name, address, phone number, and email address. With this contact book project, you can build a software tool that people can use to save and find contact details.

With the contact book project idea, users can save their contacts with less risk of losing the saved contact details. It’ll always be accessible from their computer, through the command-line.

### Examples of Contact Book Tools

There are Contact Book applications, but it’s rare to find command-line Contact Book products, as most are web, mobile, or GUI applications.

Here are some implementations of the Contact Book idea:

[Simple Contacts](https://play.google.com/store/apps/details?id=com.simplemobiletools.contacts&hl=en_US)

[Pobuca Connect](https://connect.pobuca.com/)

### Technical Details

The main objective of this project is to save contact details. It’s important that you set up the commands users can use to enter the contact details. You can use the argparse or click command-line frameworks. They abstract a lot of complex stuff, so you only have to focus on the logic to be run when executing commands.

Some features you should implement include the commands to delete contacts, update contact information, and list saved contacts. You can also allow users to list contacts using different parameters, such as alphabetical order or contact creation date.

Since it’s a command-line project, the SQLite database will be fine for saving contacts. SQLite is user-friendly to set up. You may save the contact details in a file, but a file will not offer the benefits you can gain from using SQLite, such as performance and security.

To use the SQLite database in this project, the Python sqlite3 module will be very useful.

### Extra Challenge

Remember how the database is stored on the user’s computer? What if something happens, like the user losing their files? It means they’ll also lose the contact details.

You can challenge yourself further and backup the database to an online storage platform. To do this, you can upload the database files to the cloud at certain intervals.

You can also add a command that allows users to backup the database themselves. This way, the user can still have access to the contacts if the database file is lost.

You should note that you may need some form of identification, so the contact book can tell which database file belongs to which user. Implementing a user authentication feature is one way to go about it.

---

## Defining project and Tasks

### Find a source of motivation

### Break the project into subtasks
1. Define database and domain, tables, relationships and data access. **SQLite**.
2. Define user interface. Command-line with **argparse**.
   - Set up the commands and arguments that users can use to enter the contact details.
        save (-s), update (-u), delete (-d), list (-l), sort (-o), get (-g)
4. Form of the commands:
   * contact [name, address, phone, email] -s -u
   * contact -l
   * contact -d [name] [phone] [email]
   * contact -g [name] [address] [phone] [email]

### Do research on the subtasks
   * sqlite3 (Python Standar Library, Oficial Python Documentation)
   * argparse (Python Standar Library, Oficial Python Documentation)

### Build each subtasks, one step at a time

### Reach out for help if you’re stuck

### Put the subtasks together

---

## Details

### Domain

**Contact**
* name
* address (add1, add2, add3)
* phone number (mobile1, mobile2, fijo, casa, trabajo)
* email address (email1, email2, email2)


### Funcionalities
* save
* update
* delete
* list (contacts using different parameters, such as alphabetical order or contact creation date)
* sort
* get (retrieve data contact using differents parameters)
  export to excel or csv.
* backup (backup the database to an online storage platform. To do this, you can upload the database files to the cloud at certain intervals. You can also add a command that allows users to backup the database themselves)
* loging (you may need some form of identification, so the contact book can tell which database file belongs to which user. Implementing a user authentication feature is one way to go about it)