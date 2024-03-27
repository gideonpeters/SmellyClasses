class SQLQueryBuilder:
    @staticmethod
    def select(table, columns, conditions=None):
        query = f"SELECT {', '.join(columns)} FROM {table}"
        if conditions:
            conditions_str = ' AND '.join([f"{key}='{value}'" for key, value in conditions.items()])
            query += f" WHERE {conditions_str}"
        return query

    @staticmethod
    def insert(table, values):
        columns = ', '.join(values.keys())
        vals = ', '.join([f"'{val}'" for val in values.values()])
        return f"INSERT INTO {table} ({columns}) VALUES ({vals})"

    @staticmethod
    def delete(table, conditions=None):
        if conditions:
            conditions_str = ' AND '.join([f"{key}='{value}'" for key, value in conditions.items()])
            return f"DELETE FROM {table} WHERE {conditions_str}"
        else:
            return f"DELETE FROM {table}"

    @staticmethod
    def update(table, new_values, conditions=None):
        set_values = ', '.join([f"{key}='{value}'" for key, value in new_values.items()])
        if conditions:
            conditions_str = ' AND '.join([f"{key}='{value}'" for key, value in conditions.items()])
            return f"UPDATE {table} SET {set_values} WHERE {conditions_str}"
        else:
            return f"UPDATE {table} SET {set_values}"
`