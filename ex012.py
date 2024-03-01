print('=====Challenge 12=====')
price = float(input('Type a price: '))
descont = (price / 100) * 5
print('The new price is R${:.2f}'.format(price - descont))