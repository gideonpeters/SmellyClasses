import numpy as np

class VectorUtil:
    @staticmethod
    def similarity(vector1, vector2):
        dot_product = np.dot(vector1, vector2)
        norm_vector1 = np.linalg.norm(vector1)
        norm_vector2 = np.linalg.norm(vector2)
        return dot_product / (norm_vector1 * norm_vector2)

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
`