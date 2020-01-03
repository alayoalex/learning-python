### Defining project

#### Contact’s details
* name
* address (add1, add2, add3)
* phone number (mobile1, mobile2, fijo, casa, trabajo)
* email address (email1, email2, email2)


#### Funcionalities
* save
* update
* delete
* list (contacts using different parameters, such as alphabetical order or contact creation date)
* sort
* get (retrieve data contact using differents parameters)
  export to excel or csv.
* backup (backup the database to an online storage platform. To do this, you can upload the database files to the cloud at certain intervals. You can also add a command that allows users to backup the database themselves)
* loging (you may need some form of identification, so the contact book can tell which database file belongs to which user. Implementing a user authentication feature is one way to go about it)


#### Tasks
1. Set up the commands users can use to enter the contact details.
   save (-s), update (-u), delete (-d), list (-l), sort (-o), get (-g)
2. Use the argparse or click command-line frameworks.
3. Form of the commands:
   contact [name] [address] [phone] [email] -s -u
   contact -l
   contact -d [name] [phone] [email]
   contact -g [name] [address] [phone] [email]
4. Persistency may be SQLite, plain text, json


#### Modules to study
* sqlite3 (Python Standar Library, Oficial Python Documentation)
* argparse (Python Standar Library, Oficial Python Documentation)