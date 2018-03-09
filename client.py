import requests
r = requests.get("http://vcm-3551.vm.duke.edu:5000/name")
name = r.json()

r1 =requests.get("http://vcm-3551.vm.duke.edu:5000/hello/Yi Zhao")
hello =r1.json()

r2 = requests.post("http://vcm-3551.vm.duke.edu:5000/distance",json={"a":[2,5],"b":[4,5]})
distance = r2.json()
print("The response was {0}.".format(distance['distance']))

