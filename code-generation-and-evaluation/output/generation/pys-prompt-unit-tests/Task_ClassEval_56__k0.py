class MetricsCalculator:
    def __init__(self):
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

    def update(self, actual, predicted):
        for a, p in zip(actual, predicted):
            if a == 1 and p == 1:
                self.true_positives += 1
            elif a == 0 and p == 1:
                self.false_positives += 1
            elif a == 1 and p == 0:
                self.false_negatives += 1
            else:
                self.true_negatives += 1

    def precision(self, actual, predicted):
        tp = sum(1 for a, p in zip(actual, predicted) if a == 1 and p == 1)
        fp = sum(1 for a, p in zip(actual, predicted) if a == 0 and p == 1)
        return tp / (tp + fp) if tp + fp > 0 else 0

    def recall(self, actual, predicted):
        tp = sum(1 for a, p in zip(actual, predicted) if a == 1 and p == 1)
        fn = sum(1 for a, p in zip(actual, predicted) if a == 1 and p == 0)
        return tp / (tp + fn) if tp + fn > 0 else 0

    def f1_score(self, actual, predicted):
        precision = self.precision(actual, predicted)
        recall = self.recall(actual, predicted)
        return 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0

    def accuracy(self, actual, predicted):
        tp = sum(1 for a, p in zip(actual, predicted) if a == 1 and p == 1)
        tn = sum(1 for a, p in zip(actual, predicted) if a == 0 and p == 0)
        return (tp + tn) / len(actual) if len(actual) > 0 else 0
