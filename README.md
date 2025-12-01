Ce projet implémente un **agent à réflexe simple** simulé en Python avec Pygame. L’agent représente un petit aspirateur autonome chargé de nettoyer deux chambres : **A** et **B**. Il applique des règles simples basées uniquement sur l’état actuel :

* Si A et B sont sales, il nettoie les deux.
* Si seule A est sale, il nettoie A.
* Si seule B est sale, il nettoie B.
* Si tout est propre, il patrouille entre les chambres.

L’agent ne possède **aucune mémoire**, ne planifie pas et ne construit pas de modèle interne du monde. Cette simulation illustre le fonctionnement d’un **agent à réflexe simple**, l’un des types d’agents les plus fondamentaux étudiés en Intelligence Artificielle. Le projet inclut une petite interface graphique pour visualiser les chambres et le robot en action.
