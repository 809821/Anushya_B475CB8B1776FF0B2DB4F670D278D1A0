def linearSearchProduct(productList,tragetproduct):
  indices=[]
  for index, product in enumerate(productList):
    if product==tragetproduct:
       indices.append(index)
    return(indices)
    product=["apple","banana","berry","apple","pineapple",
            "apple"]
    traget="apple"
    traget2="sky"
    result=linearSearchProduct(product,traget,traget2)
    print(result)