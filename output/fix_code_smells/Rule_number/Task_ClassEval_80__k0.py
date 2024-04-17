class SQLQueryBuilder:
    @staticmethod
    def select(table, columns, conditions=None):
        query = "SELECT "
        if columns == "*":
            query += "*"
        else:
            query += ", ".join(columns)
        query += f" FROM {table}"
        if conditions:
            query += " WHERE " + " AND ".join([f"{key}='{value}'" for key, value in conditions.items()])
        return query

    @staticmethod
    def insert(table, values):
        query = f"INSERT INTO {table} ({', '.join(values.keys())}) VALUES ({', '.join([f'%s' for _ in values.values()])})"
        return query

    @staticmethod
    def delete(table, conditions=None):
        query = f"DELETE FROM {table}"
        if conditions:
            query += " WHERE " + " AND ".join([f"{key}='{value}'" for key, value in conditions.items()])
        return query

    @staticmethod
    def update(table, new_values, conditions=None):
        query = f"UPDATE {table} SET {', '.join([f'{key}=%s' for key in new_values.keys()])}"
        if conditions:
            query += " WHERE " + " AND ".join([f"{key}='{value}'" for key, value in conditions.items()])
        return query