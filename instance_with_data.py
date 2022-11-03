cityName=['Detroite','Ann Arbor','Pittsburgh','Mars','New York']
populations=[68025,117070,304391,1683,8406000]
states=['MI','MI','PA','PA','NY']
city_tuples= list(zip(cityName,populations,states)) 


class City:
    def __init__(self, n , p , s):
        self.name=n
        self.populetion=p
        self.state=s

    def __str__(self):

        return "{},{},(pop:{})".format(self.name,self.state,self.populetion)

citys=[]

for cit in city_tuples:
     name, pop, state = cit
     city=City(name, pop, state)
     citys.append(city)
     print(city)
#print(citys)
#trythis= [City(*t) for t in city_tuples]
#citys.append(trythis)
#print(trythis)
#print(citys)


