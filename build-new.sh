buildc() {
  mkdir -p build
  jsonnet $1 > build/config.json
}

buildj(){
  (cat build/config.json | jsonnet -c -m . --tla-str ctx="$(cat $1)" k8s/main.jsonnet)
}

buildc $1
buildj