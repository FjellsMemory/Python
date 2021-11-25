"""Sort out the mail, son.  Sort it good."""
from dataclasses import dataclass


@dataclass
class MailAddress:
    """Class modeling properties of an email address."""

    name: str
    domain: str


@dataclass
class Mail:
    """Class modeling properties of an email itself."""

    sender: MailAddress
    receiver: MailAddress
    subject: str
    body: str


@dataclass
class MailAccount:
    """Class modeling properties of an email account."""

    name: str
    inbox: list[Mail]
    outbox: list[Mail]


@dataclass
class MailServer:
    """Class modeling properties of an email server."""

    domain: str
    accounts: list[MailAccount]


def show_mail_address(address: MailAddress) -> str:
    """Return the mail's address attributes as string."""
    return f"{address.name}@{address.domain}"


def show_mail(mail: Mail) -> str:
    """Return the mail as a readable as string."""
    return f"""\nFrom: {mail.sender.name}@{mail.sender.domain}
To: {mail.receiver.name}@{mail.receiver.domain}
Subject: {mail.subject}\n
{mail.body}"""


def show_mail_account(account: MailAccount) -> str:
    """Return the mail's account attributes as string."""
    inboxstr = ""
    k = 1
    for x in account.inbox:
        inboxstr = inboxstr + f"""Mail #{k}:
    sender: {x.sender.name}@{x.sender.domain}
    receiver: {x.receiver.name}@{x.receiver.domain}
    subject: {x.subject}
    body: \n{x.body}\n
    """
        k += 1
    outboxstr = ""
    k = 1
    for x in account.outbox:
        outboxstr = outboxstr + f"""Mail #{k}:
    sender: {x.sender.name}@{x.sender.domain}
    receiver: {x.receiver.name}@{x.receiver.domain}
    subject: {x.subject}
    body: \n{x.body}\n
    """
        k += 1
    return f"""\nAccount Name: {account.name}\n
####################
    Inbox Items:
####################

    {print("") if inboxstr == "" else inboxstr}

#####################
    Outbox Items:
#####################

    {print("") if outboxstr == "" else outboxstr}\n"""


def show_mail_server(server: MailServer) -> str:
    """Return the mail's server attributes as string."""
    serverlist = ", ".join(str(x) for x in server.accounts)
    return ", ".join([server.domain, serverlist])


def find_server(d_sought: str, ser_list: list[MailServer]) -> MailServer | None:
    """Check list of mail servers for a particular sought server name."""
    for x in ser_list:
        if x.domain == d_sought:
            print(f"I'm checking my list of servers for {x.domain} in find_server(), and I got it.  I know where to deliver this mail.")
            return x
    return None


def find_account(a_sght: str, a_list: list[MailAccount]) -> MailAccount | None:
    """Check list of mail accounts for a particular sought account name."""
    for x in a_list:
        match x.name:
            case a_sght:
                return x
    return None


def deliver_mail(deliver_me: Mail, ser_list: list[MailServer]) -> bool:
    """Taken an email, check server list for del possiib, if poss:  deliver."""
    found_server = find_server(deliver_me.receiver.domain, ser_list)
    if found_server is None:
        return False
    else:
        found_ac = find_account(deliver_me.receiver.name, found_server.accounts)
        if found_ac is None:
            return False
        else:
            found_ac.inbox = found_ac.inbox + [deliver_me]
            return True
    # for x in ser_list:
    #     if deliver_me.sender.domain == x.domain:
    #         found_server = x
    # for x in found_server.accounts:
    #     if deliver_me.sender.name == x.name:
    #         for y in x.outbox:
    #             if y is deliver_me:
    #                 index = x.outbox.index(y)
    #                 del x.outbox[index]
    # return False


