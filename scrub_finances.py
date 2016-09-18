import csv
import datetime
import sys

import transaction


def write_csv(good, bad):
    name = datetime.datetime.now()
    with open(str(name) + '.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        for trans in good:
            spamwriter.writerow(trans.list())
        spamwriter.writerow(['', '', '', ''] * 5)
        for trans in bad:
            spamwriter.writerow(trans.list())

def import_csv(filename):
    good_trans = []
    bad_trans = []
    money_spent = 0
    money_made = 0
    with open(filename, 'rU') as csvfile:
        reader = csv.reader(csvfile, dialect=csv.excel_tab)
        for row in reader:
            unpacked = row[0].split(',')[0:7]
            trans = transaction.Transaction(unpacked[0],
                                            unpacked[1],
                                            unpacked[2],
                                            unpacked[3],
                                            unpacked[4],
                                            unpacked[5],
                                            unpacked[6])
            trans.expand()
            if trans.category == 'transfer':
                bad_trans.append(trans)
            elif trans.account_name == 'venmo' and trans.transaction_type == 'debit' and trans.description == 'cashed out':
                bad_trans.append(trans)
            elif trans.transaction_type == 'credit' and trans.description == 'venmo cashout':
                bad_trans.append(trans)
            elif trans.category == 'transfer':
                bad_trans.append(trans)
            elif trans.amount == 'Amount':
                del(trans)
            elif trans.description == 'returned' and trans.account_name == 'credit card':
                bad_trans.append(trans)
            elif trans.description == 'chase epay':
                bad_trans.append(trans)
            elif trans.description == 'online ach thank':
                bad_trans.append(trans)
            elif trans.description == 'thank you web':
                bad_trans.append(trans)
            elif trans.description == 'fid bkg svc':
                bad_trans.append(trans)
            elif trans.description == 'wells fargo ccpymt':
                bad_trans.append(trans)
            else:
                good_trans.append(trans)
    print('Good Transactions:\n\n')
    for tran in good_trans:
        if tran.transaction_type == 'debit':
            money_spent += int(float(tran.amount))
        if tran.transaction_type == 'credit':
            money_made += int(float(tran.amount))
        tran.expand()
    print('Bad Transactions:\n\n')
    for tran in bad_trans:
        tran.expand()
    print('\n\nMoney Made: ${}'.format(money_made))
    print('\n\nMoney Spent: ${}'.format(money_spent))
    return good_trans, bad_trans

if __name__ == "__main__":
    filename = sys.argv[1]
    good, bad = import_csv(filename)
    write_csv(good, bad)
