from cards import *
import random
while True:
	firstcard=(random.sample(cards,1))
	secondcard=(random.sample(cards,1))
	thirdcard=(random.sample(cards,1))
	fourthcard=(random.sample(cards,1))
	fithcard=(random.sample(cards,1))
	if secondcard != firstcard and thirdcard != secondcard and  thirdcard != firstcard and fourthcard != thirdcard and fourthcard != secondcard and fourthcard != firstcard and fithcard != fourthcard and fithcard != thirdcard and fithcard != secondcard and fithcard != firstcard:
		print (firstcard)
		print(secondcard)
		print(thirdcard)
		print(fourthcard)
		print(fithcard)
		break


