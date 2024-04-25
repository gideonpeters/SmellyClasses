class MetricsCalculator2:
    @staticmethod
    def mrr(data):
        if not isinstance(data, list):
            raise ValueError("Input must be a list of tuples")
        
        if len(data) == 0:
            return 0.0, [0.0]
        
        mrr_score = 0.0
        mrr_list = []
        
        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each element in the list must be a tuple of (list, int)")
            
            relevance_list, k = item
            if not isinstance(relevance_list, list) or not all(isinstance(val, int) for val in relevance_list):
                raise ValueError("First element of tuple must be a list of integers")
            
            if k <= 0:
                raise ValueError("Second element of tuple must be a positive integer")
            
            mrr_score += calculate_mrr(relevance_list)
            mrr_list.append(mrr_score)
        
        mrr_score /= len(data)
        
        return mrr_score, mrr_list

    @staticmethod
    def map(data):
        if not isinstance(data, list):
            raise ValueError("Input must be a list of tuples")
        
        if len(data) == 0:
            return 0.0, [0.0]
        
        map_score = 0.0
        map_list = []
        
        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each element in the list must be a tuple of (list, int)")
            
            relevance_list, k = item
            if not isinstance(relevance_list, list) or not all(isinstance(val, int) for val in relevance_list):
                raise ValueError("First element of tuple must be a list of integers")
            
            if k <= 0:
                raise ValueError("Second element of tuple must be a positive integer")
            
            map_score += calculate_map(relevance_list)
            map_list.append(map_score)
        
        map_score /= len(data)
        
        return map_score, map_list

def calculate_mrr(relevance_list):
    mrr_score = 0.0
    for i, rel in enumerate(relevance_list):
        if rel == 1:
            mrr_score += 1 / (i + 1)
            break
    return mrr_score

def calculate_map(relevance_list):
    precision_sum = 0.0
    relevant_count = 0
    for i, rel in enumerate(relevance_list):
        if rel == 1:
            relevant_count += 1
            precision_sum += relevant_count / (i + 1)
    if relevant_count > 0:
        return precision_sum / relevant_count
    else:
        return 0.0