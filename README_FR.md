# Kit de Traduction (Translate Direct)

Un kit d'outils Python pour le traitement de la traduction de documents Markdown, prenant en charge le nettoyage de documents, le traitement de paragraphes, la traduction et la gestion des progrès.

## Fonctionnalités

- **Nettoyage de Documents**: Nettoyer les lignes vides supplémentaires et les caractères spéciaux dans les fichiers Markdown
- **Traitement de Paragraphes**: Fusionner les paragraphes courts ou réduire le nombre de paragraphes
- **Traduction Intelligente**: Utiliser l'API DeepSeek pour la traduction chinois-anglais
- **Gestion des Progrès**: Supporter la sauvegarde et la récupération des progrès de traduction
- **Conversion de Format**: Convertir le contenu traduit au format EPUB
- **Décodage des Progrès**: Extraire le contenu traduit des fichiers de progrès

## Installation

```bash
pip install -r requirements.txt
```

## Description des Outils

### 1. Nettoyage de Documents (clean_md.py)

Nettoyer les problèmes de formatage dans les fichiers Markdown:

```bash
python clean_md.py
```

Fonctionnalités:
- Supprimer les lignes vides consécutives
- Nettoyer les espaces en début et fin de ligne
- Supprimer les caractères de contrôle spéciaux
- Normaliser les espaces
- Assurer une seule ligne vide entre les paragraphes

### 2. Fusion de Paragraphes (merge_paragraphs.py)

Fusionner les paragraphes courts pour réduire le nombre de paragraphes:

```bash
python merge_paragraphs.py
```

Paramètres:
- `min_length`: Seuil de longueur minimale des paragraphes (par défaut 150 caractères)

### 3. Réduction de Paragraphes (reduce_paragraphs.py)

Réduire intelligemment le nombre de paragraphes tout en maintenant la structure du document:

```bash
python reduce_paragraphs.py <fichier_entrée> [nombre_cible] [fichier_sortie]
```

Exemple:
```bash
python reduce_paragraphs.py book_merged.md 10 book_reduced.md
```

Fonctionnalités:
- Préserver la structure des titres et des listes
- Fusionner intelligemment les paragraphes réguliers
- Supporter le nombre de paragraphes cible personnalisé

### 4. Outil de Traduction (translate_md_to_epub.py)

Traduire les fichiers Markdown en utilisant l'API DeepSeek et convertir en EPUB:

```bash
python translate_md_to_epub.py <entrée.md> <sortie.epub> <clé_api> <langue_source>
```

Paramètres:
- `entrée.md`: Fichier Markdown d'entrée
- `sortie.epub`: Fichier EPUB de sortie
- `clé_api`: Clé API DeepSeek
- `langue_source`: Langue source (en/fr)

Exemple:
```bash
python translate_md_to_epub.py book.md book_translated.epub votre_clé_api en
```

Fonctionnalités:
- Supporter la sauvegarde et la récupération des progrès
- Reprendre la traduction après interruption
- Générer automatiquement les fichiers de progrès
- Supporter la traduction anglaise et française

### 5. Décodage des Progrès (decode_progress.py)

Extraire le contenu traduit des fichiers de progrès de traduction:

```bash
python decode_progress.py <fichier_progrès> [format_sortie]
```

Exemple:
```bash
python decode_progress.py book_progress.json md
python decode_progress.py book_progress.json txt
```

Fonctionnalités:
- Afficher les statistiques de progrès de traduction
- Extraire le contenu traduit
- Supporter la sortie au format Markdown et TXT
- Lister tous les fichiers de progrès

## Flux de Travail

1. **Prétraitement de Documents**:
   ```bash
   python clean_md.py          # Nettoyer le document original
   python merge_paragraphs.py  # Fusionner les paragraphes courts
   python reduce_paragraphs.py # Réduire le nombre de paragraphes (optionnel)
   ```

2. **Traitement de Traduction**:
   ```bash
   python translate_md_to_epub.py book_merged.md book_translated.epub votre_clé_api en
   ```

3. **Visualisation des Progrès**:
   ```bash
   python decode_progress.py book_merged_progress.json
   ```

## Description des Fichiers

- `clean_md.py`: Outil de nettoyage de documents
- `merge_paragraphs.py`: Outil de fusion de paragraphes
- `reduce_paragraphs.py`: Outil de réduction de paragraphes
- `translate_md_to_epub.py`: Outil de traduction et conversion EPUB
- `decode_progress.py`: Outil de décodage des progrès
- `requirements.txt`: Dépendances Python

## Notes Importantes

1. **Clé API**: Nécessite une clé API DeepSeek valide
2. **Encodage de Fichiers**: Tous les fichiers utilisent l'encodage UTF-8
3. **Fichiers de Progrès**: Le processus de traduction génère automatiquement des fichiers `*_progress.json`
4. **Récupération d'Interruption**: Appuyer sur Ctrl+C pendant la traduction pour sauvegarder les progrès et quitter
5. **Taille de Fichier**: Recommander de réduire le nombre de paragraphes avant le traitement pour améliorer l'efficacité de traduction

## Variables d'Environnement

Vous pouvez définir des variables d'environnement pour éviter d'exposer les clés API dans la ligne de commande:

```bash
export DEEPSEEK_API_KEY="votre_clé_api_ici"
```

Puis utiliser un espace réservé dans la ligne de commande:
```bash
python translate_md_to_epub.py book.md sortie.epub <CLÉ_API> en
```

## Licence

Ce projet est destiné à l'apprentissage et à l'usage personnel uniquement.

---

## Versions Multilingues

- [中文版本](README_CN.md)
- [English Version](README.md) 