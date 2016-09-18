class Transaction:

    def __init__(self, date, description, original_description, amount, transaction_type, category, account_name):
        self.date = date
        self.description = description.lower()
        self.original_description = original_description.lower()
        self.amount = amount
        self.transaction_type = transaction_type.lower()
        self.category = category.lower()
        self.account_name = account_name.lower()

    def expand(self):
        print(self.date,
              self.description,
              self.original_description,
              self.amount,
              self.transaction_type,
              self.category,
              self.account_name)

    def list(self):
        return [self.date,
                self.description,
                self.original_description,
                self.amount,
                self.transaction_type,
                self.category,
                self.account_name]
