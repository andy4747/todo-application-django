let activeItem=null
let host='127.0.0.1'
let port='8000'

const buildList=function() {
    let wrapper=document.getElementById('list-wrapper')
    wrapper.innerHTML=''
    let url=`http://${host}:${port}/api/task-list/`
    fetch(url)
    .then((response)=>response.json())
    .then((data)=>{
        console.log('Data: ',data)

        let list=data
        for (var i in list) {
            let title=`<span class="title">${list[i].title}</span>`
            if (list[i].completed==true) {
                title=`<strike style="color:red" class="title">${list[i].title}</strike>`
            }
            let item=`
                <div id="data-row-${i}" class="task-wrapper flex-wrapper">
                    <div style="flex:7">
                        ${title}
                    </div>
                    <div style="flex:1">
                        <button class="edit"><i class="fas fa-pencil-alt"></i></button>
                    </div>
                    <div style="flex:1">
                        <button class="delete"><i class="fas fa-trash-alt" style="color:#ff3333"></i></button>
                    </div>
                </div>
            `
            wrapper.innerHTML+=item
        }

        for (var i in list) {
            let editBtn=document.getElementsByClassName('edit')[i]
            let deleteBtn=document.getElementsByClassName('delete')[i]
            let title=document.getElementsByClassName('title')[i]
            editBtn.addEventListener('click',((item)=>{
                return ()=>{
                    editItem(item)
                }
            })(list[i]))
            deleteBtn.addEventListener('click',((item)=>{
                return ()=>{
                    deleteItem(item)
                }
            })(list[i]))
            title.addEventListener('click',((item)=>{
                return ()=>{
                    jobStatusSwitcher(item)
                }
            })(list[i]))
        }
    })
}
buildList()

let form=document.getElementById('form-wrapper')
form.addEventListener('submit',(e)=>{
    e.preventDefault()
    console.log("form submitted")
    let url=`http://${host}:${port}/api/task-create/`
    if (activeItem!=null) {
        let url=`http://${host}:${port}/api/task-update/${activeItem.id}`
    }
    let title=document.getElementById('title').value
    fetch(url,{
        method:'POST',
        headers:{
            'Content-type':'application/json',
        },
        body:JSON.stringify({
            'title':title
        })
    })
    .then((response)=>{
        buildList()
        document.getElementById('form').reset()
    })
})

function editItem(item) {
    console.log("item clicked: ",item)
    activeItem=item
    document.getElementById('title').value=activeItem.title
}

function deleteItem(item) {
    console.log("delete clicked: ",item)
    fetch(`http://${host}:${port}/api/task-delete/${item.id}`,{
        method:'DELETE',
        headers:{
            'Content-type':'application/json'
        }
    })
    .then((response)=>{
        buildList()
    })

}

function jobStatusSwitcher(item) {
    console.log('sataus switcher clicker')
    item.completed=!item.completed
    fetch(`http://${host}:${port}/api/task-update/${item.id}`,{
        method:'POST',
        headers:{
            'Content-type':'application/json'
        },
        body:JSON.stringify({
            'title':item.title,
            'completed':item.completed
        })
    })
    .then((response)=>{
        buildList()
    })
}