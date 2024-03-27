class KappaCalculator:
    @staticmethod
    def kappa(matrix, n):
        total_agreements = sum(matrix[i][i] for i in range(n))
        total_items = sum(sum(row) for row in matrix)
        p_o = total_agreements / total_items
        p_e = sum(sum(matrix[i][j] * matrix[j][i] for j in range(n)) / (total_items ** 2) for i in range(n))
        kappa = (p_o - p_e) / (1 - p_e)
        return kappa

    @staticmethod
    def fleiss_kappa(matrix, n, k, N):
        total_ratings = n * N
        total_agreements = sum(sum(matrix[i][j] ** 2 - k for j in range(k)) for i in range(n))
        total_items = n * (N * k)
        p_o = (1 / total_ratings) * total_agreements
        p_e = sum((sum(matrix[i]) ** 2 - k) / (total_ratings ** 2) for i in range(n))
        kappa = (p_o - p_e) / (1 - p_e)
        return kappa
