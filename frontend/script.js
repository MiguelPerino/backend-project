async function loadProducts(search = "") { //search parametro que vai vir da pesquisa
    let url = "http://localhost:5000/products";

    if (search) {
        url += `?search=${encodeURIComponent(search)}`; //codifica o texto pra ser colocado dentro da url, por exemplo acento e espaço
    }                       
    
    //manda requisicao pro flask
    const response = await fetch(url);
    const data = await response.json();

    const products = data.products;

    const productGrid = document.getElementById("product-grid");

    // Limpa os produtos anteriores
    productGrid.innerHTML = "";

    products.forEach(product => {

        const card = document.createElement("article");
        card.classList.add("product-card");

        let image;

        if (product.name === "Salmão") {
            image = "imgs/salmao.png";
        } else if (product.name === "Pirarara") {
            image = "imgs/pirara.png";
        } else if (product.name === "Tilápia") {
            image = "imgs/tilapa.png";
        }
        else if (product.name === "Pacu") {
            image = "imgs/pacu.jpeg";
        }
        else if (product.name === "Piranha") {
            image = "imgs/piranha.jpeg";
        }
        else if (product.name === "Traíra") {
            image = "imgs/traira.jpeg";
        }

        card.innerHTML = `
            <img src="${image}" alt="${product.name}" class="product-image">

            <h3>${product.name}</h3>

            <p>${product.description}</p>

            <strong>R$ ${product.price}</strong>

            <span>Estoque: ${product.stock}</span>
        `;

        productGrid.appendChild(card);
    });
}


const searchButton = document.getElementById("search-button");
const searchInput = document.getElementById("search-input");


searchButton.addEventListener("click", () => {
    loadProducts(searchInput.value); //aqui traz o valor da pesquisa do usuario
});


loadProducts();