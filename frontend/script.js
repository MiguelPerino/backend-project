async function loadProducts(search = "") {
    let url = "http://localhost:5000/products";

    if (search) {
        url += `?search=${encodeURIComponent(search)}`;
    }

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
    loadProducts(searchInput.value);
});


loadProducts();