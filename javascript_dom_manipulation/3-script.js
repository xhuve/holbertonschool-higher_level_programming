document.getElementById("toggle_header").addEventListener("click", () => {
    const headerTagClass = document.querySelector("body header").classList
    if (headerTagClass.contains("red"))
        headerTagClass.replace("red", 'green')
    else
        headerTagClass.replace("green", 'red')
        
});