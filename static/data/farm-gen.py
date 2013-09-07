
import random
import json

class Server:
  def __init__(self, cpu, ram, network, disk):
    self.cpu = bound(cpu, 0, 1)
    self.ram = bound(ram, 0, 1)
    self.network = bound(network, 0, 1)
    self.disk = bound(disk, 0, 1)

  def mutate(self):
    deltaUsage = 1 + ((random.random() - 0.5) * 0.5)

    return Server(self.cpu * deltaUsage, self.ram * deltaUsage, self.network * deltaUsage, self.disk * deltaUsage)

  def __str__(self):
    return "cpu: %s, ram: %s, net: %s, disk: %s" % (self.cpu, self.ram, self.network, self.disk)

def randomServer():
  usage = 1 - (random.random() ** 3)
  cpuWeight = random.random()
  ramWeight = random.random()
  networkWeight = random.random()
  diskWeight = random.random()

  return Server(usage * cpuWeight, usage * ramWeight, usage * networkWeight, usage * diskWeight)

def bound(x, min, max):
  if x < min:
    return min
  elif x > max:
    return max
  else:
    return x

numServers = 32
numIterations = 32

initServers = map(lambda server: randomServer(), range(numServers))
serversOverTime = range(numIterations)
serversOverTime[0] = initServers

for i in range(1, len(serversOverTime)):
  serversOverTime[i] = map(lambda server: server.mutate(), serversOverTime[i - 1])

serversOverTime = map(lambda servers: 
  map(lambda server: server.__dict__, servers), serversOverTime)

with open('server-farm.json', 'w') as f:
  json.dump(serversOverTime, f)
