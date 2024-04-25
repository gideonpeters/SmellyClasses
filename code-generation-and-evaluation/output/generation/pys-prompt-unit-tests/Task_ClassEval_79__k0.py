class SQLGenerator:
    def __init__(self, table_name):
        self.table_name = table_name

    def select(self, fields, condition=None):
        sql = "SELECT {} FROM {}"
        if condition:
            sql += " WHERE {};"
            return sql.format(', '.join(fields), self.table_name, condition)
        else:
            sql += ";"
            return sql.format(', '.join(fields), self.table_name)

    def insert(self, values):
        sql = "INSERT INTO {} ({}) VALUES ({});"
        fields = ', '.join(values.keys())
        vals = ', '.join(["'{}'".format(value) for value in values.values()])
        return sql.format(self.table_name, fields, vals)

    def update(self, values, condition):
        sql = "UPDATE {} SET {} WHERE {};"
        set_values = ', '.join(["{} = '{}'".format(key, value) for key, value in values.items()])
        return sql.format(self.table_name, set_values, condition)

    def delete(self, condition):
        return "DELETE FROM {} WHERE {};" .format(self.table_name, condition)

    def select_female_under_age(self, age):
        return "SELECT * FROM {} WHERE age < {} AND gender = 'female';" .format(self.table_name, age)

    def select_by_age_range(self, min_age, max_age):
        return "SELECT * FROM {} WHERE age BETWEEN {} AND {};" .format(self.table_name, min_age, max_age)
