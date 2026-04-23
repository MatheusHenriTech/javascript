let nome=new String("Bruno Pinho Campos 1978")
let email="bruno@bruno.com.br"

console.log(nome)

console.log(nome.search(/pinho/i))

console.log(nome.match(/O/ig))

console.log(nome.replace(/o/ig, "Teste"))

console.log(nome.match(/\d/ig))
console.log(nome.match(/\s/ig))
console.log(nome.match(/\bP/ig))


console.log(nome.match(/no*/ig))