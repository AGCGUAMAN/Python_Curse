# -*- coding: utf-8 -*-
import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('*******')
        print('¡¡Contacto NO encontrado!!')
        print('*******')


def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]Añadir Contacto
            [ac]Atualizar Contacto
            [b]Buscar Contacto
            [e]Eliminar Contacto
            [l]Listar Contactos
            [s]Salir
        '''))

        if command == 'a':
            name = str(input('Escribe el Nombre del Contacto: '))
            phone = str(input('Escribe el Teléfono del Contacto: '))
            email = str(input('Escribe el Email del Contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            print('actualizar contacto')

        elif command == 'b':
            name = str(input('Escribe el Nombre del Contacto: '))

            contact_book.search(name)

        elif command == 'e':
            name = str(input('Escribe el Nombre del Contacto: '))

            contact_book.delete(name)

        elif command == 'l':

            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando NO encontrado.')


if __name__ == '__main__':
    print('¡ ¡ B I E N V E N I D O   A   L A   A G E N D A   D E   C O N T A C T O S ! !')
    run()