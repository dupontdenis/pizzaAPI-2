const API_BASE = "http://localhost:8000/api/pizzas/";

const list = document.getElementById("pizza-list");
const details = document.getElementById("pizza-detail");
const ingredientsInput = document.getElementById("ingredients");
const modeSelect = document.getElementById("match-mode");
const filterForm = document.getElementById("filter-form");
const message = document.getElementById("message");

// Récupérer les pizzas depuis l'API
async function getPizzas(url = API_BASE) {
    const response = await fetch(url);

    if (!response.ok) {
        throw new Error(`Erreur HTTP : ${response.status}`);
    }

    return response.json();
}

// Afficher la liste des pizzas
function displayPizzas(pizzas) {
    if (pizzas.length === 0) {
        list.innerHTML = `
            <p class="text-muted mb-0">
                Aucune pizza trouvée.
            </p>
        `;
        return;
    }

    list.innerHTML = pizzas.map(pizza => `
        <button
            type="button"
            class="list-group-item list-group-item-action"
            data-id="${pizza.id}"
        >
            ${pizza.name}
        </button>
    `).join("");
}

// Charger toutes les pizzas
async function loadPizzas() {
    message.textContent = "";

    try {
        const pizzas = await getPizzas();
        displayPizzas(pizzas);
    } catch (error) {
        list.innerHTML = "";
        message.className = "text-danger mt-3 mb-0";
        message.textContent = "Impossible de charger les pizzas.";
        console.error(error);
    }
}

// Afficher le détail d'une pizza
async function loadPizzaDetails(id) {
    details.textContent = "Chargement du détail...";

    try {
        const pizza = await getPizzas(`${API_BASE}${id}/`);

        const ingredientItems = pizza.ingredients.map(ingredient => `
            <li class="list-group-item d-flex justify-content-between">
                <span>${ingredient.name}</span>
                <span>${Number(ingredient.price).toFixed(2)} €</span>
            </li>
        `).join("");

        const totalPrice = pizza.ingredients.reduce(
            (total, ingredient) => total + Number(ingredient.price),
            0
        );

        details.innerHTML = `
            <h3 class="h5 fw-bold mb-3">${pizza.name}</h3>

            <ul class="list-group mb-3">
                ${ingredientItems}
            </ul>

            <p class="fw-bold text-end mb-0">
                Prix des ingrédients : ${totalPrice.toFixed(2)} €
            </p>
        `;
    } catch (error) {
        details.textContent = "Impossible de charger ce détail.";
        console.error(error);
    }
}

// Réagir au clic sur une pizza
list.addEventListener("click", event => {
    const button = event.target.closest("button[data-id]");

    if (button && list.contains(button)) {
        loadPizzaDetails(button.dataset.id);
    }
});

// Filtrer les pizzas
filterForm.addEventListener("submit", async event => {
    event.preventDefault();

    const params = new URLSearchParams();
    const ingredients = ingredientsInput.value.trim();

    if (ingredients) {
        params.set("ingredients", ingredients);
        params.set("mode", modeSelect.value);
    }

    const url = params.size
        ? `${API_BASE}?${params.toString()}`
        : API_BASE;

    message.className = "text-muted mt-3 mb-0";
    message.textContent = "Recherche en cours...";

    try {
        const pizzas = await getPizzas(url);

        displayPizzas(pizzas);
        message.textContent = `${pizzas.length} pizza(s) trouvée(s).`;
    } catch (error) {
        list.innerHTML = "";
        message.className = "text-danger mt-3 mb-0";
        message.textContent = "Impossible de filtrer les pizzas.";
        console.error(error);
    }
});

loadPizzas();