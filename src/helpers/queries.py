class Queries:

    @staticmethod
    def get_schema():
        return """
            # Define types
            type Product {
                description
                quantity
                price
                bought
            }

            type Order {
                total
                invoice
            }

            type Provider {
                pid
                sold
                belongs
            }

            type Location {
                name
            }

            # Define Directives and index
            description: String @index(term) @lang .
            quantity: int @index(int) .
            price: float .
            bought: [uid] @count @reverse .
            sold: [uid] @count @reverse .
            invoice: String @index(term) .
            total: float .
            date: datetime @index(day) .
            pid: String @index(term) .
            belongs: [uid] @count @reverse .
            name: String @index(term) .
        """

    @staticmethod
    def query_uid(uid, type):
        return """
            {
                response(func: uid(%s)) {
                    expand(%s)
                }
            }
        """ % (uid, type)

    @staticmethod
    def query_desc(desc):
        return """
            {
                response(func: eq(description, "%s")) {
                    uid
                }
            }
        """ % (desc)

    @staticmethod
    def query_invoice(inv):
        return """
            {
                response(func: eq(invoice, "%s")) {
                    uid
                }
            }
        """ % (inv)

    @staticmethod
    def query_pid(pid):
        return """
            {
                response(func: eq(pid, "%s")) {
                    uid
                }
            }
        """ % (pid)

    @staticmethod
    def query_name(name):
        return """
            {
                response(func: eq(name, "%s")) {
                    uid
                }
            }
        """ % (name)

    @staticmethod
    def query_belongs(pid):
        return """
            {
                response(func: uid(%s)) {
                    belongs {
                        uid
                    }
                }
            }
        """ % (pid)

    @staticmethod
    def query_boughts(uid):
        return """
            {
                response(func: uid(%s)) {
                    bought {
                        uid
                    }
                }
            }
        """ % (uid)

    @staticmethod
    def query_sold(uid):
        return """
            {
                response(func: uid(%s)) {
                    sold {
                        uid
                    }
                }
            }
        """ % (uid)

    @staticmethod
    def create_product(desc, price):
        return """
            {
                set {
                    _:product <description> "%s" .
                    _:product <price> "%s" .
                    _:product <dgraph.type> "Product" .
                }
            }
        """ % (desc, price)

    @staticmethod
    def add_bought_relation(product_uid, order_uid):
        return """
            {
                set {
                    <%s> <bought> <%s> .
                }
            }
        """ % (product_uid, order_uid)

    @staticmethod
    def add_sold_relation(product_uid, provider_uid):
        return """
            {
                set {
                    <%s> <sold> <%s> .
                }
            }
        """ % (product_uid, provider_uid)

    @staticmethod
    def create_order(inv, qty, tot, date):
        return """
            {
                set {
                    _:order <invoice> "%s" .
                    _:order <quantity> "%s" .
                    _:order <total> "%s" .
                    _:order <date> "%s" .
                    _:order <dgraph.type> "Order" .
                }
            }
        """ % (inv, qty, tot, date)

    @staticmethod
    def create_provider(pid, loc):
        return """
            {
                set {
                    _:provider <pid> "%s" .
                    _:provider <belongs> <%s> .
                    _:provider <dgraph.type> "Provider" .
                }
            }
        """ % (pid, loc)

    @staticmethod
    def add_belongs_relation(provider_uid, location_uid):
        return """
            {
                set {
                    <%s> <belongs> <%s> .
                }
            }
        """ % (provider_uid, location_uid)

    @staticmethod
    def create_location(name):
        return """
            {
                set {
                    _:location <name> "%s" .
                    _:location <dgraph.type> "Location" .
                }
            }
        """ % (name)