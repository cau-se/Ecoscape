{
  context: import '../context/cluster.json',
  monitor: import '../monitor/monitor.json',
  infra: {
    base: import '../infra/infra.json',
    chaos: import '../infra/cpu-stress.json',
    #networkChaos: import '../infra/network-chaos.json'
  },
  data: {
    kafka: import '../kafka/kafka.json'
  },
  sut: {
    base: import '../sut/sut-object-classifier.json',
    networkChaos: import '../sut/sut-object-classifier-patch.json',
    resourceChaos: import '../sut/sut-object-classifier-patch2.json'
  },
  load: {
    base: import '../load/load-image-producer.json',
  }
}