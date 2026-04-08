const caixa=document.querySelector("#caixa")


let cores=["azul", "verde", "vermelho",["claro", "escuro", "médio"]]
let cursos=["HTML", "CSS", "Javascript", cores]

// cursos.push("c++")
// cursos.unshift("Python")
// cursos.shift()

console.log(cursos[3][3][2])

cursos.map((el)=>{
    let p=document.createElement("p")
    p.innerHTML=el
    caixa.appendChild(p)
})
console.log(cursos)
