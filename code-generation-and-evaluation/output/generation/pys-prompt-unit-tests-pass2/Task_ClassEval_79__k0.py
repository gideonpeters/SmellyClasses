class SQLGenerator:
    def __init__(self, table_name):
        self.table_name = table_name

    def select(self, fields, condition=None):
        if condition:
            return f"SELECT {', '.join(fields)} FROM {self.table_name} WHERE {condition};"
        else:
            return f"SELECT {', '.join(fields)} FROM {self.table_name};"

    def insert(self, values):
        fields = ', '.join(values.keys())
        value_str = ', '.join([f"'{value}'" for value in values.values()])
        return f"INSERT INTO {self.table_name} ({fields}) VALUES ({value_str});"

    def update(self, values, condition):
        set_values = ', '.join([f"{key} = '{value}'" for key, value in values.items()])
        return f"UPDATE {self.table_name} SET {set_values} WHERE {condition};"

    def delete(self, condition):
        return f"DELETE FROM {self.table_name} WHERE {condition};"

    def select_female_under_age(self, age):
        return f"SELECT * FROM {self.table_name} WHERE age < {age} AND gender = 'female';"

    def select_by_age_range(self, min_age, max_age):
        return f"SELECT * FROM {self.table_name} WHERE age BETWEEN {min_age} AND {max_age};"
