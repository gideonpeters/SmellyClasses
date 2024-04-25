import numpy as np

class VectorUtil:
    @staticmethod
    def similarity(vector_1, vector_2):
        dot_product = np.dot(vector_1, vector_2)
        norm_1 = np.linalg.norm(vector_1)
        norm_2 = np.linalg.norm(vector_2)
        return dot_product / (norm_1 * norm_2)

    @staticmethod
    def cosine_similarities(vector1, vectors_all):
        similarities = []
        for vector in vectors_all:
            similarity = VectorUtil.similarity(vector1, vector)
            similarities.append(similarity)
        return similarities

    @staticmethod
    def n_similarity(vector_list1, vector_list2):
        similarities = [VectorUtil.similarity(v1, v2) for v1, v2 in zip(vector_list1, vector_list2)]
        return sum(similarities) / len(similarities)

    @staticmethod
    def compute_idf_weight_dict(total_docs, num_dict):
        idf_weight_dict = {}
        for key, value in num_dict.items():
            idf_weight_dict[key] = np.log(total_docs / (1 + value))
        return idf_weight_dict
