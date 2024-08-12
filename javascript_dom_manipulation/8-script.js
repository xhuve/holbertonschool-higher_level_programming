async function displayHello() {
    const result = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    const json = await result.json()

    const helloSection = document.getElementById("hello")
    helloSection.textContent = json.hello
}
 
displayHello()