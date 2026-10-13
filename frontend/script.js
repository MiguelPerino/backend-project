const API_URL = "http://localhost:5000";

const searchInput = document.getElementById("search-input");
const searchButton = document.getElementById("search-button");
const productGrid = document.getElementById("product-grid");


// Pede os produtos ao backend, "search" vem do campo de pesquisa.
async function fetchProducts(search = "") {
    let url = `${API_URL}/products`;

    if (search) {
        //trata acentos e espaços para ir na URL
        url += `?search=${encodeURIComponent(search)}`;
    }

    const response = await fetch(url);

    if (!response.ok) {
        throw new Error("Erro ao buscar produtos");
    }

    const data = await response.json();
    return data.products;
}


function createProductCard(product) {
    const card = document.createElement("article");
    card.classList.add("product-card");

    card.innerHTML = `
        <img src="imgs/${product.image}" alt="${product.name}" class="product-image">

        <h3>${product.name}</h3>

        <p>${product.description}</p>

        <strong>R$ ${product.price}</strong>

        <span>Estoque: ${product.stock}</span>

        <span class="seller-name">Vendedor: ${product.seller}</span>
    `;

    return card;
}


// mostra uma mensagem no lugar dos cards (sem resultado ou erro)
function showMessage(text) {
    productGrid.innerHTML = `<p class="message">${text}</p>`;
}


// Desenha os cards na tela
function renderProducts(products) {
    productGrid.innerHTML = "";

    if (products.length === 0) {
        showMessage("Nenhum peixe ou vendedor encontrado.");
        return;
    }

    products.forEach(product => {
        productGrid.appendChild(createProductCard(product));
    });
}


// Busca e desenha. É chamada ao abrir a página e ao pesquisar.
async function loadProducts(search = "") {
    try {
        const products = await fetchProducts(search);
        renderProducts(products);
    } catch (error) {
        showMessage("Ixi deu ruim");
    }
}


searchButton.addEventListener("click", () => {
    loadProducts(searchInput.value.trim());
});

// Também pesquisa ao apertar Enter
searchInput.addEventListener("keydown", event => {
    if (event.key === "Enter") {
        loadProducts(searchInput.value.trim());
    }
});


loadProducts();
