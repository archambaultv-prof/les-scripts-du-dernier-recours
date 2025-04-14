# ✏️ `c3hm` : Corriger à 3 heures du matin

**Ici on ne juge pas, sauf les travaux.**

Bienvenue dans le *sanctuaire obscur de la correction semi-automatisée*.
`c3hm` est une interface de ligne de commande conçue pour les profs de cégep qui
veulent survivre à la tempête de copies.

> [!WARNING]
> `c3hm` est actuellement en développement actif. Certaines
> fonctionnalités peuvent être instables ou sujettes à modification.

## 🧰 Fonctionnalités

Pendant que tu regrettes ton choix de carrière face à la montagne de
copies à corriger, `c3hm` vient à ta rescousse. Il te permet de :

- **Nettoyer** les remises des étudiant·e·s, comme un aspirateur numérique. Bye bye
  `node_modules`, `.git`, `.venv`, et autres joyeusetés. Ton OneDrive sera tellement content !

Pour l'instant c'est tout, mais on a de grands projets pour l'avenir. Reste à l'écoute !

## ⚙️ Comment ça marche ?

### c3hm poubelle

```bash
python3 c3hm.py poubelle --help
```

Cette commande nettoie les remises des étudiant·e·s en supprimant les fichiers et
dossiers inutiles. Pour l'instant elle supprime

- `__pycache__`
- `.DS_Store`
- `.git`
- `.idea`
- `.pytest_cache`
- `.venv`
- `.vscode`
- `node_modules`

Le nom de chaque dossier d'étudiant·e doit être conforme à celui
généré par Omnivox. Par exemple : `NOM1_NOM2_123456789_`.

> [!NOTE]
> `node_modules` peut être très long à supprimer, surtout s'il est sur OneDrive.