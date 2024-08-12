async function getName() {
    const result = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    const json = await result.json()

    const characterId = document.getElementById("character")
    characterId.textContent = json.name
}

getName()