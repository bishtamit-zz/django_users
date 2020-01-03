console.log('main loaded');

let element = document.getElementById('main-searchbox');
console.log(element);
element.addEventListener('keyup', (event) => {
    console.log(element.value)
});