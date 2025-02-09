# Áreas de trabalho no GIT

## Working Directory

## Staging Area

## .git directory (Repository)

## Comandos Básicos

## Como iniciar um repositorio local

```md
```shell
#!/bin/bash
git init
```

## Verificar situação do repositório

```md
```shell
#!/bin/bash
git status
```

## Como adicionar um arquivo na área de staging

```md
```shell
#!/bin/bash
git add .
```

## Commitar um arquivo na Staging Area

```md
```shell
#!/bin/bash
git add .
git commit -m "Mensagem do commit"
```

## Desfazer as alterações no working directory

```md
```shell
  git restore <nome_do_arquivo>
```

## Remover arquivos da staging area

```md
```shell
  git restore -- staged <nome_do_arquivo>
```

## Visualizar histórico de commits

Mostra o hostórico de commits em apenas uma linha

```md
```shell
  git log --oneline
```

Mostra o historico de commits com a difereça entre eles
  -p mostra as diferenças
  -2 significa que é pra mostrar a difereça dos 2 ultimos

```md
```shell
  git log --oneline -p -2 
```

## Arrumar o histórico de commits

### Alterando o último commit

Para alterar a mensagem do ultimo commit

```md
```shell
  git commit -m "Mensagem" -- amend
```

## Visualizando diferenças entre commits

Deve-se passar o hash do commit

```md
```shell
  git diff <commit_antigo> <commit_atual>
```

## Comando git rebase

### Rebase interativo

Ele permite editar, reordenar, combinar ou descartar commits. n é o número de commits a trazer a partir do HEAD

```md
```shell
  git rebase -i HEAD~n
```

Dentro o interativo pode-e usar o squash para agrupar commits

Para restaurar o repositorio a um commit anterior, usa-se o rebase também

git rebase --hard <hash_do_commit> -> apaga todas as alterações recentes e volta para o cimmit informado

git  rebase --mixed <hash_do_commit> -> volta as alterações para o word directory para que possam ser revisadas / ajustadas manualmente


