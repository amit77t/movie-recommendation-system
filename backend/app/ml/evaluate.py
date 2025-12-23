from surprise import accuracy

def evaluate(model, testset):
    predictions = model.test(testset)
    print("RMSE:", accuracy.rmse(predictions))
