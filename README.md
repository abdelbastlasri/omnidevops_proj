# TodoList App - Instructions de Déploiement Docker

## Prérequis
- Docker installé sur votre système
- Docker Compose installé (optionnel, mais recommandé)

## Structure du Projet
```
todolist-app/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── Dockerfile            # Configuration Docker
├── docker-compose.yml    # Configuration Docker Compose
├── .dockerignore         # Fichiers à ignorer lors du build
├── templates/            # Templates HTML
│   ├── _baselayout.html  # Template de base
│   ├── home.html         # Page d'accueil
│   ├── _form.html        # Formulaire d'édition
│   └── todo/
│       └── _item.html    # Template d'item todo
└── README.md             # Ce fichier
```

## Méthode 1: Avec Docker Compose (Recommandée)

### 1. Construire et démarrer l'application
```bash
cd todolist-app
docker-compose up --build
```

### 2. Accéder à l'application
Ouvrez votre navigateur et allez à: `http://localhost:8090`

### 3. Arrêter l'application
```bash
docker-compose down
```

## Méthode 2: Avec Docker uniquement

### 1. Construire l'image Docker
```bash
cd todolist-app
docker build -t todolist-app .
```

### 2. Démarrer le conteneur
```bash
docker run -d -p 8090:8090 --name todolist-container todolist-app
```

### 3. Accéder à l'application
Ouvrez votre navigateur et allez à: `http://localhost:8090`

### 4. Arrêter et supprimer le conteneur
```bash
docker stop todolist-container
docker rm todolist-container
```

## Commandes Utiles

### Voir les logs du conteneur
```bash
# Avec Docker Compose
docker-compose logs -f

# Avec Docker
docker logs -f todolist-container
```

### Redémarrer l'application
```bash
# Avec Docker Compose
docker-compose restart

# Avec Docker
docker restart todolist-container
```

### Reconstruire l'image après modifications
```bash
# Avec Docker Compose
docker-compose up --build

# Avec Docker
docker build -t todolist-app .
docker stop todolist-container
docker rm todolist-container
docker run -d -p 8090:8090 --name todolist-container todolist-app
```

## Configuration VSCode

### 1. Extensions recommandées
- Docker (Microsoft)
- Python (Microsoft)

### 2. Fichier de configuration VSCode (optionnel)
Créez `.vscode/launch.json` pour déboguer:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "program": "app.py",
            "env": {
                "FLASK_ENV": "development"
            },
            "args": [],
            "jinja": true
        }
    ]
}
```

## Fonctionnalités de l'Application

- ✅ Ajouter des tâches
- ✅ Modifier des tâches (clic sur le texte)
- ✅ Supprimer des tâches (bouton X)
- ✅ Interface responsive avec UIKit
- ✅ Interactions HTMX pour une expérience fluide
- ✅ Données persistantes en mémoire (redémarrage = perte des données)

## Personnalisation

### Changer le port
Modifiez le port dans:
1. `app.py` (ligne 68)
2. `Dockerfile` (EXPOSE et CMD)
3. `docker-compose.yml` (ports)

### Ajouter une base de données
Pour persister les données, ajoutez une base de données comme SQLite ou PostgreSQL dans `docker-compose.yml`.

## Dépannage

### Port déjà utilisé
Si le port 8090 est occupé, changez-le dans les fichiers de configuration.

### Problèmes de build
Supprimez les images et conteneurs existants:
```bash
docker-compose down --rmi all
docker system prune -f
```

