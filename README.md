# zimbra-calendar-exporter

The Zimbra Calendar Exporter allows you to access your calendar from Zimbra without basic authentication. This allows you to export it to any other calendar. One application instance allows you to use multiple accounts. Credentials are securely stored in the Keepass database.


# Setup

---

Install kpcli (if you're using Arch, you can use Keepassxc-cli):
```bash
apt-get install kpcli #Ubuntu
```

Create a database (you can also use kpcli):
```bash
keepassxc-cli db-create db.kdbx -p
```

Connect to db:
```
kpcli --kdb=db.kdbx
```

Create a new entity. In the username field, enter your Zimbra account username. In the password field, enter your Zimbra account password. In notes, create any token. It will be used to access the calendar.
```
kpcli:/> new Passwords/fokidoki
Adding new entry to "/Passwords"
Title: title
Username: username
Password:                ("g" or "w" to auto-generate, "i" for interactive)
Retype to verify: 
URL:  
Tags: 
Strings: (a)dd/(e)dit/(d)elete/(c)ancel/(F)inish? 
Notes/Comments (""): 
(end multi-line input with a single "." on a line)
| MY_TOKEN
| .
Database was modified. Do you want to save it now? [y/N]: 

Saved to db.kdbx

```

Add another account or follow these steps.

Clone this repo
```
git clone https://github.com/FokiDoki/zimbra-to-ics.git
```

move the database to the current project folder and run the build
```
mv db.kdbx zimbra-to-ics
cd zimbra-to-ics
./build.sh
```

Go to the "certs" folder and generate the certificates.
```
cd certs 
sudo certbot certonly --standalone -d <your-domain>
```
Copy `fullchain.pem` and `privkey.pem` into certificates folder.

Set up environment variables inside the docker.env file.
Change: \
ZIMBRA_URL=YOUR_MAIL_DOMAIN \
KEEPASS_PASS=KEEPASS_DATABASE_PASSWORD 

**Keep this file safe** 

Start app
```
./start.sh
```

Now your calendar avaliable at `https://your-domain:4443/MY_TOKEN/calendar.ics`