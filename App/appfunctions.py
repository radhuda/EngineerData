def purchase_classifier(x):

    if x == '30' or x == '40' or x == '50':
        y = "In stock for immediate delivery"
    if x == '20':
        y = "make on demand - 80%+ success, Takes 5 weeks to make"
    if x == '10':
        y = 'boutique - may be expensive, but worth asking'
    if x == '7':
        y = 'one-step - synthetically accessible in one step from commercial building blocks'
    if x == '3':
        y = 'may be available plated in libraries.'
    if x == '1':
        y = 'not for sale - often annotated'

    return y