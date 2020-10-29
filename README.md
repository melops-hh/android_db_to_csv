# Recover Android contacts from contacts2.db

For some reason my Android phone wouldn't allow me to export my contacts, so I
needed to find another solution.
If you have the same problems this might help you

Find your contacts2.db and copy it to your computer
```sh
[root]/data/data/com.android.providers.contacts/databases/contacts2.db
```

run the script
```sh
python contacts.py path/to/your/contacts2.db output.csv
```


