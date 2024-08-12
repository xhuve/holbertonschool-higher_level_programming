document.getElementById("add_item").addEventListener("click", () => {
    const ul = document.querySelector("ul.my_list").appendChild(document.createElement("li"))
    ul.textContent = "Item"
});