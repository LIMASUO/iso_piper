# This module is responsible for creating and managing the project database
# for all entities created in the project. This also maintains a set of
# configurations for the project.

import sqlite3

main_db = None


def validate_table(table_name):
    exists = True
    try:
        # main_db.execute('''SELECT * FROM %s''' % table_name)
        main_db.execute('''SELECT * FROM {}'''.format(table_name))
    except sqlite3.OperationalError:
        exists = False
    return exists


def validate_db():
    global main_db
    print("Creating database tables..." + '\n')
    if not (validate_table('pipe')):
        print("Creating pipe table...")
        main_db.execute('''CREATE TABLE pipe (id text, class text, subclass text, 
                        desc text, nom_dia real, main_size real, run_size real, 
                        comp_len real, end_prep_main real, end_prep_run real)''')
    else:
        print("Pipe table validated.")
    if not (validate_table('elbow')):
        print("Creating elbow table...")
        main_db.execute('''CREATE TABLE elbow (id text, class text, subclass text, 
                        desc text, nom_dia real, main_size real, run_size real, 
                        comp_len real, end_prep_main real, end_prep_run real, 
                        radius real)''')
    else:
        print("Elbow table validated.")
    if not (validate_table('geom')):
        print("Creating geometry table...")
        main_db.execute('''CREATE TABLE geom (id text, class text, desc text, 
                        parent text)''')
    else:
        print("Geom table validated.")
    if not (validate_table('cnfg')):
        print("Creating configuration table...")
        main_db.execute('''CREATE TABLE cnfg (id text, value text, desc text)''')
    else:
        print("Configuration table validated.")
    print('\n' + "Finished creating project database!" + '\n')


def initialize_db():
    global main_db
    main_db = sqlite3.connect('project.db')
    print("SQLite version: " + sqlite3.version)
    validate_db()

