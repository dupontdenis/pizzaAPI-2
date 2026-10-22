# API Pizza

## Adresse de base

`http://localhost:8000/api/`

## 1. Liste des pizzas

**Requête :** `GET /api/pizzas/`

Retourne la liste des pizzas avec leur identifiant, leur nom et leurs ingrédients.

## 2. Filtrer les pizzas par ingrédients

**Requête :** `GET /api/pizzas/?ingredients=Tomate,Mozza&mode=and`

| Paramètre | Obligatoire | Description |
|---|---|---|
| `ingredients` | Non | Noms des ingrédients séparés par des virgules. |
| `mode` | Non | `or` pour rechercher au moins un ingrédient ; `and` pour exiger tous les ingrédients. |

### Exemples

**Au moins un ingrédient (OU)**

`GET /api/pizzas/?ingredients=Tomate,Mozza&mode=or`

Retourne les pizzas qui contiennent de la tomate ou de la mozzarella.

**Tous les ingrédients (ET)**

`GET /api/pizzas/?ingredients=Tomate,Mozza&mode=and`

Retourne les pizzas qui contiennent à la fois de la tomate et de la mozzarella.

Si `mode` est absent, le mode par défaut est `or`.

## 3. Détail d'une pizza

**Requête :** `GET /api/pizzas/3/`

Retourne le détail de la pizza dont l'identifiant est `3`, avec ses ingrédients.

Si cette pizza n'existe pas, l'API retourne une erreur HTTP 404.
