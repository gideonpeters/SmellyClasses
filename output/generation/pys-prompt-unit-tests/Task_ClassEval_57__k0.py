class MetricsCalculator2:
    @staticmethod
    def mrr(data):
        if not isinstance(data, list):
            raise ValueError("Input data must be a list")

        if len(data) == 0:
            return 0.0, [0.0]

        mrr_score = 0.0
        mrr_list = []

        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each item in the list must be a tuple of format (list, int)")

            relevance_list, rank = item
            if not isinstance(relevance_list, list) or not all(isinstance(val, int) for val in relevance_list):
                raise ValueError("The first element of the tuple must be a list of integers")

            if rank <= 0:
                raise ValueError("Rank must be a positive integer")

            for i, rel in enumerate(relevance_list):
                if rel == 1:
                    mrr_score += 1 / (i + 1)
                    break

            mrr_list.append(mrr_score)

        mrr_score /= len(data)
        return mrr_score, mrr_list

    @staticmethod
    def map(data):
        if not isinstance(data, list):
            raise ValueError("Input data must be a list")

        if len(data) == 0:
            return 0.0, [0.0]

        map_score = 0.0
        map_list = []

        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each item in the list must be a tuple of format (list, int)")

            relevance_list, rank = item
            if not isinstance(relevance_list, list) or not all(isinstance(val, int) for val in relevance_list):
                raise ValueError("The first element of the tuple must be a list of integers")

            if rank <= 0:
                raise ValueError("Rank must be a positive integer")

            precision_sum = 0.0
            relevant_count = 0

            for i, rel in enumerate(relevance_list):
                if rel == 1:
                    relevant_count += 1
                    precision_sum += relevant_count / (i + 1)

            if relevant_count > 0:
                map_score += precision_sum / relevant_count

            map_list.append(map_score)

        map_score /= len(data)
        return map_score, map_list
