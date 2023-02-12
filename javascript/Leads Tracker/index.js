const saveBtn = document.getElementById('save-btn')
const saveTabBtn = document.getElementById('save-tab-btn')
const clearBtn=document.getElementById('clear-btn')
const urlEl = document.getElementById('url-el')
const urlNameEl = document.getElementById('url-name-el')
const outEl = document.getElementById('out-el')
let myUrls =[]
const localStorageUrls = JSON.parse(localStorage.getItem("myUrls"))

if (localStorageUrls) {
    myUrls = localStorageUrls
    render(myUrls)
}

function render(urls) {
    list = ''
    for (let i = 0; i < urls.length; i++) {
        list += `<li>
                    <a target='_blank' href='${urls[i][0]}'>
                    ${(urls[i][1]==="")?urls[i][0]:urls[i][1]}
                    </a>
                </li>`;
        
        
    }
    outEl.innerHTML=list
}
saveTabBtn.addEventListener('click', function(){
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
        myUrls.push([tabs[0].url,urlNameEl.value])
        localStorage.setItem("myUrls", JSON.stringify(myUrls) )
        render(myUrls)
    })
})
saveBtn.addEventListener('click',function () {
    myUrls.push([urlEl.value,urlNameEl.value])
    urlEl.value = ''
    localStorage.setItem("myUrls", JSON.stringify(myUrls))
    render(myUrls)
})

clearBtn.addEventListener('dblclick', function () {
    localStorage.clear()
    myUrls = []
    render(myUrls)
})