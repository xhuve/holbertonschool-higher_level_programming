async function getMovies() {
    const result = await fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    const json = await result.json()

    const moviesList = document.getElementById("list_movies")
    json.results.map((movie) => {
        const list = document.createElement("li")
        list.textContent = movie.title
        moviesList.appendChild(list)
    })
}

getMovies()