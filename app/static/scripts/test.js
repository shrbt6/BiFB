document.addEventListener('DOMContentLoaded', function(){
    let testCount = 0;
    let testText = document.getElementById('test-text')

    document.getElementById('test-button').addEventListener('click', function() {
        testCount += 1;
        console.log(testCount);
    }, false)
}, false)