def deliver_all_mail(servers_list: list[MailServer]):
    """Deliever all all the pending mail shipments in MailServer outboxes."""
    print("I'm now going to deliver_all_mail()")
    deliver_count = 0
    ticker = 0
    del_list = []
    fucky_list = []
    for x in servers_list:
        print(f"\nThere are {len(servers_list)} server(s) in this list total.")
        print(f"Beginning my work on server {x.domain} at index[{servers_list.index(x)}] of the list now.")
        for y in x.accounts:
            print(f"Starting a check for outbound emails in {y.name}'s account outbox now.")
            for z in y.outbox:
                print(f"There is/are now currently {len(y.outbox)} mail(s) in this outbox.")
                print(f"The email I'm gonna verify and deliver now is titled {z.subject}.")
                if y.name == z.sender.name and x.domain == z.sender.domain:
                    print(f"i'm about to stick {z.subject} into deliver_mail() as an argument and send it the fuck off.")
                    deliver_mail(z, servers_list)
                    deliver_count += 1
                    print(f"So I just now delivered {z.subject} to {z.receiver.domain}, and now I'm gonna add it to list scheduled for deletion.")
                    del_list = del_list + [z]
                    print("Added it to del_list.  Moving onto next loop - check which email is now at the top of the outbox stack!!!.")
                    print(f"I've ostensibly now delivered {deliver_count} mails from {x.domain} to {z.receiver.domain}.")
                else:
                    print(f"Something about the address of {z.subject} is FUCKY.  I ain't sendin this shit, get rekt, spammer.")
                    fucky_list = fucky_list + [z]
                ticker += 1
            print("Okay, my babies, time to delete those emails I just sent or stuck on the fucky list.")
            print(f"In my trusty del_list I got {len(del_list)} email(s), and in my fucky_list I got {len(fucky_list)} email(s).")
            print(f"They are, in order: \n")
            for mail in del_list:
                print(mail.subject)
            for mail in fucky_list:
                print(mail.subject)
            for mail in del_list:
                print(f"Now going to delete {mail.subject} from da list.")
                if mail in del_list:
                    y.outbox.remove(mail)
            for mail in fucky_list:
                print(f"Now going to delete {mail.subject} from da list.")
                if mail in fucky_list:
                    y.outbox.remove(mail)
        del_list = []
        fucky_list = []


if __name__ == "__main__":
    mailaddress1a = MailAddress("Me", "mymail.com")
    mailaddress1b = MailAddress("You", "yourmail.com")
    subject1: str = "Super important stuff!"
    body1: str = "\t\tActually... it's not that important.\n\t\tSincerely,\n\t\tMe"
    mail1 = Mail(mailaddress1a, mailaddress1b, subject1, body1)

    mailaddress2a = MailAddress("Me", "mymail.com")
    mailaddress2b = MailAddress("Him", "hismail.com")
    subject2: str = "Enuff is Enuff!"
    body2: str = "\t\tWe gotta move these refrigerators.\n\t\tSincerely,\n\t\tDire Straits"
    mail2 = Mail(mailaddress2a, mailaddress2b, subject2, body2)

    inbox1 = []
    outbox1 = [mail1, mail2]
    mailaccount1 = MailAccount("Me", inbox1, outbox1)

    mailaddress3a = MailAddress("You", "yourmail.com")
    mailaddress3b = MailAddress("Him", "hismail.com")
    subject3: str = "McGruff the Crime Dog here!"
    body3: str = "\t\tIf you see something...just walk away.\n\t\tSincerely,\n\t\tMcGruff"
    mail3 = Mail(mailaddress3a, mailaddress3b, subject3, body3)

    mailaddress4a = MailAddress("You", "yourmail.com")
    mailaddress4b = MailAddress("Me", "mymail.com")
    subject4: str = "Gosh i'm tired!"
    body4: str = "\t\tGet rekt enjoy your holiday.\n\t\tSincerely,\n\t\tJoe"
    mail4 = Mail(mailaddress4a, mailaddress4b, subject4, body4)

    inbox2 = []
    outbox2 = [mail3, mail4]
    mailaccount2 = MailAccount("You", inbox2, outbox2)

    mailaddress5a = MailAddress("Him", "hismail.com")
    mailaddress5b = MailAddress("Me", "mymail.com")
    subject5: str = "Comin for Ya!"
    body5: str = "\t\tBasically gonna destroy your family.\n\t\tSincerely,\n\t\tVoltron"
    mail5 = Mail(mailaddress5a, mailaddress5b, subject5, body5)

    mailaddress6a = MailAddress("Him", "hismail.com")
    mailaddress6b = MailAddress("You", "yourmail.com")
    subject6: str = "My name is Sue!"
    body6: str = "\t\tHow do you do?\n\t\tSincerely,\n\t\tCash"
    mail6 = Mail(mailaddress6a, mailaddress6b, subject6, body6)

    inbox3 = []
    outbox3 = [mail5, mail6]
    mailaccount3 = MailAccount("Him", inbox3, outbox3)

    mailserver1 = MailServer("mymail.com", [mailaccount1])
    mailserver2 = MailServer("yourmail.com", [mailaccount2])
    mailserver3 = MailServer("hismail.com", [mailaccount3])

    grand_ser_list = [mailserver1, mailserver2, mailserver3]

    print(show_mail_account(mailaccount1))
    input("press any key to continue. >")
    print(show_mail_account(mailaccount2))
    input("press any key to continue. >")
    print(show_mail_account(mailaccount3))
    input("press any key to continue. >")
    print("""

++++++++++++++++++++++++++++++++++++++++
            SENDING MAIL
++++++++++++++++++++++++++++++++++++++++
""")
    deliver_all_mail(grand_ser_list)
    print(show_mail_account(mailaccount1))
    input("press any key to continue. >")
    print(show_mail_account(mailaccount2))
    input("press any key to continue. >")
    print(show_mail_account(mailaccount3))
    input("press any key to continue. >")
