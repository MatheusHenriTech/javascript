const f_texto=document.querySelector("#f_texto")
const p_texto=document.querySelector("#p_texto")
const btn_texto=document.querySelector("#btn_texto")

btn_texto.addEventListener("click",(evt)=>{

})

let num=10
let curso="Javascript"
// localStorage.setItem("nome","Bruno")
// localStorage.setItem("curso",curso)
// localStorage.setItem("numero",num)
// localStorage.setItem("numero",33)
// alert(localStorage.length)


// alert(localStorage.getItem(localStorage.key(0)))
// alert(localStorage.getItem("numero"))
// alert(localStorage.getItem("nome"))
// alert(localStorage.getItem("curso"))
localStorage.clear()

sessionStorage.setItem("nome","Bruno")
sessionStorage.setItem("canal","CFB Cursos")
sessionStorage.setItem("curso",curso)
