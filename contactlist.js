// user interface and a code to crud and list contacts using a csv file
const inquirer = require("inquirer");
const fs = require("fs");
const {
    v4: uuidv4
}
    = require('uuid');
    const util = require('util');
    const readFileAsync = util.promisify(fs.readFile);
    const writeFileAsync = util.promisify(fs.writeFile);
    class Contact {
        constructor(name, email, phone) {
            this.name = name;
            this.email = email;
            this.phone = phone;
            this.id = uuidv4();
        }
    }
    class ContactList {
        constructor() {
            this.contacts = [];
        }
        addContact(contact) {
            this.contacts.push(contact);
        }
        getContacts() {
            return this.contacts;
        }
        deleteContact(id) {
            this.contacts = this.contacts.filter(contact => contact.id !== id);
        }
        async read() {
            const data = await readFileAsync("db/db.json", "utf8");
            this.contacts = JSON.parse(data);
        }
        async write() {
            const data = JSON.stringify(this.contacts);
            await writeFileAsync("db/db.json", data);
        }
    }
    module.exports = {
        Contact,
        ContactList
        }
        