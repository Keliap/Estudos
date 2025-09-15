function getProjects(){
    const urlGithub= 'https://api.github.com/users/keliap/repos'
    var loadingElement = document.getElementById('carregando')
    fetch(urlGithub, {
        
        method: 'GET'
    })
    .then((response) => response.json())
    .then((response) => {
        loadingElement.style.display='none'
        console.log(response)
        showProjects(response)
    })
    .catch((erro) =>{
        console.log(erro)
    })
}

function showProjects(data){
    var listElement = document.getElementById('lista-projetos')
    for(let i = 0; i< data.length; i ++){

        let a = document.createElement("a")
        a.href = data[i]['clone_url']
        a.target ='_blank'
        a.title = data[i]['description']
        let linkText = document.createTextNode(data[i]['name'])
        a.appendChild(linkText)
        listElement.appendChild(a)
    }


}
getProjects()