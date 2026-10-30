class FitChecker:
    def __init__(self, overfit_threshold, underfit_threshold):
        if underfit_threshold >= overfit_threshold:
            raise ValueError("underfit_threshold must be less than overfit_threshold")

        self.overfit_threshold = overfit_threshold
        self.underfit_threshold = underfit_threshold

    def get_status(self, train_loss, val_loss):
        gap = val_loss - train_loss

        if gap > self.overfit_threshold:
            return "overfitting"
        elif gap < self.underfit_threshold:
            return "underfitting"
        else:
            return "good_fit"
