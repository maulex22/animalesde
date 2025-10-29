# Ejemplo simple para practicar Pull Request

## Pasos generales

1. Hacer fork del repositorio principal.

2. Crear una nueva rama con su nombre o matrícula.

3. Editar animales.py y agregar un nuevo animal a la lista.

4. Hacer commit y push a su rama.

5. Crear un pull request al repositorio original.


## Sincronización


No olvide tener actualizado su repositorio clonado usando la herramienta de sincronización de GitHub o manteniendo su rama upstream.

## Definir rama upstream

Una rama upstream en Git se refiere a la rama principal de un repositorio original, o el repositorio desde el cual se bifurcó un proyecto, y que se utiliza para mantener un enlace de seguimiento y sincronización.  Ejemplo con un repositorio recetario.

```bash
git remote -v
```

```bash
origin   git@github.com:jlqf/recetario.git (fetch)
origin   git@github.com:jlqf/recetario.git (push)
```

ejecutar:

```bash
git remote add upstream git@github.com:Taller-jlqf/recetario-pull.git
git remote -v
```

debería ver algo similar:

```bash
origin   git@github.com:jlqf/recetario.git (fetch)
origin   git@github.com:jlqf/recetario.git (push)
upstream git@github.com:Taller-jlqf/recetario-pull.git (fetch)
upstream git@github.com:Taller-jlqf/recetario-pull.git (push)
```

## Sincronización usando upstream


Trae cambios nuevos del origina

```bash
git fetch upstream
```
Actualiza tu main local
```bash
git switch main
git merge --ff-only upstream/main
```

Mezcla tu rama con la nueva main
```bash
git switch rama-dev
git merge main
```
```bash
Resuelve conflictos, guarda y sube
git add .
git commit                # (merge) 
git push                  # (merge)
```


