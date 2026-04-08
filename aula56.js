const caixa=document.querySelector("#caixa")

const carros=["Polo", "Golf", "T-Cross", "HRV"]

let ol=`<ul>`
carros.map((el)=>{
    ol+=`<li>${el}</li>`
})
ol+=`</ul>`


caixa.innerHTML=ol