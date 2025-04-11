# 🚀 Guide LaTeX Galactique Interstellaire

Vous trouverez ici non seulement des gabarits LaTeX venus d'ailleurs, mais
aussi des astuces cosmiques pour écrire des examens les plus improbables.

N'oubliez jamais votre serviette, ne paniquez surtout pas et si jamais vous
cherchez la réponse à la grande question sur la vie, l'univers et le reste ...
c’est probablement 42.

Bonne exploration !

## 📄 Gabarits disponibles 

**Tous nos gabarits sont homologués par le Conseil Interstellaire des Examinateurs Fatigués.**

Voici les gabarits LaTeX officiels utilisés à bord de nombreux vaisseaux
pédagogiques à travers la galaxie connue (et quelques coins obscurs du cégep).

- [examen](examen/examen.tex) :  le modèle ultime pour interroger des formes de
  vie intelligentes ou, à défaut, vos étudiants. ([version PDF](examen/examen.pdf))

## 🛸 Minted, LuaLaTeX et autres magouilles cosmiques

Les gabarits LaTeX sont conçus pour fonctionner avec LuaLaTeX, un moteur de
composition légendaire, recommandé par 9 examinateurs sur 10 dans la Voie
lactée (le dixième utilise Word, mais il a été banni de la Fédération).

Certains gabarits utilisent le package `minted`, une technologie avancée de
coloration syntaxique alimentée par des trous de ver et Pygments.

Pour compiler avec succès (et ne pas provoquer l’effondrement d’un système
stellaire), assurez-vous de :

- Avoir [Pygments](https://github.com/pygments/pygments) installé sur votre planète locale.
- Utiliser l’option `--shell-escape`, sans quoi les couleurs disparaîtront dans un
cri silencieux.

Exemple de rituel d’invocation :

```bash
latexmk -lualatex -shell-escape examen.tex
```

*💡 Attention : ne pas exécuter cette commande à proximité d’un générateur d’improbabilité infinie.*