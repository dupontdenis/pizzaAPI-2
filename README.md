# API Pizza

## Installation après clonage

Le projet comprend une API Django et un client web statique. Il faut démarrer **deux serveurs**, chacun dans son propre terminal : le premier sert l'API Python, le second sert la page du client.

### 1. Installer et démarrer l'API Django

À la racine du projet, créez un environnement virtuel et activez-le.

**Windows (PowerShell) :**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux :**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Installez ensuite les dépendances et préparez la base de données :

```bash
python -m pip install -r requirements.txt
python manage.py migrate
```

Démarrez l'API dans ce premier terminal :

```bash
python manage.py runserver
```

L'API est alors accessible sur `http://localhost:8000/`. Laissez ce terminal ouvert.

### 2. Démarrer le client web

Ouvrez un **deuxième terminal**, puis démarrez le serveur statique depuis le dossier `client` :

```bash
cd client
python -m http.server 5500
```

Ouvrez `http://localhost:5500` dans votre navigateur. Laissez également ce terminal ouvert. Le client contacte l'API sur `http://localhost:8000`; les deux serveurs doivent donc fonctionner en même temps. Pour les arrêter, utilisez `Ctrl+C` dans chacun des terminaux.

## Adresse de base

`http://localhost:8000/api/`

L'API est le backend du projet : elle lit les pizzas et leurs ingrédients dans la base SQLite, puis renvoie les résultats au client au format JSON. Les routes ci-dessous sont des requêtes de lecture (`GET`). Le client web appelle ces routes pour afficher la liste, filtrer les pizzas et charger le détail sélectionné.

## 1. Liste des pizzas

**Requête :** `GET /api/pizzas/`

Retourne la liste des pizzas avec leur identifiant, leur nom et leurs ingrédients.

## 2. Filtrer les pizzas par ingrédients

**Requête :** `GET /api/pizzas/?ingredients=Tomate,Mozza&mode=and`

| Paramètre     | Obligatoire | Description                                                                           |
| ------------- | ----------- | ------------------------------------------------------------------------------------- |
| `ingredients` | Non         | Noms des ingrédients séparés par des virgules.                                        |
| `mode`        | Non         | `or` pour rechercher au moins un ingrédient ; `and` pour exiger tous les ingrédients. |

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
