from transformers import pipeline


x = lambda a: '*' + a + '*'

# Allocate a pipeline for sentiment-analysis
classifier = pipeline('sentiment-analysis')

result1 = classifier('We are very happy to introduce pipeline to the transformers repository.')
print(result1)


result2 = classifier('We are sad to see Hong Kong.')
print(result2)

result3 = classifier('We are what we are')
print(result3)

result4 = classifier('We are not sad')
print(result4)

print(x("Jack"))


