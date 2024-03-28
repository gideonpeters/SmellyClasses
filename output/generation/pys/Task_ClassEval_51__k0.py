class KappaCalculator:
    @staticmethod
    def kappa(matrix, n):
        total_agreements = sum(matrix[i][i] for i in range(len(matrix)))
        total_items = sum(sum(row) for row in matrix)
        expected_agreements = sum(sum(row) ** 2 for row in matrix) / (total_items ** 2)
        kappa = (total_agreements - expected_agreements) / (total_items - expected_agreements)
        return kappa

    @staticmethod
    def fleiss_kappa(matrix, n, k, N):
        total_items = n * N
        total_categories = k
        total_judges = len(matrix)
        
        p = [0] * total_categories
        for j in range(total_categories):
            for i in range(total_judges):
                p[j] += matrix[i][j]
            p[j] /= total_items * total_judges
        
        P = [0] * total_judges
        for i in range(total_judges):
            for j in range(total_categories):
                P[i] += (matrix[i][j] ** 2)
            P[i] = (P[i] - n) / (n * (n - 1))
        
        P_bar = sum(P) / total_judges
        P_e = sum(p_i ** 2 for p_i in p)
        
        kappa = (P_bar - P_e) / (1 - P_e)
        return kappa
